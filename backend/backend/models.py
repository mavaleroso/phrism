from calendar import c
from distutils.command.upload import upload
from statistics import mode
from tabnanny import verbose
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from xmlrpc.client import Boolean
from django.db import models
from django.dispatch import receiver
import os
from django.utils import timezone

# Create your models here.


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    def get_firstname(self):
        return self.first_name.title()
    
    def get_middlename(self):
        return self.middle_name.title() if self.middle_name else ""

    def get_lastname(self):
        return self.last_name.title()
    
    @property
    def get_fullname(self):
        if self.first_name:
            return "{} {}. {}".format(self.first_name.title(), self.middle_name[:1], self.last_name.title()) if self.middle_name else "{} {}".format(self.first_name.title(), self.last_name.title())
        else:
            return None

    class Meta:
        managed = False
        db_table = 'auth_user'



# API Data Library
class Position(models.Model):
    name = models.CharField(max_length=200, unique=True)
    acronym = models.CharField(max_length=50)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "lib_position"

class Division(models.Model):
    name = models.CharField(max_length=200, unique=True)
    acronym = models.CharField(max_length=50)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "lib_division"


class Section(models.Model):
    name = models.CharField(max_length=200, unique=True)
    division = models.ForeignKey(Division,  models.DO_NOTHING)
    acronym = models.CharField(max_length=50)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "lib_section"

    @property
    def division_(self):
        return self.division.name

# Library (Location)

class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)
    status = models.IntegerField()

    class Meta:
        db_table = "lib_region"

class Province(models.Model):
    name = models.CharField(max_length=100, unique=True)
    region = models.ForeignKey(Region, models.DO_NOTHING)
    status = models.IntegerField()

    class Meta:
        db_table = "lib_province"

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=24, unique=True)
    province = models.ForeignKey(Province, models.DO_NOTHING)
    status = models.IntegerField()

    class Meta:
        db_table = "lib_city"

class Barangay(models.Model):
    name = models.CharField(max_length=100, unique=True)
    barangay = models.ForeignKey(City, models.DO_NOTHING)
    status = models.IntegerField()

    class Meta:
        db_table = "lib_barangay"


# User Staff Management


class NameExtension(models.Model):
    name = models.CharField(max_length=24)
    status = models.IntegerField()
    upload_by = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        db_table = 'lib_extension_name'

class CivilStatus(models.Model):
    cs_name = models.CharField(max_length=128, unique=True)
    status = models.IntegerField()
    upload_by = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Civil Status"
        db_table = "lib_civil_status"

class BloodType(models.Model):
    bt_name = models.CharField(max_length=128,unique=True)
    status = models.IntegerField()
    upload_by = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Blood Type"
        db_table = "lib_blood_type"



class EmployeePersonalInfo(models.Model):
    auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    ext_name = models.ForeignKey(NameExtension,models.DO_NOTHING)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=64)
    gender = models.IntegerField()
    civil_status = models.ForeignKey(CivilStatus, models.DO_NOTHING)
    height = models.DecimalField(max_digits=11, decimal_places=2)
    weight = models.DecimalField(max_digits=11, decimal_places=2)
    blood_type = models.ForeignKey(BloodType, models.DO_NOTHING)
    is_filipino = models.IntegerField()
    is_dual_citizenship = models.IntegerField()
    dc_by_birth = models.IntegerField()
    dc_by_naturalization = models.IntegerField()
    mobile_no = models.CharField(max_length=13)
    telephone_no = models.CharField(max_length=10)
    course = models.CharField(max_length=128)
    image = models.FileField(upload_to='pictures/',default='picture/default.jpg')

    @property
    def get_gender(self):
        return "Male" if self.gender == 0 else "Female"
    
    class Meta:
        db_table = 'tbl_employee_personalinfo'


class EmployeeAppStatus(models.Model):
    name = models.CharField(max_length=64, unique=True)
    acronym = models.CharField(max_length=64, unique=True)
    status = models.BooleanField()
    upload_by = models.ForeignKey(AuthUser,models.DO_NOTHING)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'tbl_employee_status'

class EmployeeFundSource(models.Model):
    name = models.CharField(max_length=128, unique=True)
    acronym = models.CharField(max_length=64, unique=True)
    status = models.BooleanField()
    upload_by = models.ForeignKey(AuthUser, models.DO_NOTHING)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'tbl_employee_fund_source'


class EmployeeUserDetails(models.Model):
    epi = models.ForeignKey(EmployeePersonalInfo, models.DO_NOTHING)
    id_number = models.CharField(max_length=255)
    emp_status = models.ForeignKey(EmployeeAppStatus,models.DO_NOTHING)
    emp_pos = models.ForeignKey(Position,models.DO_NOTHING)
    emp_division = models.ForeignKey(Division,models.DO_NOTHING)
    emp_section = models.ForeignKey(Section, models.DO_NOTHING)
    emp_fund = models.ForeignKey(EmployeeFundSource, models.DO_NOTHING)
    salary_grade = models.CharField(max_length=255)
    salary_rate = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_employee_user_details'
    

# Landing Page
class Announcements(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    attachments = models.FileField(upload_to='announcement/documents')
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tbl_announcements'

class FeedbackForm(models.Model):
    rating = models.CharField(max_length=64)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_feedback_form'

class Events(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    attachments = models.FileField(upload_to='events/documents')
    event_date = models.DateTimeField()
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
         db_table = 'tbl_events'

#about pilar 
class AboutPilar(models.Model):
    overview = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    history = models.TextField()
    geography = models.TextField()
    climate = models.TextField()
    demographics = models.TextField()
    socio_cultural = models.TextField()
    education = models.TextField()
    social_development = models.TextField()
    environment = models.TextField()
    public_infrastructure = models.TextField()
    public_services = models.TextField()
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING)
    image = models.ImageField(upload_to='about/images')
    attachments = models.FileField(upload_to='about/documents')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tbl_about_pilar'

