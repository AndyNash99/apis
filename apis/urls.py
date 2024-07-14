from django.urls import path, include


urlpatterns = [
    path('timestamp/', include('timestamp.urls')),
]
