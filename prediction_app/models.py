from django.db import models

class HeartFailurePrediction(models.Model):
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    cp = models.IntegerField()
    chol = models.FloatField()
    target = models.IntegerField()

class LungCancerPrediction(models.Model):
    age = models.IntegerField()
    wheezing = models.BooleanField()
    fatigue = models.BooleanField()
    coughing = models.BooleanField()
    shortness_of_breath = models.BooleanField()
    smoking = models.BooleanField()
    swallowing_difficulty = models.BooleanField()
    lung_cancer = models.CharField(max_length=5)

class HIVPrediction(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    hiv_diagnoses = models.IntegerField()
    linked_to_care_within_3_months = models.FloatField()
    plwdhi_prevalence = models.FloatField()
    hiv_diagnosis = models.FloatField()

