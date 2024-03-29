from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, \
                                    PermissionsMixin  

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extrafield):
        # create and save a new user 
        if not email:
            raise ValueError('user must have an email address !')
        user = self.model(email=self.normalize_email(email), **extrafield)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        # create and save a new super user
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    # custom user model that support using email instead of username 
    email = models.EmailField(max_length=255, unique=True)

    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default = False)

    objects = UserManager()  # class attribute ทุกๆ instance จะมีเหมือนกันหมด เพิ่งเคยเห็นการ inherite เเบบนี้ ว้าวๆๆ

    USERNAME_FIELD = 'email'



