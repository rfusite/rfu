from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(null=True, blank=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def like(self):
        self.likes += 1
        self.save()


class BlogImage(models.Model):
    post = models.ForeignKey(BlogPost, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/')
