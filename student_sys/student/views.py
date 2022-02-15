from django.shortcuts import render
from django.http import HttpResponseRedirect, request
from django.urls import reverse
from django.views import View

from .models import Student
from .forms import StudentForm


# Create your views here.
#使用 class-based view  将功能区分的更开
class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        student = Student.get_all()
        context = {
            'students': student,
        }
        return context

    def get(self, request):
        context = self.get_context()
        form = StudentForm()
        context.update({'form': form})
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)


# def index(request):
#     students = Student.get_all()
#     if request.method == "POST":
#         form = StudentForm(request.POST)
#
#     else:
#         form = StudentForm()
#
#     context = {'student': students,
#                'form': form}
#     return render(request, 'index.html', context=context)
