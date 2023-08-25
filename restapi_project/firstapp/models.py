from django.db import models
from datetime import date, datetime, time
from django.utils import timezone
# Create your models here.
class cert_category_master(models.Model):
    cat_id=models.AutoField(primary_key=True,auto_created=True)
    cat_name=models.CharField(max_length=50,blank=True,null=True)

    createdby=models.CharField(max_length=40)
    timestamp=models.DateTimeField(default=datetime.now)
    delete1=models.IntegerField(default=0)
    def __str__(self):
        return str(self.cat_id)+"  -   "+str(self.cat_name)
    class Meta:
        db_table="cert_category_master"
class emp_skill_cert_master(models.Model):
    cid=models.AutoField(primary_key=True,serialize=True,auto_created=True)
    cat=models.IntegerField()    
    cert_name=models.CharField(max_length=50)    
    tcode_substr=models.CharField(max_length=10,null=True)    
    
    createdby=models.CharField(max_length=40)
    timestamp=models.DateTimeField(default=datetime.now)
    delete1=models.IntegerField(default=0)
    def __str__(self):
        return str(self.cid)+"  -   "+str(self.cert_name)
    class Meta:
        db_table="emp_skill_cert_master"
class expert_employee(models.Model):
    exp_id=models.AutoField(primary_key=True,serialize=True,auto_created=True)
    cid=models.IntegerField()
    expert_empcode=models.IntegerField()
    sub_cat=models.IntegerField()

    createdby=models.CharField(max_length=10,blank=True,null=True)
    delete1=models.IntegerField(default=0)
    timestamp=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return str(self.exp_id)
    class Meta:
        db_table="expert_employee"
class skill_fields(models.Model):
    skill_id=models.IntegerField(primary_key=True,auto_created=True)    
    field_name=models.CharField(max_length=50,default=0)    
    createdby=models.CharField(max_length=10,blank=True,null=True)
    delete1=models.IntegerField(default=0)
    timestamp=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return str(self.skill_id)+"  -   "+str(self.field_name)
    class Meta:
        db_table="skill_fields"
class skill_field_master(models.Model):
    field_id=models.AutoField(primary_key=True,auto_created=True,serialize=True)
    cert_id=models.IntegerField(blank=True,null=True)
    skill=models.IntegerField(blank=True,null=True)
    field_value=models.CharField(max_length=50,blank=True,null=True)
    seq=models.IntegerField()

    createdby=models.CharField(max_length=10,blank=True,null=True)
    delete1=models.IntegerField(default=0)
    timestamp=models.DateField(timezone.now())
    def __str__(self):
        return str(self.field_id)+"  -   "+str(self.cert_id)+"  -   "+str(self.field_value)
    class Meta:
        db_table="skill_field_master"

class skill_field_master_inputs(models.Model):
    field_id=models.AutoField(primary_key=True,auto_created=True,serialize=True)
    cert_id=models.IntegerField(blank=True,null=True)
    skill=models.IntegerField(blank=True,null=True)
    field_value=models.CharField(max_length=50,blank=True,null=True)
    input=models.CharField(max_length=500,blank=True,null=True)
    seq=models.IntegerField()

    createdby=models.CharField(max_length=10,blank=True,null=True)
    delete1=models.IntegerField(default=0)
    timestamp=models.DateField(timezone.now())
    def __str__(self):
        return str(self.field_id)
    class Meta:
        db_table="skill_field_masterV1"
