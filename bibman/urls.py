from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bibman_app.views import StudentViewSet, ProfessorViewSet  
from bibman_app.views import home  

router = DefaultRouter()
router.register(r'students', StudentViewSet)  
router.register(r'professors', ProfessorViewSet) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('/', include('bibman_app.urls')),  
    path('', home, name='home'), 
]
