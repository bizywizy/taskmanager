from django.conf.urls import url
from django.views.generic import TemplateView

from .views import TaskList, TaskAdd, TaskDelete, TaskEdit

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^task/list$', TaskList.as_view(), name='task-list'),
    url(r'^task/add$', TaskAdd.as_view(), name='task-add'),
    url(r'^task/(?P<pk>[0-9]+)/delete$', TaskDelete.as_view(), name='task-delete'),
    url(r'^task/(?P<pk>[0-9]+)/edit', TaskEdit.as_view(), name='task-edit'),
]
