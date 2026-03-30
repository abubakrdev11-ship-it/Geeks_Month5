from django.urls import path

from app.settings.views import About, HelloWorld, Contacts

app_name = 'settings'

urlpatterns = [
    path('hello/', HelloWorld.as_view()),
    path('about/', About.as_view()),
    path('contacts/', Contacts.as_view()),
]
