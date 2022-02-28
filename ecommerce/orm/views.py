from django.shortcuts import render
from .models import Student


def studentData(request):

    students = Student.objects.all().values()
    
    students1 = Student.objects.filter(student_name__startswith='H').values()
    students2 = Student.objects.filter(student_name__contains='R').values()
    #students3 = Student.objects.filter(role_id__gte=1).values()
    
    print("filter",students2)
    print(students[0].get('id'))
    print(students[0])
    studentlist =[]

    for i in students1[0].values():
        studentlist.append(i)

    print("student list =",studentlist)




     #for student in students:
     #   print(student.keys(),end= '')
      #  print(student.items())


    context = {
        'students':studentlist
    }
    return render(request,'orm/student.html',context)
