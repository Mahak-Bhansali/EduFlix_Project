from django import forms
from .models import Course, Lesson


class CreateCourseForm(forms.Form):

    class Meta:
        model = Course
        fields = "__all__"


class CreateLessonForm(forms.Form):

    class Meta:
        model = Lesson
        fields = "__all__"
