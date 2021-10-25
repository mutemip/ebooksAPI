from django.db import models


class Quote(models.Model):
    quote_author = models.CharField(max_length=55)
    quote_body = models.TextField(blank=True, null=True)
    context = models.CharField(max_length=55)
    source = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.quote_author)
