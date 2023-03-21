from django.urls import path
from . import views

urlpatterns = [
    path('vie-for-post/', views.VieForElectoralPostView.as_view(), name='vie_for_electoral_seat'),

]