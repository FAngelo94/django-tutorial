
# backend/urls.py

from django.contrib import admin
from django.urls import path, include                 # add this
from todo import views                            # add this
        
urlpatterns = [
    path('admin/', admin.site.urls),           
    path('api/todo/',views.TodoViewList.as_view()),
    path('api/todo/<int:pk>/',views.TodoViewDetail.as_view()),
    path('api/file/',views.FileUploadView.as_view())
]