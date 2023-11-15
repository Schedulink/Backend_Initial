from django.db import models

# Create your models here.

class  Admin(models.Model):
    Facultyid = models.AutoField(primary_key=True)
    Password = models.CharField(max_length=50)
    Email = models.EmailField()
    def __str__(self):
        return self.Password
     
class Department(models.Model):
    Dept_name=models.CharField(blank=False,max_length=40,primary_key=True)
    Facultyid = models.IntegerField(blank=False)
    room_no=models.CharField(blank=False,max_length=40)
    def __str__(self):
        return self.Dept_name

class Degreeprogram(models.Model):
      managed = True
      Dept_name=models.ForeignKey(Department,on_delete=models.CASCADE)
      Deg_name=models.CharField(primary_key=True,max_length=40,blank=False)
      def __str__(self) :
          return self.Deg_name

class Semester(models.Model):
    sem_id=models.CharField(max_length=10,blank=False)
    sem_num=models.IntegerField(blank=False)
    Deg_name=models.ForeignKey(Degreeprogram,on_delete=models.CASCADE)
    Reg_year=models.CharField(max_length=50)
   
    def __str__(self) :
         return f'{self.Reg_year},{self.sem_id}'
         
          


class Subject(models.Model):
    sem_id=models.ForeignKey(Semester,on_delete=models.CASCADE)
    Sub_code=models.CharField(max_length=20,blank=False,primary_key=True)
    sub_title=models.CharField(max_length=40,blank=False)
    Reg_year=models.ForeignKey(Semester,on_delete=models.CASCADE,related_name='+')
    Credit=models.IntegerField(blank=False)
    def __str__(self) :
          return f'{self.Sub_code},{self.sub_title}'


class Faculty(models.Model):
        Fac_id=models.IntegerField(blank=False)
        Fac_name=models.CharField(max_length=40,blank=False)
        sub_code=models.ForeignKey(Subject,on_delete=models.CASCADE)
        Dept_name=models.ForeignKey(Department,on_delete=models.CASCADE)
        def __str__(self) :
             return self.Fac_name

class TimetableData(models.Model):
        s_no = models.IntegerField(blank=False)
        sub_code = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='code')
        sub_title = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='title')
        fac_name = models.ForeignKey(Faculty,on_delete=models.CASCADE)
        def __str__(self) :
             return self.sub_code
         
