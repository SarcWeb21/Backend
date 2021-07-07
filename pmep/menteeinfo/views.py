
from django.shortcuts import render
from django.http import HttpResponse
from .models import Mentee, Mentor, temp
# Create your views here.
def index(request):
	return render(request, 'menteeinfo/index.html')

#Mentee registration
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
		# for l in range(1,6):
		# 	mentor = Mentor.objects.filter(id = '("preference"+str(l))')
		# 	if(mentor.hits>=3*mentor.no_of_mentees):
		# 		mentor.gray_out = 0
		# 		return HttpResponse("Your preference_"+str(l)+ " is not available")
		# 	else:
		# 		mentor.hits = mentor.hits+1


		SOP = request.POST.get('SOP')
		mentee = Mentee(full_name = full_name, roll_no = roll_no,
			department = department, graduation_year = graduation_year,
			contact_number = contact_number, email_id = email_id,
			preference_1 = preference_1, preference_2 = preference_2,
			preference_3 = preference_3, preference_4 = preference_4, 
			preference_5 = preference_5, SOP = SOP)
		mentee.save()
	return render(request, "menteeinfo/register.html", context)

#sorted mentor display
# def corementors(request):
#     allmentors = Mentor.objects.filter(field="Core")
#     # allmentors_sorted = allmentors.order_by['gray_out']
#     return render(request, 'menteeinfo/register.html', {'mentors_list_core': allmentors})

# def analyticsmentors(request):
#     allmentors = Mentor.objects.filter(field="Analytics")
#     # allmentors_sorted = allmentors.order_by['gray_out']
#     return render(request, 'menteeinfo/register.html', {'mentors_list_analytics': allmentors})

# def financementors(request):
#     allmentors = Mentor.objects.filter(field="Finance")
#     # allmentors_sorted = allmentors.order_by['gray_out']
#     return render(request, 'menteeinfo/register.html', {'mentors_list_finance': allmentors})

# def csmentors(request):
#     allmentors = Mentor.objects.filter(field="IT/Software")
#     # allmentors_sorted = allmentors.order_by['gray_out']
#     return render(request, 'menteeinfo/register.html', {'mentors_list_cs': allmentors})

# def othermentors(request):
#     allmentors = Mentor.objects.filter(field="Others")
#     # allmentors_sorted = allmentors.order_by['gray_out']
#     return render(request, 'menteeinfo/register.html', {'mentors_list_other': allmentors})


#temporary
# def trmpe(request):
# 	if request.method == 'POST':
# 		preference_1 = request.POST.get('preference_1')
# 		preference_2 = request.POST.get('preference_2')
# 		preference_3 = request.POST.get('preference_3')
# 		preference_4 = request.POST.get('preference_4')
# 		preference_5 = request.POST.get('preference_5')
# 		assign = temp(preference_1=preference_1, preference_2=preference_2, preference_3=preference_3, preference_4=preference_4, preference_5=preference_5)
# 		assign.save()
# 	return HttpResponse('Done')