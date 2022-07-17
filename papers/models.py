from django.db import models

# Create your models here.

class pastPaper(models.Model):
    board = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    year = models.IntegerField()
    month = models.CharField(max_length = 10)
    variant = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    questionNum = models.IntegerField()
    answer = models.CharField(max_length=1)
    hardness = models.IntegerField()
    difficulty = models.IntegerField()
    # p


    # Return the required paper 
    def __str__(self):
        return '{}/{}/{}/{}/{}'.format(self.board,  
        self.subject, self.topic, self.year, self.month,    
        self.variant)






