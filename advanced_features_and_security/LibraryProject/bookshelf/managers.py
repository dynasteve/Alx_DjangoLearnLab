from django.contrib.auth.models import UserManager

class CustomUserManager(UserManager):
  """
  Custom manager for CustomUser model
  """
  
  def create_user(self, username, password=None, **kwargs):
    if not username:
        raise ValueError("Username must be set")

    username = self.model.normalize_username(username)
    
    user = self.model(username=username, **kwargs)
    
    if password:
        user.set_password(password)
    
    # Only default to False if not explicitly passed
    if 'is_staff' not in kwargs:
        user.is_staff = False
    if 'is_superuser' not in kwargs:
        user.is_superuser = False

    user.save(using=self._db)
    return user
  
  def create_superuser(self, username, password=None, **kwargs):
    kwargs.setdefault("is_staff", True)
    kwargs.setdefault("is_superuser", True)
    kwargs.setdefault("is_active", True)

    if kwargs.get("is_staff") is not True:
        raise ValueError("Superuser must have is_staff=True")

    if kwargs.get("is_superuser") is not True:
        raise ValueError("Superuser must have is_superuser=True")

    return self.create_user(username=username, password=password, **kwargs)
