from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    question = models.CharField(max_length=1000)
    answer = models.TextField()
    created = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.question