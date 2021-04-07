from django.conf.urls import url, include
from webrate import views

urlpatterns = [
url(r'^auth', include('django_registration.backends.one_step.urls')),
url(r'^$', views.home, name = "home"),
url(r'profile$', views.view_profile, name = "view_profile"),
url(r'register/$', views.register, name = 'register'),
url(r'login/$', views.login, name = 'login'),
url(r'search/$', views.search_project, name = 'search_project'),
url(r'submit_rating/$', views.submit_rating, name = 'submit_rating'),
]