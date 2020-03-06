from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, fullname, username, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        # now = timezone.now()
        # extra_fields.setdefault('is_staff', False)
        # extra_fields.setdefault('is_superuser', False)
        # extra_fields.setdefault('is_active', False)

        if not fullname:
            raise ValueError(_('The fullname must be set'))
        if not username:
            raise ValueError(_('The username must be set'))
        if not email:
            raise ValueError(_('User must have an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email,
                          username = username,
                          fullname = fullname
                        #   is_staff = is_staff,
                        #   is_superuser = is_superuser,
                        #   last_login = now,
                        #   created_at = now,
                        #   updated_at = now,
                          **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)