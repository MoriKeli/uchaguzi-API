from django.db.models.signals import pre_save, post_save
from .models import Aspirants, VotingResults
from django.dispatch import receiver
from uuid import uuid4


@receiver(pre_save, sender=Aspirants)
def generate_aspirantsID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid4()).upper().replace('-', '')

@receiver(pre_save, sender=VotingResults)
def generate_resultsID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid4()).replace('-', '')

