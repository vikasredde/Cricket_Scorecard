from django.db import models

class Team(models.Model):
    
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Player(models.Model):


    name=models.CharField(max_length=100)
    team=models.ForeignKey(Team,on_delete=models.CASCADE,related_name='Players')


    def __str__(self):
        return self.name
