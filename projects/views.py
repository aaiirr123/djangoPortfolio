from django.shortcuts import render, get_object_or_404
from .models          import Project, ArtImages, ComputerScienceP, Eproject, Lproject
# Create your views here.

def aaron(request):
    projs = Project.objects
    return render(request, 'projects/aaron.html', {'projs':projs})

def about(request):
    return render(request, 'projects/about.html')

def art(request):
    artwork = ArtImages.objects
    return render(request, 'projects/art.html', {'artwork':artwork})

def computerScience(request):
    CS = ComputerScienceP.objects
    return render(request, 'projects/computerScience.html', {'CS':CS})

def entrepreneurship(request):
    Eproj = Eproject.objects
    return render(request, 'projects/Entre.html', {'Eproject':Eproj})

def leadership(request):
    Lproj = Lproject.objects
    return render(request, 'projects/leadership.html', {'Lproj': Lproj})

def leadershipProject(request, project_id):
    project_detail = get_object_or_404(Lproject, pk=project_id)
    return render(request, 'projects/leadershipProject.html', {'project': project_detail})

def computerProject(request, CP_id):
    CP_detail = get_object_or_404(ComputerScienceP, pk=CP_id)
    return render(request, 'projects/computerProject.html', {'CP': CP_detail})

def detail(request, project_id):
    project_detail = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/detail.html', {'project': project_detail})

def artwork(request, artwork_id):
    artwork_detail = get_object_or_404(ArtImages, pk=artwork_id)
    return render(request, 'projects/artwork.html', {'art': artwork_detail})

def EntProject(request, project_id):
    project_detail = get_object_or_404(Eproject, pk=project_id)
    return render(request, 'projects/EntDetail.html', {'project': project_detail})