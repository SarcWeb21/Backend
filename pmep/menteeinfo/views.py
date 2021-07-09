from django.shortcuts import render
from django.http import HttpResponse
from .models import Mentee, Mentor, temp
# Create your views here.
def index(request):
	return render(request, 'menteeinfo/index.html')

# Mentee registration
def register(request):
	corementors = Mentor.objects.filter(field="Core")
	consultmentors = Mentor.objects.filter(field="Consultancy")
	analyticmentors = Mentor.objects.filter(field="Analytics")
	finmentors = Mentor.objects.filter(field="Finance")
	csmentor = Mentor.objects.filter(field="IT/Software")
	othermentors = Mentor.objects.filter(field="Other")
    # allmentors_sorted = allmentors.order_by['gray_out']
	context = {
		'mentors_list_core': corementors, 
		'mentors_list_consult': consultmentors,
		'mentors_list_analysis': analyticmentors,
		'mentors_list_fin': finmentors,
		'mentors_list_cs': csmentor,
		'mentors_list_other': othermentors
	}
	return render(request, "menteeinfo/register.html", context)
# def mentorexp(request):
#     allmentors = Mentor.objects.all()
# 	for mentor in allmentors:
#     	exp = mentor.experience


def menteereg(request):
	if request.method == 'POST':
        # full_name = request.POST.get('full_name')
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
		full_name = request.POST.get('roll_no')
		

		SOP = request.POST.get('SOP')
		mentee = Mentee(full_name = full_name, roll_no = roll_no,
			department = department, graduation_year = graduation_year,
			contact_number = contact_number, email_id = email_id,
			preference_1 = preference_1, preference_2 = preference_2,
			preference_3 = preference_3, preference_4 = preference_4, 
			preference_5 = preference_5, SOP = SOP)
		mentee.save()
	return render(request, 'menteeinfo/register_success.html')