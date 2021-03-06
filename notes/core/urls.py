from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^registro/$', views.registro, name="registro"),
    url(r'^home/$', views.home, name="home"),
    url(r'^add/$', views.create_note, name="create"),
    url(r'^edit/(?P<id>\d+)/$', views.edit_note, name="edit"),
    url(r'^delete/(?P<id>\d+)/$', views.delete_note, name="delete"),
    url(r'^logout/$', views.exit, name="logout"),
    url(r'^cadastro', views.cadastroUsuario, name='cadastro'),
    url(r'sobre', views.sobre, name='sobre'),


]
