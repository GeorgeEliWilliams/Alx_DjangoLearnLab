## Permissions and Groups Setup

We use Django’s permission system to restrict access to Book model operations.

### Custom Permissions
Defined in `Book` model:
- can_view
- can_create
- can_edit
- can_delete

### Groups
1. Viewers: `can_view`
2. Editors: `can_view`, `can_create`, `can_edit`
3. Admins: All permissions

### How to Assign
- Go to Django admin
- Create groups
- Assign permissions
- Assign users to appropriate groups

### Enforced in Views Using:
- `@permission_required('bookshelf.can_edit')` and similar decorators
