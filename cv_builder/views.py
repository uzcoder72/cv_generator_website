from django.shortcuts import render, redirect
from .forms import ResumeForm
from .models import Resume
from django.shortcuts import get_object_or_404
from .pdf_generator import create_pdf_response
from .doc_generator import create_doc_response

def cv_form_view(request):
    if request.method == 'POST':
        # request.FILES is required because we are uploading a photo!
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save()
            # After saving, send the user to choose their template (We build this in Lesson 4)
            return redirect('choose_template', resume_id=resume.id)
    else:
        form = ResumeForm()
        
    return render(request, 'cv_builder/index.html', {'form': form})

# Placeholder for lesson 4
def choose_template(request, resume_id):
    return render(request, 'cv_builder/choose.html', {'resume_id': resume_id})

def generate_pdf_view(request, resume_id, template_id):
    resume = get_object_or_404(Resume, id=resume_id)
    return create_pdf_response(resume, template_id)
def generate_doc_view(request, resume_id, template_id):
    resume = get_object_or_404(Resume, id=resume_id)
    return create_doc_response(resume, template_id)