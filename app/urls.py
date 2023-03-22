from django.urls import path
from . import views

urlpatterns = [
    path('vie-for-post/', views.VieForElectoralPostView.as_view(), name='vie_for_electoral_seat'),
    path('vote/', views.VotingView.as_view(), name='cast_vote'),
    path('polls/', views.PollingView.as_view(), name='polls'),
    path('nominations/', views.NominationView.as_view(), name='nominate_candidate'),

]