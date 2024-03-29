from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EleveViewSet, EleveDetailView

router = DefaultRouter()
router.register(r'eleves', EleveViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('eleves/<int:pk>/', EleveDetailView.as_view(), name='eleve-detail'),
]

# GET /eleves/: Retrieve a list of all students and create a new student.
# GET /eleves/{id}/: Retrieve details about a specific student.
# PUT /eleves/{id}/: Update a specific student.
# DELETE /eleves/{id}/: Delete a specific student.