from django.conf.urls import url, include
from webrate import views

urlpatterns = [
url(r'auth/', include('django_registration.backends.one_step.urls')),
url('', views.home)

]