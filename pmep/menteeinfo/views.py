from django.shortcuts import render
from django.http import HttpResponse
from .models import Mentee
# Create your views here.
def index(request):
	return HttpResponse('hi')

def register(request):
	if request.method == 'POST':
		full_name = request.POST.get('full_name')
		roll_no = request.POST.get('roll_no')
		department = request.POST.get('department')
		graduation_year = request.POST.get('graduation_year')
		contact_number = request.POST.get('contact_number')
		email_id = request.POST.get('email_id')
		preference_1 = request.POST.get('preference_1')
		preference_2 = request.POST.get('preference_2')
		preference_3 = request.POST.get('preference_3')
