from random import randint
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import viewsets
# from rest_framework.parsers import JSONparser
from rest_framework.decorators import api_view
from django.core.mail import send_mail

# Create your views here.
from .models import Admin,Department,Degreeprogram,Semester,Subject,Faculty,TimetableData
from .serializers import AdminSerializer,DeptSerializer,DegpgmSerializer,SemSerializer,SubSerializer,FacSerializer,TimetableDataSerializer
from .import models

# admin--view
class adminview(viewsets.ModelViewSet):
    queryset= Admin.objects.all()
    serializer_class=AdminSerializer

# department--view
@api_view(['GET'])
def deptOverview(request):
    api_urls={
        'List':'/dept-list/',
        'Create':'/dept-create/',
        'Update':'/dept-Update/',
        'Delete':'/dept-delete/',
    }
    return Response(api_urls)
@api_view(['GET'])
def showalldep(request):
    admins=Department.objects.all()
    serializer=DeptSerializer(admins,many=True)
    return Response(serializer.data)

# degree-progamme -- view
@api_view(['GET'])
def degpgmOverview(request):
    api_urls={
        'List':'/degpgm-list/',
        'Create':'/degpgm-create/',
        'Update':'/degpgm-Update/',
        'Delete':'/degpgm-delete/',
    }
    return Response(api_urls)
@api_view(['GET'])
def showalldegpgm(request):
    admins=Degreeprogram.objects.all()
    serializer=DegpgmSerializer(admins,many=True)
    return Response(serializer.data)

#sem view
@api_view(['GET'])
def SemesterOverview(request):
    api_urls={
        'List':'Semester-list/',
        'Create':'/Semester-create/',
        'Update':'/Semester-Update/',
        'Delete':'/Semester-delete/',
    }
    return Response(api_urls)
@api_view(['GET'])
def showallsem(request):
    admins=Semester.objects.all()
    serializer=SemSerializer(admins,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def SubjectOverview(request):
    api_urls={
        'List':'Subject-list/',
        'Create':'/Subject-create/',
        'Update':'/Subject-Update/',
        'Delete':'/Subject-delete/',
    }
    return Response(api_urls)
@api_view(['GET'])
def showallsub(request):
    admins=Subject.objects.all()
    serializer=SubSerializer(admins,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def FacultyOverview(request):
    api_urls={
        'List':'Faculty-list/',
        'Create':'/Faculty-create/',
        'Update':'/Faculty-Update/',
        'Delete':'/Faculty-delete/',
    }
    return Response(api_urls)

@api_view(['GET'])
def showallsub(request):
    admins=Faculty.objects.all()
    serializer=FacSerializer(admins,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Overllview(request):
    api_urls={
        'List':'overall-list/',
        'Create':'/overall-create/',
        'Update':'/overall-Update/',
        'Delete':'/overall-delete/',
    }
    return Response(api_urls)

@api_view(['GET'])
def overallshow(request):
    admins=TimetableData.objects.all()
    serializer=TimetableDataSerializer(admins,many=True)
    return Response(serializer.data)

@csrf_exempt
def forgetpass(request):
    email=request.POST.get("email")
    verify=models.Admin.objects.filter(email=email).first()
    if verify:
        # otp_digit=randint(100000,999999)
        link=f"http://localhost:3000/For_pass/{verify.id}/"
        send_mail(
            'Verify Account',
            'please verify account',
            'pranovvimal30@gmail.com',
            [email],
            fail_silently=False,
            html_message=f'<p>Your OTP is</p><p>{link}</p>'
        )
        return JsonResponse({'bool':True,'msg':'OTP sent to your mail'})
    else:
        return JsonResponse({'bool':False,'msg':'Invalid Email!!'})
        # models.Admin.objects.filter(email=email).update(otp_digit=otp_digit)
    

# @csrf_exempt
# @api_view(['POST'])
# def Admincreate(request):
#     serializer = AdminSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return JsonResponse(serializer.data)


# def Fac_login(request):
#     Facultyid = request.POST['Facultyid']
#     Email  = request.POST['Email']
#     Password = request.POST['Password']
#     data = Admin.objects.get(Facultyid=Facultyid,email=Email,password=Password)
#     if data:
#         return JsonResponse({'bool':True})
#     else:
#         return JsonResponse({'bool':False})
        
# def Fac_login(request):
#     form = Admin()
#     if request.method == 'POST':
#         form = Admin(request.POST)
#         # if form:
#         #     # return JsonResponse({'bool':True})
#         #     return http
#         # else:
#         return HttpResponse(form.data) 
            
            