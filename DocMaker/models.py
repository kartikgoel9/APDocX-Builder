from django.db import models

from django.utils import timezone

import datetime

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Subject(models.Model):
    subject_owner = models.ForeignKey(User, related_name='experiment_by', on_delete=models.CASCADE)
    subject_faculty = models.CharField(max_length=30, null=True, blank=True)
    subject_name = models.CharField(max_length=80, blank=True, null=True)
    semester = models.IntegerField()
    roll_no = models.CharField(max_length=30, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject_name




class Experiments(models.Model):
    experiment_name = models.ForeignKey(Subject, related_name='experiments_by_subjects', on_delete=models.CASCADE,
                                        null=True, blank=True)
    experiment_owner = models.ForeignKey("User", related_name="experiment_by_which_owner", on_delete=models.CASCADE)
    experiment_number = models.IntegerField(null=True, blank=True)
    aim = models.TextField(max_length=500)
    source_code = models.TextField(max_length=10000)
    image_one = models.ImageField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.aim

    @property
    def imageURL(self):
        try:
            url = self.image_one.url
        except:
            url = ''
        return url


class UserCurrentSelectedSubjects(models.Model):
    subject_selection_owner = models.ForeignKey(User, related_name='subject_selected_by', on_delete=models.CASCADE)
    selected_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.selected_subject.subject_name
