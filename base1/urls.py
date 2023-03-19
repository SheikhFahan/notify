from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.indexPage, name="index"),
    path("about_us/", views.aboutUs, name="aboutUs"),

    path("login/", views.loginPage, name="login"),
    path("register/", views.registerPage, name="register"),
    path("logout/", views.logoutPage, name = "logout"),

    path("profile/", views.profile, name="profile"),
    path("profile_view/", views.profileView, name="profileView"),
    
    path("resources/", views.resources, name="resources"),

    path("upload_notes", views.uploadNote, name="noteUpload"),
    path("upload_assignment", views.uploadAssignment, name="assignmentUpload"),
    path("upload_questions", views.uploadQuestion, name="questionPaperUpload"),

    path("delete_notes/<str:pk>/", views.deleteNote, name="noteDelete"),
    path("delete_assignment/<str:pk>/", views.deleteAssignment, name="assignmentDelete"),
    path("delete_questions/<str:pk>/", views.deleteQuestion, name="questionPaperDelete"),
    
    path("view_notes/", views.viewNotes, name = "viewNotes"),
    path("view_assignments/", views.viewAssignments, name = "viewAssignments"),
    path("views_questions/", views.viewQuestions, name = "viewQuestions"),

    path("resc/<str:pk>/", views.pdfSearch, name = 'customPdf')



]
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

