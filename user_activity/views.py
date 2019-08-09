from django.shortcuts import render
from . models import UploadForm,Upload
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.




# Create your views here.
@login_required
@permission_required('user_activity.can_upload_files', raise_exception=True)
def upload_data(request):
    if request.method=="POST":
        img = UploadForm(request.POST, request.FILES)       
        if img.is_valid():
            img.save()  
            messages.info(request, 'file uploaded successfully')
            return HttpResponseRedirect(reverse('user_activity:upload'))
    else:

        img=UploadForm()
    images=Upload.objects.all()
    return render(request,'user_activity/upload_files.html',{'form':img,'images':images})