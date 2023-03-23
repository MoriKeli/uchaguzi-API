from accounts.models import User
from django.db import models

class Aspirants(models.Model):
    """
        This model is to used to map aspirants details. An aspirant in this case is a registered voter who is vying for a given electoral seat, e.g.
        MCA, MP, Women Rep., etc. This model stores aspirants details besides nomination form and profile pic. Electoral officials will nominate a candidate
        while the Chairperson or Assistant Chairperson will approve a nominated candidate .
    """
    id  = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    name = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)     # name of the aspirant
    alias = models.CharField(max_length=30, blank=True)     # nickname or alias of the aspirant, e.g. "Iron lady" or "Tunu" or "Freedom fighter"
    electoral_post = models.CharField(max_length=70, blank=False)   # post the aspirant is vying for: Women Rep., President, MCA
    political_party = models.CharField(max_length=100, blank=False)
    slogan = models.CharField(max_length=50, blank=False)   # slogan his/her party is using for campaign, e.g. "Jubilee", "Inawezekana"
    manifesto = models.TextField(blank=False)
    nomination_form = models.FileField(upload_to='Nomination-Forms/')
    pic = models.ImageField(upload_to='Aspirants-Dps/', null=False)
    nominated = models.BooleanField(default=False, editable=False, blank=False)
    approved = models.BooleanField(default=False, editable=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Electoral Aspirants'
        ordering = ['name', 'electoral_post']

    def __str__(self):
        return self.name
    
class VotingResults(models.Model):
    """ This table stores election results. """
    id = models.CharField(max_length=30, primary_key=True, unique=True, editable=False)
    aspirant = models.ForeignKey(Aspirants, on_delete=models.DO_NOTHING, editable=False)   # Name of a given aspirant - person vying for a given electoral seat
    total_votes = models.PositiveIntegerField(default=0, editable=False)    # Total votes garnered in favor of the stated aspirant
    voter_turnout = models.PositiveIntegerField(default=0, editable=False)      # Total voters who voted in favor of the stated aspirant
    percentage = models.DecimalField(max_digits=3, decimal_places=2, default=0.0, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Election results'
        ordering = ['-total_votes']

    def __str__(self):
        return self.aspirant

class PollsResults(models.Model):
    """ This model saves info about poll results just like VotingResults """
    id = models.CharField(max_length=30, primary_key=True, unique=True, editable=False)
    aspirant = models.ForeignKey(Aspirants, on_delete=models.DO_NOTHING, editable=False)
    total_votes = models.PositiveIntegerField(default=0, editable=False)
    voters_turnout = models.PositiveIntegerField(default=0, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Polls results'
        ordering = ['total_votes']

    def __str__(self):
        return self.aspirant


class Nominations(models.Model):
    """ Stores info. about every nominated aspirants in addition to officials who have nominated an aspirant """
    aspirant = models.ForeignKey(Aspirants, on_delete=models.CASCADE, editable=False)
    officer_name = models.ForeignKey(User, on_delete=models.DO_NOTHING, editable=False)
    role = models.CharField(max_length=50, blank=False)
    is_nominated = models.BooleanField(default=False, editable=False)   # returns True if aspirant is nominated else False.
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Nomination details'
        ordering = []

    def __str__(self):
        return self.officer_name


class Voters(models.Model):
    """ Stores details of voters who have elected their leaders. """
    id = models.CharField(max_length=30, primary_key=True, unique=True, editable=False)
    voter = models.OneToOneField(User, on_delete=models.DO_NOTHING, editable=False)
    mca = models.BooleanField(default=False, editable=False, db_column='Member of County Assembly')
    mp = models.BooleanField(default=False, editable=False, db_tablespace='Member of Parliament')
    women_rep = models.BooleanField(default=False, editable=False, db_tablespace='Women Representative')
    senator = models.BooleanField(default=False, editable=False)
    governor = models.BooleanField(default=False, editable=False)
    president = models.BooleanField(default=False, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Voters Elections Info.'
        ordering = ['voter']

    def __str__(self):
        return self.voter


class Polled(models.Model):
    """ Stores details of voters who have participated in polls. """
    id = models.CharField(max_length=30, primary_key=True, unique=True, editable=False)
    voter = models.OneToOneField(User, on_delete=models.DO_NOTHING, editable=False)
    mca = models.BooleanField(default=False, editable=False, db_column='Member of County Assembly')
    mp = models.BooleanField(default=False, editable=False, db_tablespace='Member of Parliament')
    women_rep = models.BooleanField(default=False, editable=False, db_tablespace='Women Representative')
    senator = models.BooleanField(default=False, editable=False)
    governor = models.BooleanField(default=False, editable=False)
    president = models.BooleanField(default=False, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Polled'
        ordering = ['voter']

