class blog(models.Model):
    title = models.CharField()
    context = models.TextField()
    after = models.DateTimeField()
    initial = models.DateTimeField()