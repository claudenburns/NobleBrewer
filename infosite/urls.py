from django.conf.urls import patterns, url, include

from infosite import views
#from infosite.views import AboutView

urlpatterns = patterns('',
    url(r'^about/', views.about, name='about'),
    #url(r'^about/', AboutView.as_view()),
    url(r'^$', views.index, name='index'),
   
)
