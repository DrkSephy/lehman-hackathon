from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'hack.views.signup', name='signup'),
    
    url('^register/', CreateView.as_view(
            template_name='register.html',
            form_class=UserCreationForm,
            success_url='hack.login'
    )),
    # url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'}),

    url(r'^login/','hack.views.login', name='login'),
    # rest of your URLs as normal
# )

)
# url(r'^accounts/login/$', auth_views.login, {'template_name': 'myapp/login.html'}),
