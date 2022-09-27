from django.urls import path
from . import views
urlpatterns = [
    path('', views.index_page),
    path('profile', views.profile_page),
    path('gallery/<int:id>/view-photo', views.gallery_page),
    path('education', views.education_page),
    path('what-do/<int:id>/category', views.category_page),
    path('operation/view/<int:id>/details/', views.operation_view_details),
    path('program/all-program/', views.all_program),
    path('program/<int:id>/view-program/', views.program_view_details),
    path('achievment/all-achievment/', views.all_achievment),
    path('social-activities/', views.social_activities),
]
