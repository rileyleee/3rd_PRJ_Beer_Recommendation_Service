from django.db import models
# from django.forms import ModelForm
# from beer_recommend_prj import settings


class Column(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        # TODO : 장고의 URL Reverse 기능을 사용하기
        return f"/column/{self.pk}/"

    def __str__(self):
        return f"[{self.pk}] {self.title}"


# class Column_comment(models.Model):
#     event = models.ForeignKey(Column, on_delete=models.CASCADE)
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
#     comment = models.TextField()


class Event(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        # TODO : 장고의 URL Reverse 기능을 사용하기
        return f"/event/{self.pk}/"

    def __str__(self):
        return f"[{self.pk}] {self.title}"


# class Event_comment(models.Model):
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
#     comment = models.TextField()
