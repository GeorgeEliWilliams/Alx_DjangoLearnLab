from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        # Create authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")
        
        # Create books
        self.book1 = Book.objects.create(
            title="Book One",
            publication_year=2000,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title="Book Two",
            publication_year=2020,
            author=self.author2
        )

        self.list_url = reverse('book-list-create')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})

    def test_list_books(self):
        """Test GET all books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_create_book_authenticated(self):
        """Test POST create book as authenticated user"""
        self.client.login(username='testuser', password='password123')
        data = {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author1.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Test POST create book as unauthenticated user (should fail)"""
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2021,
            "author": self.author1.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_book(self):
        """Test GET single book"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_update_book_authenticated(self):
        """Test PUT update book as authenticated user"""
        self.client.login(username='testuser', password='password123')
        data = {
            "title": "Updated Book",
            "publication_year": 2010,
            "author": self.author1.id
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_update_book_unauthenticated(self):
        """Test PUT update book as unauthenticated user (should fail)"""
        data = {
            "title": "Fail Update",
            "publication_year": 2010,
            "author": self.author1.id
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_authenticated(self):
        """Test DELETE book as authenticated user"""
        self.client.login(username='testuser', password='password123')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_unauthenticated(self):
        """Test DELETE book as unauthenticated user (should fail)"""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_filter_books_by_year(self):
        """Test filtering books by publication_year"""
        response = self.client.get(f"{self.list_url}?publication_year=2000")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book['publication_year'] == 2000 for book in response.data))

    def test_search_books_by_title(self):
        """Test searching books by title"""
        response = self.client.get(f"{self.list_url}?search=Book%20One")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Book One" in book['title'] for book in response.data))

    def test_order_books_by_year_desc(self):
        """Test ordering books by publication_year descending"""
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
