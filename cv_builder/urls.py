from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_form_view, name='home'),
    path('choose/<int:resume_id>/', views.choose_template, name='choose_template'),
    path('download-pdf/<int:resume_id>/<int:template_id>/', views.generate_pdf_view, name='generate_pdf'),
    path('download-doc/<int:resume_id>/<int:template_id>/', views.generate_doc_view, name='generate_doc'),
]
