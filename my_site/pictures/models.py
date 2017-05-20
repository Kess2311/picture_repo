from django.db import models
from .validator import validate_file_extension
import datetime, os


class Picture(models.Model):
    CHITTENANGO = 'C'
    NY = 'N'
    CARS = 'H'
    COLORADO = 'D'
    NIGHT = 'B'

    PICTURE_CHOICES = (
        (CARS, 'Cars'),
        (CHITTENANGO, 'Chittenango'),
        (COLORADO, 'Colorado'),
        (NIGHT, 'Night'),
        (NY, 'New York'),
    )

    def content_file_name(self, filename):
        """
        Used to rename the file to pk of the doctor and test
        gives a unique name for each file
        :param filename: original filename
        :return: new filename
        """
        ext = filename.split('.')[-1]
        filename = "%s_%s.%s" % (filename, self.id, ext)
        return os.path.join('pictures/static/pictures/', filename)

    description = models.TextField(default='Uploaded Photo')
    location = models.CharField(max_length=1, choices=PICTURE_CHOICES, default='A')
    date = models.DateField(default=datetime.date.today)
    file = models.FileField(default=None, upload_to=content_file_name, validators=[validate_file_extension])
