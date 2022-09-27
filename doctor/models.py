import os
from django.db import models
from ckeditor.fields import RichTextField

class OperationCatagory(models.Model):
    category_name   = models.CharField(max_length=100)
    category_image  = models.ImageField(upload_to='images/category_image', blank=True)
    details         = models.CharField(max_length=200, blank=True)
    sequence        = models.IntegerField()
    status          = models.BooleanField(default=1)
    def __str__(self):
        return self.category_name

class GalleryCatagory(models.Model):
    gallery_category   = models.CharField(max_length=100)
    sequence        = models.IntegerField()
    status          = models.BooleanField(default=1)
    def __str__(self):
        return self.gallery_category

class SliderInfo(models.Model):
    slider_title   = models.CharField(max_length=100, blank=True)
    slider_images  = models.ImageField(upload_to='images/slider')
    slider_order   = models.IntegerField()
    status         = models.BooleanField(default=True)
    upload_date    = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.slider_title

    class Meta:
        verbose_name = 'Slider Image'
        verbose_name_plural = 'Slider Images'


class PersonalProfile(models.Model):
    full_name         = models.CharField(max_length=160)
    qualification     = models.CharField(max_length=160,blank=True)
    designation       = models.CharField(max_length=160,blank=True)
    specialist        = models.CharField(max_length=260,blank=True)
    specialist2        = models.CharField(max_length=260,blank=True)
    specialist3        = models.CharField(max_length=260,blank=True)
    specialist4        = models.CharField(max_length=260,blank=True)
    working_place     = models.CharField(max_length=160,blank=True)
    email             = models.EmailField(max_length=70,blank=True)
    phone             = models.CharField(max_length=20,blank=True)
    mobile            = models.CharField(max_length=15,blank=True)
    address           = models.CharField(max_length=200,blank=True)
    profile_message   = RichTextField()
    logo              = models.ImageField(upload_to='images/logo', blank=True)
    profile_picture   = models.ImageField(upload_to='images/logo', blank=True)
    facebook_id       = models.CharField(max_length=200,blank=True)
    twitter_id        = models.CharField(max_length=200,blank=True)
    status            = models.BooleanField(default=True)



class GalleryInfo(models.Model):
    gallery_category = models.ForeignKey(GalleryCatagory, on_delete = models.CASCADE)
    gallery_title   = models.CharField(max_length=100, blank=True)
    gallery_images  = models.ImageField(upload_to='images/gallery')
    gallery_order   = models.IntegerField()
    status          = models.BooleanField(default=True)
    upload_date     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gallery_title

    class Meta:
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallerys'


class OperationPost(models.Model):
    operation_category  = models.ForeignKey(OperationCatagory, on_delete = models.CASCADE)
    operation_name      = models.CharField(max_length=100, blank=True)
    operation_title     = models.CharField(max_length=100, blank=True)
    operation_place     = models.CharField(max_length=100, blank=True)
    operation_details   = RichTextField()
    before_images       = models.ImageField(upload_to='images/operations')
    after_images        = models.ImageField(upload_to='images/operations')
    status              = models.BooleanField(default=True)
    operation_date      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.operation_title

    class Meta:
        verbose_name = 'Operation Post'
        verbose_name_plural = 'Add Operation Post'

class MyAward(models.Model):
    award_title    = models.CharField(max_length=100, blank=True)
    award_year     = models.CharField(max_length=100, blank=True)
    for_award      = models.CharField(max_length=100, blank=True)
    place          = models.CharField(max_length=100, blank=True)
    award_details  = RichTextField()
    award_images   = models.ImageField(upload_to='images/award')
    status         = models.BooleanField(default=True)
    award_date     = models.DateTimeField(auto_now_add=True)


class MyEducation(models.Model):
    name_of_degree    = models.CharField(max_length=100, blank=True)
    institute_name    = models.CharField(max_length=100, blank=True)
    passing_year      = models.CharField(max_length=100, blank=True)
    section          = models.CharField(max_length=100, blank=True)
    CGPA              = models.CharField(max_length=100, blank=True)
    board             = models.CharField(max_length=100, blank=True)
    status            = models.BooleanField(default=True)
    pub_date          = models.DateTimeField(auto_now_add=True)


class MyProgram(models.Model):
    program_title      = models.CharField(max_length=100, blank=True)
    program_details    = RichTextField()
    program_place      = models.CharField(max_length=100, blank=True)
    program_image      = models.ImageField(upload_to='images/program_image')
    program_date       = models.DateTimeField(auto_now_add=True)
    status             = models.BooleanField(default=True)

    def __str__(self):
        return self.program_title

    class Meta:
        verbose_name = 'My Program'
        verbose_name_plural = 'My Programs'


class AcademicQualification(models.Model):
    education_label     = models.CharField(max_length=100, blank=True)
    institute_name      = models.CharField(max_length=100, blank=True)
    group               = models.CharField(max_length=100, blank=True)
    board               = models.CharField(max_length=100, blank=True)
    passing_year        = models.CharField(max_length=100, blank=True)
    division            = models.CharField(max_length=100, blank=True)
    status              = models.BooleanField(default=True)

    def __str__(self):
        return self.education_label

    class Meta:
        verbose_name = 'Qualification'
        verbose_name_plural = 'Academic Qualification'


class Experience(models.Model):
    course_name     = models.CharField(max_length=100, blank=True)
    awording_body   = models.CharField(max_length=100, blank=True)
    duration        = models.CharField(max_length=100, blank=True)
    country         = models.CharField(max_length=100, blank=True)
    remark          = models.CharField(max_length=100, blank=True)
    status          = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'My Experience'



class SocialActivities(models.Model):
    title           = models.CharField(max_length=100, blank=True)
    details         = RichTextField()
    place           = models.CharField(max_length=100, blank=True)
    country         = models.CharField(max_length=100, blank=True)
    program_image   = models.ImageField(upload_to='images/program_image')
    program_date    = models.DateTimeField(auto_now_add=True)
    status          = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Activities'
        verbose_name_plural = 'Social Activities'




 









