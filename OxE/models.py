from django.db import models

# Create your models here.

# Create your models here.
class Elibrary(models.Model):
    title         = models.CharField(max_length=120)
    description   = models.TextField(blank=True,null=True)
    price         = models.DecimalField(decimal_places=2,max_digits=10000)
    summery       = models.TextField(blank=True)
    oer           = models.BooleanField(default=True)

class index:
    course_id: int
    course_title: str
    course_description: str
    course_img: str
    course_value : str
    coruse_student : str
    course_math: bool
    course_science: bool
    course_english: bool