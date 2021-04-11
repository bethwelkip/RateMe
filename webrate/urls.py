from django.conf.urls import url, include
from webrate import views

urlpatterns = [
    # url(r'^auth', include('django_registration.backends.simple.urls')),
# url(r'^auth', include('django_registration.backends.one_step.urls')),
url(r'^$', views.home, name = "home"),
url(r'profile$', views.view_profile, name = "view_profile"),
url(r'register/$', views.register, name = 'register'),
url(r'login/$', views.login, name = 'login'),
url(r'upload/$', views.upload_project, name = 'upload_project'),
url(r'search/$', views.search_project, name = 'search_project'),
url(r'^view_project/submit_rating/(?P<id>\d+)$', views.submit_rating, name = 'submit_rating'),
url(r'^view_project/(?P<id>\d+)$', views.view_project, name = 'view_project'),
]