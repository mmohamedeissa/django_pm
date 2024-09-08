from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models
from . import forms
from django.urls import reverse_lazy, reverse


# Create your views here.

class ProjectListView(ListView):
    model = models.Project
    template_name = 'project/project_list.html'
    paginate_by = 9

    def get_queryset(self):
        query_set = super().get_queryset()
        where = {}
        q = self.request.GET.get('q', None)

        if q:
            where['title__icontains'] = q

        return query_set.filter(**where)

class ProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'project/project_create.html'
    success_url = reverse_lazy('project_list')


class ProjectUpdateView(UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = 'project/project_update.html'
    def get_success_url(self):
        return reverse('project_update',args=[self.object.id])


class TaskCreateView(CreateView):
    model = models.Task
    fields = ['project', 'description']
    template_name = 'project/task_create.html'
    http_method_names = ['post']
    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])



class TaskUpdateView(UpdateView):
    model = models.Task
    fields = ['is_complete']
    http_method_names = ['post']
    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])




class TaskDeleteView(DeleteView):
    model = models.Task
    http_method_names = ['post']
    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])


class ProjectDeleteView(DeleteView):
    model = models.Project
    template_name = 'project/task_delete.html'
    success_url = reverse_lazy('project_list')
