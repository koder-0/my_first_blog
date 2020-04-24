from django.utils import timezone
from django.contrib.auth.models import User
from blog.models import Post
from faker import Faker
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_site.settings')
# django.setup()


def create_post(n):
    fake = Faker()
    for i in range(n):
        id = 1
        title = "post no"+str(id)
        text = fake.text()
        Post.objects.create(
            author=User.objects.get(id=id),
            title=title,
            text=text,
            created_date=timezone.now(),
            published_date=timezone.now()
        )


create_post(10)
