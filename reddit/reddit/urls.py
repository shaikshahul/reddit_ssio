from django.conf.urls import url,include
from django.contrib import admin
from ssioapp.Views.authentication import login_user,user_logout,signup

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('social_django.urls', namespace='social')),
    url(r'^login$', login_user, name="login-page"),
    url(r'^signup/$', signup, name='signup'),


]
