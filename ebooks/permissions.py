from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    # method to return True if user is_staff or if request is in SAFE_METHODS(GET, HEAD, OPTIONS)
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin

