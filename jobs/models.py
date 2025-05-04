from django.db import models

# Company Model
class Company(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name


# Location Model (linked to Company)
class Location(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="locations")
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city}, {self.country}"


# Job Model (linked to Company)
class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="jobs")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="jobs")
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# Applicant Model (linked to Job)
class Applicant(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applicants")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    resume = models.FileField(upload_to="resumes/")
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} for {self.job.title}"
