from django.conf.urls import url
from views import web_page
urlpatterns = [
    url(r'^app', web_page),
]