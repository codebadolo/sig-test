from django.urls import path
from .views import ( 
                   # ClasseListView,
    EleveListView,
                  #  EleveDetailView,
    PaiementCreateView ,Eleve
                   # ClasseCreateView
                    
)


urlpatterns = [
    # Endpoint for listing all classes  https://www.madinaharabic.com/arabic-language-course/lessons/
    #path('classes/', ClasseListView.as_view(), name='class-list'),
    
    #path('classescreate/', ClasseCreateView.as_view(), name='class-create'),

    # Endpoint for listing students in a specific class
    path('classes/<int:class_id>/students/', EleveListView.as_view(), name='student-list'),

path('students/', Eleve.as_view(), name='student-detail'),

    # Endpoint for retrieving detailed information about a student
    #path('students/<int:pk>/', EleveDetailView.as_view(), name='student-detail'),

    # Endpoint for creating a new payment for a student
    path('students/<int:student_id>/payments/create/', PaiementCreateView.as_view(), name='payment-create'),
]
