from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from email.utils import formataddr
from datetime import datetime, timedelta
from django.contrib.auth.decorators import user_passes_test

from .forms import LeaveRequestForm, ComplaintForm, ResignationForm
from .models import LeaveRequest, Complaint, Resignation


def home(request):
    return render(request, "portal/index.html")


def _send_to_department(request, subject: str, message: str, sender_display_name: str, department: str):
    dept_raw = (department or "").strip()
    NORMALIZE = {"management": "Management"}
    dept = NORMALIZE.get(dept_raw.lower(), dept_raw)

    recipients = settings.DEPARTMENT_RECIPIENTS.get(dept, [])
    if not recipients:
        messages.warning(request, f"No recipients found for {dept or 'Unknown'} department.")
        return

    from_header = formataddr((sender_display_name, settings.DEFAULT_FROM_EMAIL))
    global_rcpts = list(getattr(settings, "NOTIFICATION_EMAILS", []))

    send_mail(
        subject=subject,
        message=message,
        from_email=from_header,
        recipient_list=recipients + global_rcpts,
        fail_silently=False,
    )


def _eligible(joining_date):
    """Check if joining date is >= 6 months ago."""
    if not joining_date:
        return False
    six_months_ago = datetime.today().date() - timedelta(days=180)
    return joining_date <= six_months_ago


def leave_request_view(request):
    if request.method == "POST":
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            joining_date = form.cleaned_data.get("joining_date")
            if not _eligible(joining_date):
                messages.error(request, "You must be employed for at least 6 months to submit a leave request.")
                return redirect("home")
            obj = form.save()
        else:
            jd = request.POST.get("joining_date")
            joining_date = datetime.strptime(jd, "%Y-%m-%d").date() if jd else None
            if not _eligible(joining_date):
                messages.error(request, "You must be employed for at least 6 months to submit a leave request.")
                return redirect("home")
            obj = form.Meta.model.objects.create(
                employee_name=request.POST.get("employee_name"),
                department=request.POST.get("department"),
                joining_date=joining_date,
                date=request.POST.get("date"),
                reason=request.POST.get("reason"),
            )

        subject = "New Leave Request"
        message = (
            f"Employee: {obj.employee_name}\n"
            f"Department: {obj.department}\n"
            f"Joining Date: {obj.joining_date}\n"
            f"Leave Date: {obj.date}\n"
            f"Reason:\n{obj.reason}\n"
        )
        _send_to_department(request, subject, message, obj.employee_name, obj.department)
        messages.success(request, "Leave request submitted and emailed.")
    return redirect("home")


def complaint_view(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            joining_date = form.cleaned_data.get("joining_date")
            if not _eligible(joining_date):
                messages.error(request, "You must be employed for at least 6 months to submit a complaint.")
                return redirect("home")
            obj = form.save()
        else:
            jd = request.POST.get("joining_date")
            joining_date = datetime.strptime(jd, "%Y-%m-%d").date() if jd else None
            if not _eligible(joining_date):
                messages.error(request, "You must be employed for at least 6 months to submit a complaint.")
                return redirect("home")
            obj = form.Meta.model.objects.create(
                agent_name=request.POST.get("agent_name") or request.POST.get("employee_name"),
                department=request.POST.get("department"),
                joining_date=joining_date,
                complaint_against=request.POST.get("complaint_against", "N/A"),
                complaint_text=request.POST.get("complaint_text") or request.POST.get("reason"),
            )

        subject = "New Complaint"
        message = (
            f"Agent: {obj.agent_name}\n"
            f"Department: {obj.department}\n"
            f"Joining Date: {obj.joining_date}\n"
            f"Complaint Against: {obj.complaint_against}\n\n"
            f"Complaint:\n{obj.complaint_text}\n"
        )
        _send_to_department(request, subject, message, obj.agent_name, obj.department)
        messages.success(request, "Complaint submitted and emailed.")
    return redirect("home")


def resignation_view(request):
    if request.method == "POST":
        form = ResignationForm(request.POST)
        if form.is_valid():
            joining_date = form.cleaned_data.get("joining_date")
            if not _eligible(joining_date):
                messages.error(request, "You must be employed for at least 6 months to submit a resignation.")
                return redirect("home")
            obj = form.save()
        else:
            jd = request.POST.get("joining_date")
            joining_date = datetime.strptime(jd, "%Y-%m-%d").date() if jd else None
            if not _eligible(joining_date):
                messages.error(request, "You must be employed for at least 6 months to submit a resignation.")
                return redirect("home")
            obj = form.Meta.model.objects.create(
                employee_name=request.POST.get("employee_name"),
                department=request.POST.get("department"),
                joining_date=joining_date,
                date=request.POST.get("date"),
                reason=request.POST.get("reason"),
            )

        subject = "New Resignation"
        message = (
            f"Employee: {obj.employee_name}\n"
            f"Department: {obj.department}\n"
            f"Joining Date: {obj.joining_date}\n"
            f"Resignation Date: {obj.date}\n"
            f"Reason:\n{obj.reason}\n"
        )
        _send_to_department(request, subject, message, obj.employee_name, obj.department)
        messages.success(request, "Resignation submitted and emailed.")
    return redirect("home")


# ✅ New Records View (for staff only)
@user_passes_test(lambda u: u.is_staff)
def records_view(request):
    leaves = LeaveRequest.objects.all().order_by("-created_at")
    complaints = Complaint.objects.all().order_by("-created_at")
    resignations = Resignation.objects.all().order_by("-created_at")

    return render(request, "portal/records.html", {
        "leaves": leaves,
        "complaints": complaints,
        "resignations": resignations,
    })


# ✅ New Detail Views
@user_passes_test(lambda u: u.is_staff)
def leave_detail(request, pk):
    leave = get_object_or_404(LeaveRequest, pk=pk)
    return render(request, "portal/leave_detail.html", {"leave": leave})


@user_passes_test(lambda u: u.is_staff)
def complaint_detail(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    return render(request, "portal/complaint_detail.html", {"complaint": complaint})


@user_passes_test(lambda u: u.is_staff)
def resignation_detail(request, pk):
    resignation = get_object_or_404(Resignation, pk=pk)
    return render(request, "portal/resignation_detail.html", {"resignation": resignation})
