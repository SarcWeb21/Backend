from django.shortcuts import render
from pmpportal.models import Registration


def mentors(request):
    allmentors = Registration.objects.all()
    context = {'mentors': allmentors}
    return render(request, 'mentorcards.html', context)
