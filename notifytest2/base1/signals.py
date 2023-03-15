from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Professor
#from django_plpy.installer import pltrigger


# @pltrigger(event="INSERT", when="AFTER", model=User)
# def professor(new: User, old : User, td, plpy):
#     # user to automatically create a professor object when ever a new user
#     # is created
#     if created:
#         print('in signal')
#         Professor.objects.create(
#             user = instance,
#             fname = instance.username,
#         )
#         print("profile created")
#     else:
#         print('profile not created')

    
def professor(sender, instance, created, **kwargs):
    # user to automatically create a professor object when ever a new user
    # is created
    if created:
        print('in signal')
        Professor.objects.create(
            user = instance,
            fname = instance.username,
        )
        print("profile created")
    else:
        print('profile not created')

    
post_save.connect(professor, sender  = User)