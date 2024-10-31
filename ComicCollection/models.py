from django.contrib.auth.models import User
from django.db import models


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Series(models.Model):
    name = models.CharField(max_length=200)
    start_year = models.IntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    count_issues = models.IntegerField()
    count_issues_in_collection = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Issue(models.Model):
    issue_number = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=200)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    cover_root_path = models.CharField()
    cover_date = models.DateField()
    stores_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

