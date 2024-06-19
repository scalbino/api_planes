from django.urls import path
from .views import ReciveToken, SendToken

urlpatterns = [
    path('token/',ReciveToken.as_view(), name='receivetoken'),
    path('token/<str:unique_id>/', SendToken.as_view(), name='sendtoken'),


]