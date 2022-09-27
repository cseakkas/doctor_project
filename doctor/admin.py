from django.contrib import admin
from . import models
# Register your models here.

class OperationCatagoryAdmin(admin.ModelAdmin):
    list_display    = ['category_name','sequence', 'details','status',]
    search_fields   = ['category_name','details','status',]
    list_filter     = ['category_name','details',]
    

class GalleryCatagoryAdmin(admin.ModelAdmin):
    list_display    = ['gallery_category','sequence', 'status',]
    search_fields   = ['gallery_category','sequence','status',]
    list_filter     = ['gallery_category','sequence',]
    
class SliderInfoAdmin(admin.ModelAdmin):
    list_display    = ['slider_title', 'slider_order', 'slider_images', 'upload_date',  'status',]
    search_fields   = ['slider_title', 'slider_order', 'status',]
    list_filter     = ['status',]

class PersonalProfileAdmin(admin.ModelAdmin):
    list_display    = ['full_name', 'qualification', 'designation',  'mobile', 'email', 'status',]
    search_fields   = ['full_name', 'qualification', 'designation',  'mobile', 'email', 'status',]
    list_filter     = ['full_name', 'qualification','status',]

class GalleryInfoAdmin(admin.ModelAdmin):
    list_display    = ['gallery_category', 'gallery_title', 'gallery_order', 'status',]
    search_fields   = ['gallery_category','gallery_title',]
    list_filter     = ['status',]

class OperationPostAdmin(admin.ModelAdmin):
    list_display    = ['operation_category', 'operation_name', 'operation_title', 'operation_date', 'status',]
    search_fields   = ['operation_category','operation_name', 'operation_date',]
    list_filter     = ['operation_category','status',]

class MyAwardAdmin(admin.ModelAdmin):
    list_display    = ['award_title', 'for_award', 'award_year', 'award_date', 'status',]
    search_fields   = ['award_title', 'for_award', 'award_year', 'award_date', 'status',]
    list_filter     = ['award_title','status',]

class MyEducationAdmin(admin.ModelAdmin):
    list_display    = ['name_of_degree', 'passing_year', 'CGPA', 'board', 'status',]
    search_fields   = ['name_of_degree', 'passing_year', 'CGPA', 'board', 'status',]
    list_filter     = ['name_of_degree','status',]


class MyProgramAdmin(admin.ModelAdmin):
    list_display    = ['program_title', 'program_place', 'program_date', 'status',]
    search_fields   = ['program_title', 'program_place', 'program_date', 'status',]
    list_filter     = ['program_title', 'status',]

class AcademicQualificationAdmin(admin.ModelAdmin):
    list_display    = ['education_label', 'institute_name', 'group', 'board', 'passing_year', 'status',]
    search_fields   = ['education_label', 'institute_name', 'group', 'status',]
    list_filter     = ['education_label', 'status',]

class ExperienceAdmin(admin.ModelAdmin):
    list_display    = ['course_name', 'awording_body', 'duration', 'country', 'status',]
    search_fields   = ['course_name', 'awording_body', 'duration', 'status',]
    list_filter     = ['course_name', 'status',]


class SocialActivitiesAdmin(admin.ModelAdmin):
    list_display    = ['title', 'place', 'country', 'country', 'status',]
    search_fields   = ['title', 'place', 'country', 'status',]
    list_filter     = ['title', 'status',]


admin.site.register(models.OperationCatagory, OperationCatagoryAdmin)
admin.site.register(models.GalleryCatagory, GalleryCatagoryAdmin)
admin.site.register(models.SliderInfo, SliderInfoAdmin)
admin.site.register(models.PersonalProfile, PersonalProfileAdmin)
admin.site.register(models.GalleryInfo, GalleryInfoAdmin)
admin.site.register(models.OperationPost, OperationPostAdmin)
admin.site.register(models.MyAward, MyAwardAdmin)
admin.site.register(models.MyEducation, MyEducationAdmin)
admin.site.register(models.MyProgram, MyProgramAdmin)
admin.site.register(models.AcademicQualification, AcademicQualificationAdmin)
admin.site.register(models.Experience, ExperienceAdmin)
admin.site.register(models.SocialActivities, SocialActivitiesAdmin)