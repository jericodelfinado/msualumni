from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from views import dashboard, UsersListView, GroupsListView
from profiles.admin_jc import views as profiles_admin
#from admin_profiles.views import (
#  index,
#  add_profile_view,
#  get_profile,
#  profile_details,
#  save_profile_details,
#  save_hometown,
#  save_residence,
#  save_business,
#  advanced_search
#)
urlpatterns = patterns (
    url(r'^$', dashboard),
    url(r'^dashboard$', dashboard),
    url(r'^users$', UsersListView.as_view(), name='users-list'),
    url(r'^groups$', GroupsListView.as_view(), name='groups-list'),
    url(r'^profiles$', profiles_admin.index),
    url(r'^profiles/', include('profiles.admin_jc.urls')),
    url(r'^login/$',
        auth_views.login,
        {'template_name':'admin/login.html',
         'redirect_field_name':'/admin/dashboard'
        }),
    #url(r'^news/', include('news.urls'))
)

