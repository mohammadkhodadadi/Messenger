import pprint

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('chat', views.ChatViewSet, basename='chat')

app_name = 'api'

urlpatterns = [
    # ... other URL patterns ...
    path('', include(router.urls)),
    path('your-model-list/', views.your_model_list, name='your-model-list'),
]


print("\n@@@@@@@@@@@@@@@@@@@@@@@@\n")
pprint.pprint(router.urls)
print("\n@@@@@@@@@@@@@@@@@@@@@@@@\n")