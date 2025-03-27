from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


User = get_user_model()

class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, username = None, email=None):
        try:
            user = User.objects.get(username=username, email=email)
            if user.groups.filter(name="Teacher").exists():
                return user
            elif user.groups.filter(name="Student").exists():
                return user
        except User.DoesNotExist:
            return None
        return None
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None