from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    """To allow read-only for any request"""
    if request.method in permissions.SAFE_METHODS:
      return True

    """Grant write-permissions to only owner"""
    return obj.owner == request.user
