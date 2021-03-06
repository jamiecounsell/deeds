from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.authtoken import views as auth_views
from users import views as user_views
from deeds import views as deed_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'deeds', deed_views.DeedViewSet)

urlpatterns = patterns('',
    url(r'^$', deed_views.home),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/register', user_views.register),
    url(r'^users/(?P<pk>[0-9]+)/$', user_views.detail),
    url(r'^users/current', user_views.whoami),
    url(r'^users/leaderboard', user_views.leaderboard),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', auth_views.obtain_auth_token)
)
