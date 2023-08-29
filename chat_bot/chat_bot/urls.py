from django.contrib import admin
from django.urls import path, include

from botsessions.views import ChatBotView
from users.views import CustomAuthToken, GetUserData

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('user_data/', GetUserData.as_view(), name='get_user_data'),
    path('chatbot/', ChatBotView.as_view(), name='chatbot'),
]
