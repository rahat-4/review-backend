from django.db import models


class OrganizationStatus(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    PENDING = "PENDING", "Pending"
    INACTIVE = "INACTIVE", "Inactive"
    DELETED = "DELETED", "Deleted"
    SUSPENDED = "SUSPENDED", "Suspended"


class MemberRole(models.TextChoices):
    STAFF = "STAFF", "Staff"
    CUSTOMER = "CUSTOMER", "Customer"
