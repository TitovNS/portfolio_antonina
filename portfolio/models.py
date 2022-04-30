from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='posts/images', unique=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    text = RichTextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class MyWork(models.Model):
    title = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='works/images', unique=True)
    video = models.FileField(upload_to='works/video', unique=True)
    text = models.TextField()

    def __str__(self):
        return self.title


class Biography(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='biography', unique=True)
    text = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials', unique=True)
    text = models.TextField()


class About(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='posts/images', unique=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    text = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

