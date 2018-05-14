from django.conf.urls import url ,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView





urlpatterns = [
    # url('^test/', include('django.contrib.auth.urls')),
    url(r'^',include('grama.urls')),
    url(r'^login/$', views.login_redirect, name='login_redirect'),
    url(r'admin/', admin.site.urls),
    url(r'^grama/', include('grama.urls')),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^grama/',include('django.contrib.auth.urls')),

]
admin.site.site_header = _("Grama Panchayath")
admin.site.site_title = _("Grama Panchayath")
