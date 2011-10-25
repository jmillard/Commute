from django.db import models

class City(models.Model):
    city = models.CharField(max_length=100)
    city_slug = models.SlugField()
    def __unicode__(self):
        return self.city

class State(models.Model):
    state = models.CharField(max_length=2)
    state_slug = models.SlugField()
    def __unicode__(self):
        return self.state

class Zipcode(models.Model):
    zipcode = models.CharField(max_length=5)
    zipcode_slug = models.SlugField()
    def __unicode__(self):
        return self.zipcode

class Location(models.Model):
    address = models.CharField(max_length=255)
    city = models.ForeignKey(City)
    state = models.ForeignKey(State)
    zipcode = models.ForeignKey(Zipcode)
    def __unicode__(self):
        return self.location

    
