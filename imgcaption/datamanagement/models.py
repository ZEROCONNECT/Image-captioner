import uuid
from django.db import models

# Create your models here.

class ImageDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    img_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    caption_generated = models.TextField()
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "imagedetails"
        managed = True
        verbose_name = "ImageDetail"
        verbose_name_plural = "ImageDetails"