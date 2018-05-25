from django.conf.urls import url
from django.contrib.auth import views as auth_views

from django.views.generic import TemplateView
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)
from django.conf import settings
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^tender/$', views.post_list, name='post_list'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^pinbox/$', views.pinbox, name='pinbox'),
    url(r'^inbox/$', views.inbox, name='inbox'),
    url(r'^index/$', views.index, name='index'),
    url(r'^download/$', views.download, name='download'),
    url(r'^gindex/$', views.gindex, name='index'),
    url(r'^error/$', views.error, name='error'),
    url(r'^details/$', views.details, name='details'),
    url(r'^mdetails/$', views.mdetails, name='mdetails'),
    # url(r'^forms/$', views.post_forms, name='post_form'),
    url(r'^forms/$', views.post_tender, name='post_tender'),
    url(r'^bforms/$', views.birth, name='birth'),
    url(r'^dforms/$', views.death, name='death'),
    # for to send feedback
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^gmaps/$', views.gmaps, name='gmaps'),
    url(r'^login/$',login,{'template_name':'grama/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'grama/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^service/$', views.service, name='service'),
    url(r'^password_change/$', views.password_change, name='password_change'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

]

#
# url(r'^reset-password/$', password_reset,name  ='reset_password'),
# url(r'^reset-password/done$', password_reset_done,name='password_reset_done'),
# # url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,name='password_reset_confirm '),
# url(r'^reset/password/confirm(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
# url(r'^reset-password/complete/$', password_reset_complete,name='password_reset_complete'),
