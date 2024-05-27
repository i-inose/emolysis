from django.db import models

class TextInput(models.Model):
  text = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.text[:50]