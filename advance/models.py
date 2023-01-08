from django.db import models
import uuid
# Create your models here.

class Advance(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    owner = models.ForeignKey(
        "core.User",
        related_name="advances",
        on_delete = models.CASCADE
    )

    DEBT = "Debt"
    IMPROVEMENT = "Improvement"
    CAR = "Car"
    OCCASION = "Occasion"

    REASON_FOR_ADVANCE_CHOICES = [
        (DEBT, "Consolidating debt"),
        (IMPROVEMENT, "Home improvement/repair"),
        (CAR, "Car"),
        (OCCASION, "Special occasion/event"),
    ]

    description = models.TextField(max_length=1000)
    first_line_address = models.CharField(max_length=255)
    second_line_address = models.CharField(max_length=255)
    postocde = models.CharField(max_length=255)
    town_or_city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    monthly_rent = models.DecimalField(max_digits=8, decimal_places=2)
    lease_agreement_file = models.FileField()
    rent_protection_policy_file = models.FileField()
    tenant_vetting_file = models.FileField()
    amount_of_rent_selling = models.DecimalField(max_digits=8, decimal_places=2)

    THREE_MONTHS = 3
    SIX_MONTHS = 6
    TWEVLE_MONTHS = 12
    TWENTYFOUR_MONTHS = 24
    THIRTYSIX_MONTHS = 36
    FOURTYEIGHT_MONTHS = 48
    SIXTY_MONTHS = 60

    ADVANCE_DURATION_CHOICES = [
        (THREE_MONTHS, "3 months"),
        (SIX_MONTHS, "6 months"),
        (TWEVLE_MONTHS, "12 months"),
        (TWENTYFOUR_MONTHS, "24 months"),
        (THIRTYSIX_MONTHS, "36 months"),
        (FOURTYEIGHT_MONTHS, "48 months"),
        (SIXTY_MONTHS, "60 months"),
    ]

    estimated_monthly_payment = models.DecimalField(max_digits=8, decimal_places=2)

    TERM_INTEREST_CHOICES = [
        (0.2399, 0.2399),
        (0.2199, 0.2199),
        (0.1999, 0.1999),
        (0.1799, 0.1799),
        (0.1599, 0.1599),
        (0.1399, 0.1399),
        (0.1299, 0.1299),
    ]

    name_on_bank_account = models.CharField(max_length=255)
    bank_account_number = models.CharField(max_length=100)
    sort_code_bank_account = models.CharField(max_length=100)


