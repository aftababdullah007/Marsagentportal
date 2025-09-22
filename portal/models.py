from django.db import models

DEPARTMENT_CHOICES = [
    ("Medicare", "Medicare"),
    ("Final Expense", "Final Expense"),
    ("HVAC", "HVAC"),
    ("CSR's", "CSR's"),
    ("Management", "Management"),
]

class LeaveRequest(models.Model):
    employee_name = models.CharField(max_length=120)
    department = models.CharField(max_length=32, choices=DEPARTMENT_CHOICES)
    joining_date = models.DateField(null=True, blank=True)  # ✅ now nullable
    date = models.DateField()
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Leave: {self.employee_name} ({self.department}) {self.date}"


class Complaint(models.Model):
    agent_name = models.CharField(max_length=120)
    department = models.CharField(max_length=32, choices=DEPARTMENT_CHOICES)
    joining_date = models.DateField(null=True, blank=True)  # ✅ now nullable
    complaint_against = models.CharField(max_length=120)
    complaint_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint by {self.agent_name} ({self.department})"


class Resignation(models.Model):
    employee_name = models.CharField(max_length=120)
    department = models.CharField(max_length=32, choices=DEPARTMENT_CHOICES)
    joining_date = models.DateField(null=True, blank=True)  # ✅ now nullable
    date = models.DateField()
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resignation: {self.employee_name} ({self.department})"
