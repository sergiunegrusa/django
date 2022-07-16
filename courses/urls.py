from django.urls import reverse, path
from .views import (
    CourseView,
    CourseListView,
    CourseCreateView,
    # my_fbv,
)

app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('<int:id>/', CourseView.as_view(), name='courses-detail'),
]