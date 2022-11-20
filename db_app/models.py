# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and ForeignKey has `on_delete` set to the desired behavior
#   * Remov` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Country(models.Model):
    cname = models.CharField(primary_key=True, max_length=50)
    population = models.BigIntegerField()

    class Meta:
        db_table = 'country'
    def __str__(self) -> str:
        return self.cname

class Discover(models.Model):
    cname = models.ForeignKey(Country, models.CASCADE, db_column='cname')
    disease_code = models.ForeignKey('Disease', models.CASCADE, db_column='disease_code')
    first_enc_date = models.DateField()

    class Meta:
        db_table = 'discover'
        unique_together = (('cname', 'disease_code'),)


class Disease(models.Model):
    disease_code = models.TextField(primary_key=True, max_length=50)
    pathogen = models.CharField(max_length=20)
    description = models.TextField(max_length=140)
    dtid = models.ForeignKey('Diseasetype', models.CASCADE, db_column='dtid')

    class Meta:
        db_table = 'disease'
    def __str__(self) -> str:
        return self.disease_code


class Diseasetype(models.Model):
    did = models.AutoField(primary_key=True)
    description = models.TextField(max_length=140)

    class Meta:
        db_table = 'diseasetype'
    def __str__(self) -> str:
        return f'{self.did}' 

class Doctor(models.Model):
    email = models.ForeignKey('Users', models.CASCADE, db_column='email', primary_key=True)
    degree = models.CharField(max_length=20)

    class Meta:
        db_table = 'doctor'
    def __str__(self) -> str:
        return f'{self.email}'


class Publicservant(models.Model):
    email = models.ForeignKey('Users', models.CASCADE, db_column='email', primary_key=True)
    department = models.CharField(max_length=50)

    class Meta:
        db_table = 'publicservant'
    def __str__(self) -> str:
        return f'{self.email}'


class Record(models.Model):
    email = models.ForeignKey(Publicservant, models.CASCADE, db_column='email')
    cname = models.ForeignKey(Country, models.CASCADE, db_column='cname')
    disease_code = models.ForeignKey(Disease, models.CASCADE, db_column='disease_code')
    total_deaths = models.IntegerField()
    total_patients = models.IntegerField()

    class Meta:
        db_table = 'record'
        unique_together = (('email', 'cname', 'disease_code'),)


class Specialize(models.Model):
    sid = models.ForeignKey(Diseasetype, models.CASCADE, db_column='sid')
    email = models.ForeignKey(Doctor, models.CASCADE, db_column='email')

    class Meta:
        db_table = 'specialize'
        unique_together = (('sid', 'email'),)


class Users(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    salary = models.IntegerField()
    phone = models.CharField(max_length=20)
    cname = models.ForeignKey(Country, models.CASCADE, db_column='cname')

    class Meta:
        db_table = 'users'
    def __str__(self) -> str:
        return self.email
