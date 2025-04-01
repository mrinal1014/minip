from django.shortcuts import render, redirect
from .models import Student
from django.http import JsonResponse
from django.shortcuts import render
from .models import Student

from django.shortcuts import render
from django.http import JsonResponse
from .models import Student

from django.http import JsonResponse
from django.shortcuts import render
from .models import Student

def chatbot_page(request):
    return render(request, "students/chatbot.html")

def search_api(request):
    query = request.GET.get('q', '')
    students = Student.objects.filter(registration_number__icontains=query) if query else []
    results = [{'name': s.name, 'program': s.program, 'department': s.department} for s in students]
    return JsonResponse(results, safe=False)



from django.shortcuts import render
def home(request):
    """Render the home page with project details."""
    return render(request, 'students/home.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        roll_number = request.POST['roll_number']
        registration_number = request.POST['registration_number']
        year_of_study = request.POST['year_of_study']
        section = request.POST['section']
        program = request.POST['program']
        department = request.POST['department']
        school = request.POST['school']

        Student.objects.create(
            name=name,
            age=age,
            email=email,
            roll_number=roll_number,
            registration_number=registration_number,
            year_of_study=year_of_study,
            section=section,
            program=program,
            department=department,
            school=school
        )
        return redirect('student_list')
    return render(request, 'students/add_student.html')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def student_search_by_registration(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            reg_number = data.get("query", "").strip()
            student = Student.objects.filter(registration_number=reg_number).first()
            if student:
                response_text = f"Name: {student.name}, Reg No: {student.registration_number}, Program: {student.program}, Department: {student.department}"
            else:
                response_text = "No student found with this registration number."
            return JsonResponse({"response": response_text})
        except Exception as e:
            return JsonResponse({"response": "Error processing request."}, status=500)
    return JsonResponse({"response": "Invalid request."}, status=400)
