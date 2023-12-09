from django.db import models
from task.models import TaskModel

class CategoryModel(models.Model):
    categoryName = models.CharField(max_length=255)
    task = models.ManyToManyField(TaskModel, related_name='categories')

    def __str__(self):
        return self.categoryName