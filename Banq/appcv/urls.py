from django.urls import path
from . import views

urlpatterns = [
    path('', views.Trombi, name='Trombi'),

    path('create_personne/', views.create_or_edit_personne, name='create_personne'),
    path('creation/', views.creation, name='creation'),
    path('create_experience/', views.create_or_edit_experience, name='create_experience'),
    path('create_formation/', views.create_or_edit_formation, name='create_formation'),
    path('Create_Skill/', views.create_or_edit_competence, name='Create_Skill'),
    path('create_langue/', views.create_or_edit_langue, name='create_langue'),
    path('create_loisir/', views.create_or_edit_loisir, name='create_loisir'),
    path('create_cv/', views.create_or_edit_cv, name='create_cv'),
    path('create_contact/', views.create_contact, name='create_contact'),
    path('view_cv/<int:cv_id>/', views.view_cv, name='view_cv'),
    
    path('connexion', views.formulaire, name='formulaire'),
    
    path('create_or_edit_personne/', views.create_or_edit_personne, name='create_or_edit_personne'),
    path('creation/', views.creation, name='creation'),
    path('create_or_edit_experience/', views.create_or_edit_experience, name='create_or_edit_experience'),
    path('create_or_edit_formation/', views.create_or_edit_formation, name='create_or_edit_formation'),
    path('create_or_edit_competence/', views.create_or_edit_competence, name='create_or_edit_competence'),
    path('create_or_edit_langue/', views.create_or_edit_langue, name='create_or_edit_langue'),
    path('create_or_edit_loisir/', views.create_or_edit_loisir, name='create_or_edit_loisir'),
    path('create_or_edit_cv/', views.create_or_edit_cv, name='create_or_edit_cv'), 
    path('register/', views.register, name='register'),
    path('create_contact/', views.create_contact, name='create_contact'),






    path('view_experiences/', views.view_experiences, name='view_experiences'),
    path('view_formations/', views.view_formations, name='view_formations'),
    path('view_competences/', views.view_competences, name='view_competences'),
    path('view_langues/', views.view_langues, name='view_langues'),
    path('view_hobbies/', views.view_hobbies, name='view_hobbies'),

    path('view_person/', views.view_person, name='view_person'),
    path('view_contact/', views.view_contact, name='view_contact'),

    path('view_cvs/', views.view_cvs, name='view_cvs'),

    path('Trombi/', views.Trombi, name='Trombi'),
    path('cv/<int:pk>/', views.cv_detail, name='cv_detail'),  
    
    path('cv/<int:cv_id>/edit/', views.edit_cv, name='edit_cv'),

    path('cv/<int:cv_id>/delete/', views.delete_cv, name='delete_cv'),

path("cv/<int:cv_id>/send_email/", views.send_cv_email, name="send_cv_email"),
]
