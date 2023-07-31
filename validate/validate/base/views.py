from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .models import Certificate
from django.http import HttpResponse


# Create your views here.
def validate(request):
    if request.method == 'POST':
        c_id = request.POST.get('certificateId')
        try:
            certificate = Certificate.objects.get(c_id=c_id)
            # Certificate ID exists in the database, perform your validation logic here
            # For example, you could return a success message:
            messages.info(request,'valid certificate')
            return redirect('')
        except Certificate.DoesNotExist:
            # Certificate ID does not exist in the database
            messages.info(request,'no certificate')
            return redirect('')
    return render(request, 'validate.html')