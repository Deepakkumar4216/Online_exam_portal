from django.db import models

# Create your models here.

class Registeration(models.Model):
    Name = models.CharField(max_length=30)
    F_Name = models.CharField(max_length=30)
    M_Name = models.CharField(max_length=30)
    DOB = models.DateField()
    Gender = models.CharField(max_length=5)
    Contact = models.IntegerField(max_length=10)
    mc = models.CharField(max_length=50)
    mp = models.CharField(max_length=8)
    my = models.CharField(max_length=5)
    ic = models.CharField(max_length=50)
    ip = models.CharField(max_length=8)
    iy = models.CharField(max_length=5)
    gc = models.CharField(max_length=50)
    gp = models.CharField(max_length=8)
    gy = models.CharField(max_length=5)
    oc = models.CharField(max_length=50)
    op = models.CharField(max_length=8)
    oy = models.CharField(max_length=5)
    Email = models.EmailField(max_length=30)
    Password = models.CharField(max_length=20)
    C_Password = models.CharField(max_length=20)

    def __str__(self):
        return self.Name


class Question(models.Model):
    Ques = models.TextField()
    Ans1 = models.TextField()
    Ans2 = models.TextField()
    Ans3 = models.TextField()
    Ans4 = models.TextField()
    RightAns = models.IntegerField()
    RightAnsTxt = models.TextField(default="")
    StudentAns = models.IntegerField(default=0)

    def __str__(self):
        return self.Ques
class Time(models.Model):
    duration=models.IntegerField()

    def __str__(self):
        n = self.duration
        s = str(n)
        return s


# class UserAns(models.Model):
#     Username = models.CharField(max_length=30)
#     Email = models.EmailField(max_length=30)
#     Ans1 = models.IntegerField()
#     Ans2 = models.IntegerField()
#     Ans3 = models.IntegerField()
#     Ans4 = models.IntegerField()
#     Ans5 = models.IntegerField()
#     Ans6 = models.IntegerField()
#     Ans7 = models.IntegerField()
#     Ans8 = models.IntegerField()
#     Ans9 = models.IntegerField()
#     Ans10 = models.IntegerField()
        