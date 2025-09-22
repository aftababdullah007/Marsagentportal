from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("leave/", views.leave_request_view, name="leave"),
    path("complaint/", views.complaint_view, name="complaint"),
    path("resignation/", views.resignation_view, name="resignation"),
    path("records/", views.records_view, name="records"),  # ✅ New page

    # ✅ Detail pages
    path("leave/<int:pk>/", views.leave_detail, name="leave_detail"),
    path("complaint/<int:pk>/", views.complaint_detail, name="complaint_detail"),
    path("resignation/<int:pk>/", views.resignation_detail, name="resignation_detail"),
]
