from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()

    # NOTE-TO-SELF:
    # This is setting the default to the function,
    # NOT the value, otherwise every object would
    # have the time the class was read in.
    created_at = models.DateTimeField(
        default=timezone.now,
        blank=False,
        null=False,
    )

    # last_updated_at = models.DateTimeField(
    #     default=timezone.now,
    #     blank=False,
    #     null=False,
    # )

    published_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    def publish(self):
        # NOTE-TO-SELF:
        # This time, we want the exact timestamp, so
        # we're calling the now method
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
