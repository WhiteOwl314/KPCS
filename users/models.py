from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    birthdate = models.DateField()
    telNumber = models.BigIntegerField()
    phoneNumber = models.BigIntegerField()
    address = models.CharField(max_length=140)
    connectCounselor = models.ForeignKey(
        "User", on_delete=models.CASCADE, blank=True, null=True
    )
    joinPath = models.CharField(max_length=200, blank=True)
