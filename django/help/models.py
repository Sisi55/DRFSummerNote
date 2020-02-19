from django.db import models
from root.storages import PublicMediaStorage
import os
from uuid import uuid4
from django.utils import timezone


# 드롭박스: 1:1 요청, 수정 요청, 게시 요청
# 제목 *
# 내용 *
class Question(models.Model):
    title = models.CharField(
        max_length=100
    )
    contents = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )


def help_image_upload_to(instance, filename):
    ymd_path = timezone.now().strftime('%Y/%m/%d/%H/%M')
    uuid_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()
    return '/'.join([
        ymd_path,
        uuid_name + extension,
    ])


class HelpContentImage(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.FileField(
        storage=PublicMediaStorage(),
        upload_to=help_image_upload_to
    )
