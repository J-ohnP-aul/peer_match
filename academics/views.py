from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import ( Course, StudentAcademicProfile, StudentUnit)
from .forms import AcademicProfileF, StudentUnitForm

# Create your views here.

@login_required
def academic_profile_v(request):
  if request.method == "POST":
    form = AcademicProfileF(request.POST)
    
    if form.is_valid():
      reg_no = form.cleaned_data("reg_no").strip().upper()
      
      # get reg
      parts  = reg_no.split("/")
      if len(parts) != 3:
        form.add_error("reg_no", "Enter a valid Registration Number")
      else:
        reg_prefix = parts[0]
        year = parts[2]
        
        try:
          course = Course.objects.get(reg_prefix=reg_prefix)
        except Course.DoesNotExist:
          form.add_error("reg_no", "Reg no could not be verified")
        else:
          StudentAcademicProfile.objects.update_or_create(
            student = request.user,
            defaults={
              "reg_no": reg_no,
              "course": course,
              "year_joined": 2000 + int(year)
            }
          )
          return redirect("academic_profile_success")
  else:
    form = AcademicProfileF()
  return render(request, "academics/academic_profile.html", {"form":form})
      
@login_required
def select_units_v(request):
  profile = get_object_or_404(StudentAcademicProfile, student=request.user)
  if request.method == "POST":
    form = StudentUnitForm(request.POST)
    form.fields["units"].queryset = profile.course.units.all() #allow units belonging to std course
    if form.is_valid():
      StudentUnit.objects.filter(student=request.user).tiodelete() #remove previouse slec
      # save nw selection
      for unit in form.cleaned_data["units"]:
        StudentUnit.objects.create(
          student=request.user,
          unit=unit
        )
      return redirect("academic_profile_success")
  else:
      form = StudentUnitForm()
      form.fields["units"].queryset = profile.course.units.all()
  return render(
      request,
      "academics/select_units.html",
      {
          "form": form,
          "profile": profile,
      }
  )

@login_required
def academic_profile_success_v(request):
    profile = get_object_or_404(StudentAcademicProfile,student=request.user)
    units = StudentUnit.objects.filter(
        student=request.user
    ).select_related("unit")
    return render(
        request,
        "academics/academic_profile_success.html",
        {
            "profile": profile,
            "units": units,
        }
    )