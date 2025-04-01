from django.urls import path
from .views import student_list, add_student, student_search_by_registration,chatbot_page,home
from django.urls import path
from .views import chatbot_page, search_api
urlpatterns = [
    path("chatbot/", chatbot_page, name="chatbot"),
    path('',home, name='home'),  # Home Page
    path("about/", student_list, name="student_list"),
    path("add/", add_student, name="add_student"),
    path('search_api/', search_api, name='search_api'),
    
]


