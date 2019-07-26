from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Registeration, Question
from django.db.models import Q

def index(request):
    if request.session.get('name') is not None:
        return render(request,'study/instruction.html')
    return render(request,'study/home.html')


def register(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            f_name = request.POST['fname']
            m_name = request.POST['mname']
            dob = request.POST['dob']
            rad = request.POST['rad']
            contact = request.POST['mob']
            Mc = request.POST['mc']
            Mp = request.POST['mp']
            My = request.POST['my']
            ic = request.POST['ic']            
            ip = request.POST['ip']
            iy = request.POST['iy']
            gc = request.POST['gc']
            gp = request.POST['gp']
            gy = request.POST['gy']
            oc = request.POST['oc']
            op = request.POST['op']
            oy = request.POST['oy']
            email = request.POST['email']
            password = request.POST['password']
            c_password = request.POST['c_password']

            obj = Registeration(
                Name = name,
                F_Name = f_name,
                M_Name = m_name,
                DOB = dob,
                Gender = rad,
                Contact = contact,
                mc = Mc,
                mp = Mp,
                my = My,
                ic = ic,
                ip = ip,
                iy = iy,
                gc = gc,
                gp = gp,
                gy = gy,
                oc = oc,
                op = op,
                oy = oy,
                Email = email,
                Password = password,
                C_Password = c_password
            )
            obj.save()
            return render(request,'study/Login.html')
        else:
            return render(request,'study/register.html')
    except Exception as e:
        return HttpResponse(e)


def about(request):
    return render(request,'study/about.html')


def forget(request):
    if request.session.get('name') is not None:
        return render(request,'study/instruction.html')
    try:
        if request.method == 'POST':
            user_id = request.POST['user_id']
            if user_id == "":
                param = {'label_name':"userid",'userid':"Please enter your Email_id"}
                return render(request,'study/forget.html',param)
            obj = Registeration.objects.filter(Q(Email = user_id)).first()
            if obj==None:
                param = {'label_name':"userid",'userid':"Please enter a valid Email_id"}
                return render(request,'study/forget.html',param)
            pswd = obj.Password
            param = {'label_name':"Your password is",'userid':pswd,'status':"hidden",'text_box_status':"disabled"}
            return render(request,'study/forget.html',param)
        param = {'label_name':"userid",'userid':"Enter your Email_id"}
        return render(request,'study/forget.html',param)

    except Exception as e:
        return HttpResponse(e)


def instruction(request):
    if request.session.get('name') is None:
        return render(request,'study/login.html')
    try:
        if request.method == 'POST':
            val = request.POST['btn']
            if val == "Start_Test":
                ob = Question.objects.all()
                return render(request,'study/ques.html', {'ob': ob})
            if val == "Logout":
                del request.session['name']
                return render(request,'study/home.html')
        else:
            return render(request,'study/instruction.html')
    except Exception as e:
        return HttpResponse(e)        

    


def login(request):

    if request.session.get('name') is not None:
        return render(request,'study/instruction.html')

    if request.method == 'POST':
        try:
            btn = request.POST['llgn']
            if btn == "signup":
                return render(request,'study/register.html')
            if btn == "signin":
                Email_id = request.POST['email']
                pswd = request.POST['password']
                if Email_id == "" or pswd == "":
                    return HttpResponse("Please enter all the fields")
                obj = Registeration.objects.filter(Q(Email = Email_id)).first()
                if obj == None:
                    return HttpResponse("User does not exist. Please enter a valid user_id")
                request.session['name'] = Email_id
                return render(request,'study/instruction.html')
        except Exception as e:
            return HttpResponse(e)

    return render(request,'study/login.html')


def ques(request):
    if request.session.get('name') is None:
        return render(request,'study/login.html')
    try:
        if request.method == 'POST':
            arr = [request.POST["quizcheck[1]"],request.POST["quizcheck[2]"],request.POST["quizcheck[3]"],request.POST["quizcheck[4]"],request.POST["quizcheck[5]"],request.POST["quizcheck[6]"],request.POST["quizcheck[7]"],request.POST["quizcheck[8]"],request.POST["quizcheck[9]"],request.POST["quizcheck[10]"]]
            for i in range(len(arr)):
                ob = Question.objects.get(id=i+1)
                ob.StudentAns=arr[i]
                ob.save()
            obj = Question.objects.all()

            i = 0
            rightans = 0
            wrongans = 0
            for ob in obj:
                if ob.RightAns == (int)(arr[i]):
                    rightans += 1
                elif ob.RightAns != (int)(arr[i]) and (int)(arr[i])!=0:
                    wrongans += 1
                i += 1
            attempt = rightans+wrongans
            session_name = request.session.get('name')
            user = Registeration.objects.get(Q(Email = session_name))
            username = user.Name
            param = {'username':username,'arr':arr,'attempt':attempt,'correct':rightans,'wrong':wrongans,'finalresult':rightans}
            return render(request,'study/result.html',param)
        return render(request,'study/instruction.html')
    except Exception as e:
        return HttpResponse(e)


def result(request):
    if request.session.get('name') is None:
        return render(request,'study/login.html')
    try:
        if request.method == 'POST':
            btn = request.POST['btn']
            arr = request.POST['arr_textbox']
            if btn == "review":
                obj = Question.objects.all()
                return render(request,'study/review.html',{'obj':obj,'arr':arr})
            if btn == "Logout":
                session_name = request.session.get('name')
                user = Registeration.objects.get(Q(Email = session_name))
                username = user.Name
                param = {'username':username}
                del request.session['name']
                return render(request,'study/thank.html',param)
        return render(request,'study/instruction.html')
    except Exception as e:
        return HttpResponse(e)


def thank(request):
    return render(request,'study/thank.html')

def Review(request):
    if request.session.get('name') is None:
        return render(request,'study/login.html')
    if request.method=='POST':
        return render(request,'study/review.html')
    return render(request,'study/instruction.html')