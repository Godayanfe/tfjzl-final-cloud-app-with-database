from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    # Home page - list all courses
    path('', views.index, name='index'),

    # Auth
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),

    # Course
    path('course/<int:course_id>/', views.course_details, name='course_details'),
    path('enroll/<int:course_id>/', views.enroll, name='enroll'),

    # Exam
    path('<int:course_id>/submit/', views.submit, name='submit'),
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='exam_result'),
]
