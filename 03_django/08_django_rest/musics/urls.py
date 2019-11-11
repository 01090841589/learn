from django.urls import path
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Music API",
        default_version="v1",
        description="음악관련 API 서비스입니다.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="edujustin.hphk@gmail.com"),
        license=openapi.License(name="SSAFY"),
    )


)


app_name = 'musics'

urlpatterns = [
    path('musics/', views.music_list, name='music_list'),
    path('musics/<int:music_pk>/', views.music_detail, name='music_detail'),
    path('musics/<int:music_pk>/comments/', views.comments_create, name='comments_create'),
    path('comments/<int:comment_pk>/', views.comments_update_and_delete, name='comments_update_and_delete'),
    path('artists/', views.artist_list, name='artist_list'),
    path('artists/<int:artist_pk>/', views.artist_detail, name='artist_detail'),
    path('docs/', schema_view.with_ui('redoc'), name='api_docs'),
    path('swagger/', schema_view.with_ui('swagger'), name='api_swagger'),
]