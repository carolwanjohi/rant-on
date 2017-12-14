from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url( r'^$', views.index, name="index"),

    url(r'^profile/', views.profile, name="profile"),

    url(r'^account/logout/', views.Logout, name="logout"),

    url(r'^update/profile/', views.update_profile, name="updateProfile"),

    url(r'^create/rant', views.create_rant, name="createRant"),

    url(r'^other-rants/', views.other_rants, name="otherRants"),

    url(r'^single/rant/(\d+)', views.single_rant, name="singleRant"),

    url(r'^ajax/reaction/(?P<title>[-_\w.]+)', views.reaction, name="reaction")

]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
