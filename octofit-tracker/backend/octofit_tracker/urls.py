"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardViewSet)

@api_view(['GET'])
def api_root(request):
    """Return API entry points using the Codespace external URL when available."""

    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev"
        make_url = lambda path: f"{base_url}{path}"
    else:
        make_url = request.build_absolute_uri

    return Response({
        'users': make_url('/api/users/'),
        'teams': make_url('/api/teams/'),
        'activities': make_url('/api/activities/'),
        'workouts': make_url('/api/workouts/'),
        'leaderboard': make_url('/api/leaderboard/'),
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    # Serve the same DRF API-root view at '/' and '/api/' (no redirect)
    path('', api_root, name='api_root'),
    path('api/', api_root),
    path('api/', include(router.urls)),
]
