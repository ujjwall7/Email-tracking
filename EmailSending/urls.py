from django.contrib import admin
from django.urls import path
from master.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', send_email, name='send_email'),
    path('mark_email_as_opened/<int:email_id>/', mark_email_as_opened, name='mark_email_as_opened'),

]
