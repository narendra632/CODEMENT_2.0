from django.shortcuts import render, get_object_or_404

from django.contrib import messages

from .models import Contact, Hackathon, Tool, Channel

from django.core.mail import send_mail


def index(request):
    channels = Channel.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = ""
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, "Message received! I'll get back to you soon😊")

        # send an email to yourself
        send_mail(
            subject,
            f"Name: {name}\nEmail: {email}\nMessage: {message}",
            email,
            ['codement13@gmail.com'], # your email address
            fail_silently=True,
        )
    return render(request, "index.html", {'channels': channels})


def codement_20(request):
    hackathons = Hackathon.objects.all()
    tools = Tool.objects.all()

    return render(request,"codement_20.html",{'hackathons': hackathons, 'tools': tools}) 




  

