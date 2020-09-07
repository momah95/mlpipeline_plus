from django.contrib import admin
from django.urls import path, include, re_path
from allauth.account.views import confirm_email
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from dj_rest_auth.registration.views import VerifyEmailView, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),

    # my apps
    path('miners/', include('miners.urls')),

    # auth
    # re_path(r'', include('allauth.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/register/', include('dj_rest_auth.registration.urls')),

    re_path(r'^auth/verify-email/$', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', confirm_email, name='account_confirm_email'),

    re_path(r'^auth/password/reset/$', PasswordResetView.as_view(), name='password_reset'),
    re_path(r'^auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
