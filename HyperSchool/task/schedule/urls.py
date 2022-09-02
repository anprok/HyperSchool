from django.urls import path
from .views import main, CourseDetailView, TeacherDetailView, AddStudentView, MyLoginView, MySignupView

urlpatterns = [
    path('schedule/main/', main, name='main'),
    path('schedule/add_course/', AddStudentView.as_view()),
    path('schedule/course_details/<int:pk>', CourseDetailView.as_view(), name='course-detail'),
    path('schedule/teacher_details/<int:pk>', TeacherDetailView.as_view(), name='teacher-detail'),
    path('login/', MyLoginView.as_view()),
    path('signup/', MySignupView.as_view()),
]
