from typing import List
from django.conf import settings
from .models import NotificationRecipient

def get_recipients(category: str) -> List[str]:
    db_emails = list(
        NotificationRecipient.objects
        .filter(active=True, category__in=[category, "all"])
        .values_list("email", flat=True)
    )
    # optional fallback list from settings
    extra = getattr(settings, "NOTIFICATION_EMAILS", [])
    return sorted(set(db_emails + list(extra)))
