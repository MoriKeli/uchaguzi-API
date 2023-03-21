from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from datetime import datetime
from .models import User, VotingStation
import uuid

@receiver(pre_save, sender=User)
def generate_userID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '').upper()[:25]

    try:
        if datetime.now().strftime('%Y-%m-%d %H:%M:%S') > instance.created.strftime('%Y-%m-%d %H:%M:%S'):
            user_dob = str(instance.dob)    # user's dob
            get_VoterDob = datetime.strptime(user_dob, '%Y-%m-%d')
            current_date = datetime.now()
            user_age = current_date - get_VoterDob
            convert_userAge = int(user_age.days/365.25)
            instance.age = convert_userAge
            
        else:
            user_dob = str(instance.dob)    # user's dob
            get_VoterDob = datetime.strptime(user_dob, '%Y-%m-%d')
            current_date = datetime.now()
            user_age = current_date - get_VoterDob
            convert_userAge = int(user_age.days/365.25)
            instance.age = convert_userAge
    
    except AttributeError:
        return


@receiver(pre_save, sender=VotingStation)
def generate_votingstationID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).upper().replace('-', '')[:25]

