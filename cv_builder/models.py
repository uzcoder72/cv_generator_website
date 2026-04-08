from django.db import models

class Resume(models.Model):
    # 1. Personal Info
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    contacts = models.CharField(max_length=100, help_text="Phone number, address")
    email = models.EmailField()
    social_media = models.CharField(max_length=200, help_text="LinkedIn, GitHub, etc.")
    specialization = models.CharField(max_length=100, help_text="e.g. Software Engineer")
    
    # 2. Education
    edu_start = models.DateField(help_text="Start Date")
    edu_end = models.DateField(help_text="End Date")
    edu_institution = models.CharField(max_length=150, help_text="University Name")
    edu_degree = models.CharField(max_length=150, help_text="Degree Name")
    
    # 3. Experience
    exp_start = models.DateField(help_text="Start Date")
    exp_end = models.DateField(help_text="End Date")
    exp_employer = models.CharField(max_length=150)
    exp_position = models.CharField(max_length=150)
    
    # 4. Skills
    skills = models.TextField(help_text="Comma-separated list of skills")
    
    # 5. Photo
    photo = models.ImageField(upload_to='resume_photos/')
    
    # 6. Languages
    languages = models.CharField(max_length=200, help_text="Comma-separated languages")
    
    # 7. Extra info
    extra_info = models.TextField(blank=True, null=True) # blank=True so it's strictly optional

    def __str__(self):
        return f"{self.name} {self.surname}'s Resume"
