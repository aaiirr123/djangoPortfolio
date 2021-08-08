
from django.contrib import admin
from django.urls import path
import projects.views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', projects.views.aaron, name='aaron'),
    path('about/', projects.views.about, name='about'),
    path('art/', projects.views.art, name='artworks'),
    path('computerscience/', projects.views.computerScience, name='computerScience'),
    path('entrepreneurship/', projects.views.entrepreneurship, name='entrepreneurship'),
    path('leadership/', projects.views.leadership, name='leadership'),
    path('leadership/<int:project_id>', projects.views.leadershipProject, name='leadershipProject'),
    path('computerscience/<int:CP_id>', projects.views.computerProject, name='computerProject'),
    path('art/<int:artwork_id>', projects.views.artwork, name='art'),
    path('projects/<int:project_id>', projects.views.detail, name='detail'),
    path('entrepreneurship/<int:project_id>', projects.views.EntProject, name='EntProject'),

] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
