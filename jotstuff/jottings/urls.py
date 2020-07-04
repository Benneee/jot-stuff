from django.urls import path
from .views import JottingList, JottingDetail


urlpatterns = [
  path('<int:pk>/', JottingDetail.as_view()),
  path('', JottingList.as_view())
]
