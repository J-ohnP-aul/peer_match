from django.db import models
from django.conf import settings

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.code} - {self.name}"
      
class Course(models.Model):
  school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="courses")
  name = models.CharField(max_length=150)
  code = models.CharField(max_length=20, unique=True)
  reg_prefix = models.CharField(max_length=10, unique=True)  #in16 sftware
  description = models.TextField(blank=True)
  
  def __str__(self):
     return f"{self.code} - {self.name}"
  
class Unit(models.Model):
  course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="units")
  code = models.CharField(max_length=20)
  name = models.CharField(max_length=150)

  year = models.PositiveSmallIntegerField()
  semester = models.PositiveSmallIntegerField()

  def __str__(self):
      return f"{self.code} - {self.name}"

class StudentUnit(models.Model):  # record the units that belong to a particular student
  student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="academic_units")
  unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="students")
  class Meta:
    constraints = [
        models.UniqueConstraint(
            fields=["student", "unit"],
            name="unique_student_unit"
        )
    ]

  def __str__(self):
      return f"{self.student} - {self.unit}"
    
class StudentAcademicProfile(models.Model): #who is this student academically
    student = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="academic_profile"
    )
    reg_no = models.CharField(
        max_length=30,
        unique=True
    )
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name="students")
    year_joined = models.PositiveSmallIntegerField()
    def __str__(self):
        return f"{self.student.username} - {self.reg_no}"