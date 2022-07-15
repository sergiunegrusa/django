from django.urls import reverse, path
from .views import (
    CourseView,
    my_fbv,
)

app_name = 'courses'
urlpatterns = [
    path('', CourseView.as_view(template_name='contact.html'), name='course-list')
]