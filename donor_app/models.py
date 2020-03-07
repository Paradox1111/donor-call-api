from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.utils import timezone
# from django.contrib.auth.models import (
#     AbstractBaseUser, BaseUserManager, PermissionsMixin
# )
# from django.utils.translation import gettext_lazy as _

# #manager pattern from https://kite.com/blog/python/custom-django-user-model/
# class StewardManager(BaseUserManager):
#     def create_steward(
#             self, name, password=None,
#             commit=True):
#         """
#         Creates and saves a User with the given name
#         and password.
#         """
#         if not name:
#             raise ValueError(_('Stewards must have a name'))
#         if not name:
#             raise ValueError(_('Stewards must have a password'))

#         steward = self.model(
#             name=name
#         )

#         steward.set_password(password)
#         if commit:
#             steward.save(using=self._db)
#         return steward

#     def create_superuser(self, name, password):
#         """
#         Creates and saves a superuser with the given email, first name,
#         last name and password.
#         """
#         steward = self.create_steward(
 
#             password=password,
#             name=name,
#             commit=False,
#         )
#         steward.is_staff = True
#         steward.is_superuser = True
#         steward.save(using=self._db)
#         return steward


# class Steward(AbstractBaseUser, PermissionsMixin):
#     name = models.CharField(
#         verbose_name=_('email address'), max_length=255, unique=True
#     )
#     # password field supplied by AbstractBaseUser
#     # last_login field supplied by AbstractBaseUser

#     is_active = models.BooleanField(
#         _('active'),
#         default=True,
#         help_text=_(
#             'Designates whether this user should be treated as active. '
#             'Unselect this instead of deleting accounts.'
#         ),
#     )
#     is_staff = models.BooleanField(
#         _('staff status'),
#         default=False,
#         help_text=_(
#             'Designates whether the user can log into this admin site.'
#         ),
#     )
#     # is_superuser field provided by PermissionsMixin
#     # groups field provided by PermissionsMixin
#     # user_permissions field provided by PermissionsMixin

#     date_joined = models.DateTimeField(
#         _('date joined'), default=timezone.now
#     )

#     objects = StewardManager()

#     USERNAME_FIELD = 'name'
#     REQUIRED_FIELDS = ['password']

#     def __str__(self):
#         return self.name

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

# from https://simpleisbetterthancomplex.com/tutorial/2016/11/23/how-to-add-user-profile-to-django-admin.html
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Donor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donors', default=1)
    botsteward = models.CharField(max_length=100, default="Gretchen Bond")
    orgName = models.CharField(max_length=100, default="")
    lastname = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    paymentnum = models.CharField(max_length=100, default="")
    yeartotal = models.CharField(max_length=100, default="")
    lastgift = models.CharField(max_length=100, default="")
    lastgiftdate = models.CharField(max_length=100, default="")
    nextlastgift = models.CharField(max_length=100, default="")
    nextlastgiftdate = models.CharField(max_length=100, default="")
    comments = models.CharField(max_length=100, default="", blank=True)
    def __str__(self):
        return f'{self.orgName} {self.lastname}'