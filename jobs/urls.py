from django.urls import path, include 
from . import views
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, LocationViewSet, JobViewSet, ApplicantViewSet

# Setup DRF router
router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'applicants', ApplicantViewSet)

urlpatterns = [
    # Web (HTML) views
    path('', views.job_list, name='job_list'),
    path('<int:job_id>/', views.job_detail, name='job_detail'),

    # REST API routes
    path('api/', include(router.urls)),
]