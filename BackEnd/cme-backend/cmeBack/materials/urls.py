
from django.urls import path
from .views import MateriaisListCreate, MateriaisRetrieveUpdateDestroy

urlpatterns = [
    path('materiais/', MateriaisListCreate.as_view(), name='materiais-list-create'),
    path('materiais/<int:pk>/', MateriaisRetrieveUpdateDestroy.as_view(), name='materiais-retrieve-update-destroy'),
]