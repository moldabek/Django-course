from django.db import models


class List(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')

    class Meta:
        verbose_name_plural = "Lists"
        verbose_name = "List"

    def get_absolute_url(self):
        return f"list_item/{self.id}/"

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    created = models.DateField(auto_now_add=True, verbose_name="Created")
    due_on = models.DateField(verbose_name="Due on")
    owner = models.CharField(max_length=255, verbose_name="Owner")
    mark = models.BooleanField(default=False, verbose_name="Mark")
    list = models.ForeignKey(to=List, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Tasks"
        verbose_name = "Task"

    def __str__(self):
        return self.name
