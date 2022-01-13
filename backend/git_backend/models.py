from django.db import models

# Create your models here.


class PullRequestModel(models.Model):

    class PullRequestStatus(models.TextChoices):
        STATUS_OPEN = 'OP', 'OPEN'
        STATUS_CLOSED = 'CL', 'CLOSED'
        STATUS_MERGED = 'MR', 'MERGED'

    status = models.CharField(
        max_length=2,
        choices=PullRequestStatus.choices,
        default=PullRequestStatus.STATUS_OPEN
    )
    base_branch_name = models.CharField(max_length=200)
    compare_branch_name = models.CharField(max_length=200)
    merge_commit_message = models.CharField(
        max_length=500, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
