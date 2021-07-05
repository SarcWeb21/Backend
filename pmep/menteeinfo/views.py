from django.shortcuts import render
from django.http import HttpResponse
from .models import Mentee, Mentor, temp
# Create your views here.
def index(request):
	return render(request, 'menteeinfo/index.html')
#Mentee registration
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
		preference_4 = request.POST.get('preference_4')
		preference_5 = request.POST.get('preference_5')
		#for grayout
		for l in range(1,6):
			mentor = Mentor.objects.filter(id = '("preference"+str(l))')
			if(mentor.hits>=3*mentor.no_of_mentees):
				mentor.gray_out = 0
				return HttpResponse("Your preference_"+str(l)+ " is not available")
			else:
				mentor.hits = mentor.hits+1


		SOPs = request.POST.get('SOP')
		mentee = Mentee(full_name = full_name, roll_no = roll_no,
			department = department, graduation_year = graduation_year,
			contact_number = contact_number, email_id = email_id,
			preference_1 = preference_1, preference_2 = preference_2,
			preference_3 = preference_3, preference_4 = preference_4, 
			preference_5 = preference_5, SOP = SOPs)
		mentee.save()
	return render(request, "menteeinfo/register.html")

#sorted mentor display
def mentors(request):
    # allmentors = Mentor.objects.all()
    # allmentors_sorted = allmentors.order_by['gray_out']
    return render(request, 'menteeinfo/mentorcards.html')

#temporary
def trmpe(request):
	if request.method == 'POST':
		preference_1 = request.POST.get('preference_1')
		preference_2 = request.POST.get('preference_2')
		preference_3 = request.POST.get('preference_3')
		preference_4 = request.POST.get('preference_4')
		preference_5 = request.POST.get('preference_5')
		assign = temp(preference_1=preference_1, preference_2=preference_2, preference_3=preference_3, preference_4=preference_4, preference_5=preference_5)
		assign.save()
	return HttpResponse('Done')