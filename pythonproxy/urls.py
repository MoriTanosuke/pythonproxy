from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pythonproxy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'pythonproxy.views.home', name='home'),
    url(r'^about$', 'pythonproxy.views.about', name='about'),
)
