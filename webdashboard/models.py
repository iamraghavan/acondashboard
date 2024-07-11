from django.db import models

class WebdashboardFolder(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'webdashboard_folder'

    def __str__(self):
        return self.name

class WebdashboardImage(models.Model):
    name = models.CharField(max_length=100)
    file = models.CharField(max_length=100)
    firebase_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    folder = models.ForeignKey(WebdashboardFolder, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'webdashboard_image'
    
    def __str__(self):
        return self.name
