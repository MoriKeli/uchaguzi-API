from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """"
        This is the User model that will be used by the API as the default user model. The model contains user's profile i.e. voters and officials.
        There are two boolean fields to check distinguish users:
            - is_voter: returns True if a user is a registered voter else False
            - is_official: returns True if a user is a registered electoral official else False

            NOTE: Both fields cannot be checked at the same time. One can either be an electoral official or a registered voter. 
    """
    id = models.CharField(max_length=25, primary_key=True,  unique=True, editable=False)
    first_name = models.CharField(max_length=100, editable=False, blank=False)
    last_name = models.CharField(max_length=100, editable=False, blank=False)
    username = models.CharField(max_length=70, unique=True, editable=False)
    profile_pic = models.ImageField(upload_to='User-Dps/', default='default.png')
    email = models.EmailField(unique=True, blank=False)
    age = models.PositiveIntegerField(default=0, null=True)
    dob = models.DateField(blank=False, null=True)
    gender = models.CharField(max_length=10, blank=False)
    national_id = models.CharField(max_length=8, blank=False)   # A kenyan national id. no. has a max. of 8 digits
    phone_no = models.CharField(max_length=10, blank=False)     # store phone numbers without Kenyan phone no. code, i.e +254
    role = models.CharField(max_length=25, blank=False)     # stores the role of a given electoral official.
    is_voter = models.BooleanField(default=False, blank=False)
    is_official = models.BooleanField(default=False, blank=False)
    edited = models.DateTimeField(auto_now=True)    # updated date and time for every instance a user updates his profile

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ['username']
        verbose_name_plural = 'Users'


class VotingStation(models.Model):
    """
        This model stores info. of a given voter. Its details entail where a given voter will cast his/her vote.
        For example, if a voter is to vote in Nairobi County, Embakasi Constituency, Kayole East ward then s/he cannot
        vote for other nominated aspirants in Kisumu or Mombasa. He/she can only vote for Nairobi aspirants. 
    """
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    voter = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    county = models.CharField(max_length=50, blank=False)
    constituency = models.CharField(max_length=70, blank=False)
    ward = models.CharField(max_length=70, blank=False)
    is_registered = models.BooleanField(default=False, editable=False, blank=False)
    registered = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Voting Stations'
        ordering = ['county', 'constituency']

    def __str__(self):
        return self.voter.username

    