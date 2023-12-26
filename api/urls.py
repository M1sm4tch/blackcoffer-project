from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData),
    path('add',views.postdata),
    path('bulk-data/', views.BulkDataModelCreateView.as_view(), name='bulk-data-create'),
]
