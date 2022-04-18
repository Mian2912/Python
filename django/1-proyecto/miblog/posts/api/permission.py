from rest_framework.permissions import BasePermission
#si es admin podra realizar todas las operaciones crud
#si no es admin solo podra leer

class IsAdminOrReadOnly(BasePermission):
    def has    