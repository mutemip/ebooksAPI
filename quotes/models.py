from django.db import models


class Quote(models.Model):
    quote_author = models.CharField(max_length=55)
    quote_body = models.TextField()
    context = models.CharField(max_length=255, blank=True)
    source = models.CharField(max_length=155)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quote_author
