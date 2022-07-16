from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import CourseModelForm
from .models import Course
# Create your views here.

class CourseCreateView(View):
    template_name = "courses/course_create.html"
    def get(self, request, id_=None, *args, **kwargs):
        form = CourseModelForm()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, id_=None, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get_object(self, request, *args, **kwargs):
        context = {
            'object_list': self.get_queryset()
        }
        return render(request, self.template_name, context)

class CourseView(View):
    template_name = "courses/course_detail.html"
    def get(self, request, id_=None, *args, **kwargs):
        context = {}
        if id_ is not None:
            obj = get_object_or_404(Course, id=id_)
            context['object'] = obj
        return render(request, self.template_name, context)


def my_fbv(request, *args, **kwargs):
    print(request.method)
    return render(request, 'about.html', {})