from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .forms import SearchForm, StudentAddForm
from .models import Course, Teacher, Student


def main(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        q = request.GET.get('q')
        if q:
            courses = Course.objects.filter(title__contains=q)
        else:
            courses = Course.objects.all()
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()
        courses = Course.objects.all()
    return render(request, 'main.html', {'form': form, 'courses': courses, 'quantity': len(courses)})


class CourseDetailView(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        students = Student.objects.filter(course=course.pk)
        context['students'] = students
        return context


class TeacherDetailView(DetailView):
    model = Teacher


class AddStudentView(CreateView):
    form_class = StudentAddForm
    template_name = "student_enroll.html"
    success_url = "/schedule/add_course/"


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/schedule/main'
    template_name = 'signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
