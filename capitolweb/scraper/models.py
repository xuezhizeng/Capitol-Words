from django.db import models


class CRECScraperResult(models.Model):

    def __str__(self):
        if self.success:
            outcome = 'successful'
        else:
            outcome = 'failed'
        date_str = self.date.strftime('%Y-%m-%d')
        return 'CREC Issued Date: {0}, scraping {1}: {2}'.format(
            date_str, outcome, self.message
        )

    date = models.DateField()
    success = models.BooleanField()
    message = models.TextField()
    num_crec_files_uploaded = models.IntegerField(default=0)
