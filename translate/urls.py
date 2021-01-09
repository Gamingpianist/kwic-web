from django.urls import path
from .views import account, history, KwicsubView, delete_kwic, searchByName

urlpatterns = [
    path('account/', account),
    path('history/', history),
    path('kwic-detail/', KwicsubView.as_view()),
    path('delete/', delete_kwic),
    path('search/', searchByName)
]