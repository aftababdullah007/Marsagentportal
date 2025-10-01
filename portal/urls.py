from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("leave/", views.leave_request_view, name="leave"),
    path("complaint/", views.complaint_view, name="complaint"),
    path("resignation/", views.resignation_view, name="resignation"),
    path("records/", views.records_view, name="records"),  # staff-only

    # Auth
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(template_name="portal/login.html"),
        name="login",
    ),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Optional: signup to satisfy the `{% url 'signup' %}` link in your login page
   

    # Detail pages
    path("leave/<int:pk>/", views.leave_detail, name="leave_detail"),
    path("complaint/<int:pk>/", views.complaint_detail, name="complaint_detail"),
    path("resignation/<int:pk>/", views.resignation_detail, name="resignation_detail"),
]
