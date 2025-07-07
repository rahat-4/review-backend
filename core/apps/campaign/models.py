from django.db import models

from common.models import BaseModel

from .choices import CampaignProgress


class Campaign(BaseModel):
    """
    Represents a campaign in the system.
    """

    name = models.CharField(max_length=255, unique=True, verbose_name="Campaign Name")
    description = models.TextField(blank=True, verbose_name="Description")

    class Meta:
        verbose_name = "Campaign"
        verbose_name_plural = "Campaigns"

    def __str__(self):
        return self.name


class OrganizationCampaign(BaseModel):
    """
    Represents the association between an organization and a campaign.
    """

    name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Campaign Name"
    )
    campaign_type = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Campaign Type"
    )
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="organization_campaigns",
        verbose_name="Organization",
    )
    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE,
        related_name="campaign_organizations",
        verbose_name="Campaign",
    )
    customers = models.ManyToManyField(
        "organization.OrganizationMember",
        blank=True,
        related_name="campaigns_customers",
        verbose_name="Customers",
    )
    ammount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="Amount",
        help_text="Total amount for the campaign",
    )
    progess = models.CharField(
        max_length=25,
        choices=CampaignProgress.choices,
        default=CampaignProgress.NOT_STARTED,
        verbose_name="Progress",
        help_text="Current progress of the campaign",
    )
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True, verbose_name="Description")

    class Meta:
        unique_together = ("organization", "campaign")
        verbose_name = "Organization Campaign"
        verbose_name_plural = "Organization Campaigns"

    def __str__(self):
        return f"{self.organization} - {self.campaign}"
