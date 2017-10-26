from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$', views.index),                        # INDEX.HTML
    url(r'^new',views.new),                        # NEW.HTML
    url(r'^create',views.create),                   # NEW.HTML
    url(r'^(?P<user_id>\d+)/show$', views.show),              # SHOW.HTML
    url(r'^(?P<user_id>\d+)/destroy$', views.destroy),    # SHOW.HTML - DELETE
    url(r'^(?P<user_id>\d+)/edit$', views.edit),         # EDIT.HTML
    url(r'^(?P<user_id>\d+)/update$', views.show)        # EDIT.HTML - UPDATE

]