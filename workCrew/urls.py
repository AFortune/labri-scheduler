from django.conf.urls import patterns, url

from workCrew import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'^$', views.index, name='allergies'),
)

