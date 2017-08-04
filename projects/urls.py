from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^projects-completed/$', views.CompletedView.as_view(), name='projectsCompleted'),
    url(r'^projects-under-development/$', views.UnderDevelopmentView.as_view(), name='projectsUnderDevelopment'),
]
