from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse
from create.models import Certificate
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
import pdfkit
# path_wkhtmltopdf = b'C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe'
# config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        date = request.POST['date']
        sign = request.POST['sign']
        details = request.POST['details']
        # user = User.objects.create_user(name=name, date = date, sign= sign, details=details)
        obj = Certificate.objects.create(name=name,date=date,sign=sign,details=details)
        obj.save() 
        return redirect(reverse('print'))          
    else:
        return render(request,"index.html")
    

def certificate(request):
    return render(request,'certificate.html')


def Print(request):
    posts = Certificate.objects.latest('id')
    return render(request, 'certificate_template.html', {'posts': posts})

def generate_pdf(request):
    posts = Certificate.objects.latest('id')
    template_path = 'certificate_template.html'
    context = {'posts':posts}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] ='filename="sample.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse("error")
    return response
# def generate_pdf(request):

#     posts = Certificate.objects.latest('id')
    
#     # Load the HTML template
#     template = get_template('certificate_template.html')
    
#     # Render the HTML template with the certificate data
#     html_content = template.render({'posts': posts})
#     pdf = pdfkit.from_string(html_content, "file.pdf")
#     if pdf:
#         # Provide the PDF as a downloadable file
#         response = HttpResponse(pdf, content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
#         return response
#     else:
#         # Handle the case when PDF generation fails
#         return HttpResponse("Error while generating PDF.", status=500)