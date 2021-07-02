from django.shortcuts import render
from django.http import HttpResponse
from pmpportal.models import Registration

# Create your views here.
def index(request):
    return render(request,'index.html')

def step1(request):
    return render(request, 'step-one.html')

def savedata(request):
    if request.method == 'POST':
        full_name=request.POST.get('name')
        rollno=request.POST.get('rollno')
        department=request.POST.get('department')
        degree=request.POST.get('degree')
        # degree_other=request.POST.get('degree_other')
        graduation_year=request.POST.get('graduation_year')
        designation=request.POST.get('designation')
        experience=request.POST.get('experience')
        contact=request.POST.get('contact')
        mail=request.POST.get('email')
        # field_mentorship=request.POST.get('')

        analytics=request.POST.get('analytics')
        consultancy=request.POST.get('consultancy')
        finance=request.POST.get('finance')
        FMCG=request.POST.get('FMCG')
        software=request.POST.get('software')
        core=request.POST.get('core')
        other_mentorship=request.POST.get('other_mentorship')

        no_of_mentees=request.POST.get('no_of_mentees')
        referral=request.POST.get('referral')
        suggestions=request.POST.get('suggestion')

        registration=Registration(full_name=full_name, rollno=rollno, department=department, degree=degree,graduation_year=graduation_year, designation=designation, experience=experience, contact=contact,  mail=mail, analytics=analytics,  consultancy=consultancy, finance=finance , FMCG=FMCG, software=software, core=core, other_mentorship=other_mentorship , no_of_mentees=no_of_mentees, referral=referral,  suggestions=suggestions)
        registration.save()
    return HttpResponse('Eh')
