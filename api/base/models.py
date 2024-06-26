from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Company(models.Model):

    class Meta:
        verbose_name_plural = "Company Information"

    # ======= Info =======
    name = models.CharField(
        max_length=255,
        help_text="Enter the full name.",
    )
    short_name = models.CharField(
        max_length=255,
        help_text="Enter the short name.",
    )
    motto = models.CharField(
        max_length=255,
        help_text="Enter the company motto.",
    )
    # ======= Contact =======
    primary_email = models.EmailField(help_text="Enter the primary contact email.")
    secondary_email = models.EmailField(
        help_text="Enter the secondary contact email.", blank=True
    )
    primary_phone = models.CharField(
        max_length=255,
        help_text="Enter the primary contact phone number.",
    )
    secondary_phone = models.CharField(
        max_length=255,
        help_text="Enter the secondary contact phone number.",
        blank=True,
    )

    # ======= Addressing =======
    building = models.CharField(
        max_length=255,
        help_text="Enter the location building",
        blank=True,
    )
    street = models.CharField(
        max_length=255,
        help_text="Enter the location street",
        blank=True,
    )
    PO_box = models.CharField(
        max_length=255,
        help_text="Enter the P.O Box",
        blank=True,
    )
    city_name = models.CharField(
        max_length=255,
        help_text="Enter the city name",
        blank=True,
    )
    zip_code = models.CharField(
        max_length=255,
        help_text="Enter the zip code",
        blank=True,
    )
    open_days = models.CharField(
        max_length=255,
        help_text="e.g Monday - Friday",
        blank=True,
    )
    open_hours = models.CharField(
        max_length=255,
        help_text="e.g 8:15AM - 05:00PM",
        blank=True,
    )

    # ======= Social =======
    twitter_x = models.URLField(
        max_length=255,
        help_text="Enter the X account url",
        blank=True,
    )
    facebook = models.URLField(
        max_length=255,
        help_text="Enter the facebook account url",
        blank=True,
    )
    instagram = models.URLField(
        max_length=255,
        help_text="Enter the Instagram account url",
        blank=True,
    )
    linkedin = models.URLField(
        max_length=255,
        help_text="Enter the Linkedin account url",
        blank=True,
    )
    tiktok = models.CharField(
        max_length=255,
        help_text="Enter the organization's tiktok account url (Not required).",
        blank=True,
    )
    whatsapp = models.URLField(
        max_length=255,
        help_text="Enter the Whatsapp url in the format 'https://wa.me/254700000000'. Replace with appropriate phone number",
        blank=True,
    )

    @staticmethod
    def get_or_create_singleton():
        """
        Ensure only one record exists
        """

        obj, created = Company.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return self.name


@receiver(post_save, sender=Company)
def ensure_single_company(sender, instance, created, **kwargs):
    """
    Signal receiver to ensure only one record exists
    """

    if created and Company.objects.count() > 1:
        instance.delete()
