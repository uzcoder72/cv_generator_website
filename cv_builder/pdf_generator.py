from xhtml2pdf import pisa
from django.template.loader import render_to_string
from django.http import HttpResponse
from io import BytesIO

def create_pdf_response(resume, template_id):
    # Pick the right HTML template
    template_name = f'cv_builder/template{template_id}.html'
    
    # Render the HTML with our database data
    html_string = render_to_string(template_name, {'resume': resume})
    
    # Prepare the browser to receive a PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{resume.name}_{resume.surname}_CV.pdf"'
    
    # Generate the PDF and inject it into the response!
    pisa_status = pisa.CreatePDF(
       BytesIO(html_string.encode('utf-8')), dest=response
    )
    
    # Return it to the user
    return response
