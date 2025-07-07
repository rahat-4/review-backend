from django.contrib.auth import get_user_model
from django.db import models

from address.models import AddressField
from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField

from common.models import BaseModel

from .choices import OrganizationStatus, MemberRole
from .utils import get_organization_media_path_prefix, get_organization_slug

User = get_user_model()


class Organization(BaseModel):
    slug = AutoSlugField(unique=True, populate_from=get_organization_slug)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(
        upload_to=get_organization_media_path_prefix, blank=True, null=True
    )
    subdomain = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        null=True,
        help_text="Required for non-chamber and non-pharmacy organizations",
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sub_organizations",
    )
    status = models.CharField(
        max_length=25,
        choices=OrganizationStatus.choices,
        default=OrganizationStatus.ACTIVE,
    )
    description = models.TextField(blank=True, null=True)
    address = AddressField(blank=True, null=True)
    phone = PhoneNumberField(unique=True, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["phone"],
                name="unique_non_null_phone",
                condition=~models.Q(phone=None),
            )
        ]

    def __str__(self):
        return f"{self.name} (Slug: {self.slug}) (UID: {self.uid})"


class OrganizationMember(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="organization_members"
    )
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="members"
    )
    role = models.CharField(
        max_length=25, choices=MemberRole.choices, default=MemberRole.CUSTOMER
    )

    def __str__(self):
        return f"{self.user.phone} → {self.organization.name} -{self.role}"
