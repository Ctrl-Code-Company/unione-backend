from django.db import models

from ckeditor.fields import RichTextField


class Location(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Subject(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Major(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class University(models.Model):
    IELTS_CHOICES = (
        ("5-5.5", "5-5.5"),
        ("6-6.5", "6-6.5"),
        ("7-7.5", "7-7.5"),
        ("8-8.5", "8-8.5"),
        ("9", "9"),
        ("No", "No"),
    )
    MATH_CHOICES = (
        ("Foundation", "Foundation"),
        ("High", "High"),
        ("SAT", "SAT"),
        ("No", "No"),
    )
    LOCATION_TYPE = (
        ("Domestic", "Domestic"),
        ("International", "International")
    )
    ielts_choice = models.CharField(max_length=255, choices=IELTS_CHOICES, default="6-6.5")
    math_choice = models.CharField(max_length=255, choices=MATH_CHOICES, default="SAT")
    title = models.CharField(max_length=255)
    website = models.URLField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to="university/")
    wallpaper = models.ImageField(upload_to="university/", blank=True)
    ielts = models.FloatField(default=0.0)
    sat = models.IntegerField(default=0)
    gpa = models.FloatField(default=0.0)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    location_type = models.CharField(max_length=255, choices=LOCATION_TYPE, default="International")
    scholarship_count = models.PositiveIntegerField()
    acceptance_rate = models.IntegerField()
    in_the_world = models.IntegerField()
    majors = models.ManyToManyField(Major)
    subjects = models.ManyToManyField(Subject)
    fee = models.CharField(max_length=255)
    requirements = RichTextField(
        blank=True,
        null=True,
        config_name='default',
        external_plugin_resources=[(
            'mathjax',
            '/static/ckeditor/ckeditor/plugins/mathjax/',
            'plugin.js',
        )]
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"
