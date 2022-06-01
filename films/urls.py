from django.urls import path
from .views import (
                            FilmsDetailView, 
                            FilmsListView
                        )
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('films-list', FilmsListView.as_view(), name = 'flims_list'),
    path('film-detail/<int:pk>', FilmsDetailView.as_view(), name = 'film_detail'),
    path('token-create', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-refresh', TokenRefreshView.as_view(), name='token_refresh'),
]