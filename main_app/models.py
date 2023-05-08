from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.


class Boot(models.Model):
  name = models.CharField(max_length=50)
  manufacturer = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('boots_detail', kwargs={'pk': self.id})


class Player(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=30)
    club = models.CharField(max_length=100)
    birth_date = models.DateField('Birth Date')
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    boots = models.ManyToManyField(Boot)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('player_detail', args=[str(self.id)])

    
class Training(models.Model):
  
  TRAININGS = (
    ('M', 'Morning'),
    ('D', 'Day'),
    ('E', 'Evening'),
  ) 
  date = models.DateField('Training Date')
  training = models.CharField(
    max_length=1,
    choices=TRAININGS,
    # default=TRAININGS[0][0],
    verbose_name='training time'
  )
  player = models.ForeignKey(
    Player,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_training_display()} on {self.date}"

  class Meta:
    ordering = ['-date']