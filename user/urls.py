from django.urls import path

from .views import (
    SignUpView,
    LogInView,
    KakaoSignInView
)

urlpatterns = [
    path('/sign_up', SignUpView.as_view()),
    path('/login', LogInView.as_view()),
    path('/kakao_login', KakaoSignInView.as_view())
]