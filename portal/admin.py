from django.contrib import admin
from .models import LeaveRequest, Complaint, Resignation

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ("employee_name", "department", "date", "created_at")
    list_filter = ("department", "date", "created_at")
    search_fields = ("employee_name", "reason")

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ("agent_name", "department", "complaint_against", "created_at")
    list_filter = ("department", "created_at")
    search_fields = ("agent_name", "complaint_against", "complaint_text")

@admin.register(Resignation)
class ResignationAdmin(admin.ModelAdmin):
    list_display = ("employee_name", "department", "date", "created_at")
    list_filter = ("department", "date", "created_at")
    search_fields = ("employee_name", "reason")
