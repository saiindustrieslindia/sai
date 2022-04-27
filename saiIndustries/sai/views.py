from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = ' *** '+request.POST['subject']
        message = request.POST['message']
        #send an email
        send_mail(
            name+'-'+subject, # subject
            message, #message
            email, #from email
            ['saiindustrieslindia@gmail.com', 'ravishankarbhure@saiindustriesorg.com']
        )
        return render(request, 'home.html', {'name': name})
    else:
        return render(request, 'home.html', {})
