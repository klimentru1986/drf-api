from django.urls import path
from user.views import CreateUserView

app_name = 'user'

urlpatterns = [
    path('create/', view=CreateUserView.as_view(), name='create'),
]
