from django.shortcuts import render
from . import models
# Create your views here.
def index_page(request):
    profile     = models.PersonalProfile.objects.all().last()
    slider_list = models.SliderInfo.objects.all().order_by("slider_order")[:10]
    category_list = models.OperationCatagory.objects.all().order_by("sequence")[:8]
    program_list = models.MyProgram.objects.filter(status = True).order_by("id").reverse()
    context = {
        'profile': profile,
        'slider_list': slider_list,
        'category_list': category_list,
        'program_list': program_list,
        'gallery_category': models.GalleryCatagory.objects.all().order_by("sequence"),
    }
    return render(request, 'doctor/index.html', context)

def category_page(request,id): 
    get_cat_id = models.OperationCatagory.objects.get(id=id)
    operation_list = models.OperationPost.objects.filter(operation_category_id = id)
    
    context = {
        'get_cat_id':get_cat_id,
        'operation_list':operation_list,
        'gallery_category': models.GalleryCatagory.objects.all().order_by("sequence"),
    }
    return render(request, 'doctor/category_page.html', context)

def profile_page(request): 
    profile         = models.PersonalProfile.objects.all().first()
    academic_info   = models.AcademicQualification.objects.all()
    experience   = models.Experience.objects.all()
    
    context = {
        'profile':profile,
        'academic_info':academic_info,
        'experience':experience,
        'gallery_category': models.GalleryCatagory.objects.all().order_by("sequence"),
    }
    return render(request, 'doctor/profile.html', context)

def gallery_page(request,id): 
    get_cat_id     = models.GalleryCatagory.objects.get(id = id)
    gallery_list   = models.GalleryInfo.objects.filter(gallery_category = id)
    
    context = {
        'get_cat_id':get_cat_id,
        'gallery_list':gallery_list,
        'gallery_category': models.GalleryCatagory.objects.all().order_by("sequence"),
    }
    return render(request, 'doctor/gallery.html', context)

def education_page(request): 
    education     = models.MyEducation.objects.all()
    
    context = {
        'education':education,
        'gallery_category': models.GalleryCatagory.objects.all().order_by("sequence"),
    }
    return render(request, 'doctor/education.html', context)

def operation_view_details(request,id): 
    get_operation  = models.OperationPost.objects.get(id=id)
    
    context = {
        'get_operation':get_operation,
        'gallery_category': models.GalleryCatagory.objects.all().order_by("sequence"),
    }
    return render(request, 'doctor/operation_view_details.html', context)

def all_achievment(request): 
    award_list = models.MyAward.objects.all().order_by("id").reverse()
    context = {
        'award_list':award_list,
        'gallery_category': models.GalleryCatagory.objects.all().order_by("sequence"),
    }
    return render(request, 'doctor/all_achievment.html', context)
 

def all_program(request): 
    program_list = models.MyProgram.objects.filter(status = True).order_by("id").reverse()
    context = {
        'program_list':program_list,
        'gallery_category': models.GalleryCatagory.objects.all().order_by("sequence"),
    }
    return render(request, 'doctor/all_program.html', context)


def program_view_details(request,id): 
    program  = models.MyProgram.objects.get(id=id)
    context = {
        'program':program,
        'gallery_category': models.GalleryCatagory.objects.all().order_by("sequence"),
    }
    return render(request, 'doctor/program_view_details.html', context)

def social_activities(request): 
    activities  = models.SocialActivities.objects.all().order_by("id").reverse()
    context = {
        'activities':activities,
        'gallery_category': models.GalleryCatagory.objects.all().order_by("sequence"),
    }
    return render(request, 'doctor/social_activities.html', context)