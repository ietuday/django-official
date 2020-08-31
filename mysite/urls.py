
from django.contrib import admin
from django.urls import path,include
from polls import views  
from polls.views import IndexView


urlpatterns = [
    path('', views.index),  
    path('react-index/', IndexView.as_view()),

    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls'))
]
