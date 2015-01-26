from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class TimeStampedModel(models.Model):
    timestamp = models.DateTimeField(
        db_column='TimeStamp',
        auto_now=True
    )

    class Meta:
        abstract = True


class Grade(TimeStampedModel):
    id = models.IntegerField(
        primary_key=True,
        db_column='GradeID'
    )
    realization = models.ForeignKey(
        'Realisation',
        db_column='RealisationID'
    )
    name = models.CharField(
        max_length=50,
        db_column='Name'
    )
    max_value = models.CharField(
        max_length=64,
        db_column='MaxValue'
    )

    class Meta:
        db_table = 'Grades'


class GradeValue(TimeStampedModel):
    id = models.IntegerField(
        primary_key=True,
        db_column='GradeValueID'
    )
    grade = models.ForeignKey(
        'Grade',
        db_column='GradeID'
    )
    registration = models.ForeignKey(
        'Registration',
        db_column='RegistrationID'
    )
    value = models.CharField(
        db_column='Value',
        max_length=10
    )
    date = models.CharField(
        db_column='Date',
        max_length=10
    )

    class Meta:
        db_table = 'GradeValues'


class Realisation(TimeStampedModel):
    id = models.IntegerField(
        primary_key=True,
        db_column='RealisationID'
    )
    ver = models.CharField(
        max_length=1,
        db_column='Ver'
    )
    subject = models.ForeignKey(
        'Subject',
        db_column='SubjectID'
    )
    semester = models.ForeignKey(
        'Semester',
        db_column='SemesterID'
    )
    user = models.ForeignKey(
        'User',
        db_column='UserID',
        null=True
    )

    class Meta:
        db_table = 'Realisations'


class Group(TimeStampedModel):
    id = models.IntegerField(
        primary_key=True,
        db_column='GroupID'
    )
    name = models.CharField(
        max_length=50,
        db_column='Name'
    )

    class Meta:
        db_table = 'Groups'


class Registration(TimeStampedModel):
    id = models.IntegerField(
        primary_key=True,
        db_column='RegistrationID'
    )
    student = models.ForeignKey(
        'Student',
        db_column='StudentID'
    )
    realisation = models.ForeignKey(
        'Realisation',
        db_column='RealisationID'
    )
    value = models.CharField(
        max_length=5,
        db_column='Value',
        null=True
    )

    class Meta:
        db_table = 'Registrations'


class Semester(TimeStampedModel):
    id = models.IntegerField(
        primary_key=True,
        db_column='SemesterID'
    )
    name = models.CharField(
        db_column='Name',
        max_length=10
    )
    active = models.CharField(
        db_column='Active',
        max_length=1
    )

    class Meta:
        db_table = 'Semesters'


class Student(TimeStampedModel):
    id = models.IntegerField(
        primary_key=True,
        db_column='StudentID'
    )
    group = models.ForeignKey(
        'Group',
        db_column='GroupID'
    )
    index = models.CharField(
        max_length=10,
        db_column='IndexNo'
    )

    class Meta:
        db_table = 'Students'


class Subject(TimeStampedModel):
    id = models.IntegerField(
        primary_key=True,
        db_column='SubjectID'
    )
    name = models.CharField(
        max_length=50,
        db_column='Name'
    )
    conspect = models.CharField(
        max_length=255,
        db_column='Conspect'
    )
    url = models.URLField(
        max_length=50,
        db_column='url',
        null=True
    )

    class Meta:
        db_table = 'Subjects'


class User(TimeStampedModel, AbstractBaseUser):
    id = models.IntegerField(
        primary_key=True,
        db_column='UserID'
    )
    uid = models.CharField(
        max_length=16,
        db_column='UID'
    )
    password = models.CharField(
        max_length=16,
        db_column='PWD'
    )
    first_name = models.CharField(
        max_length=50,
        db_column='FirstName'
    )
    last_name = models.CharField(
        max_length=50,
        db_column='LastName'
    )

    class Meta:
        db_table = 'Users'
