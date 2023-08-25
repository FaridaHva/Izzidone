from django.db import models

class Order(models.Model):
    title=models.ForeignKey("services.SubService", max_length=50, verbose_name="Title", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name="User")
    subService = models.ForeignKey("services.SubService", verbose_name="Subservice", on_delete=models.CASCADE)
    options = models.ManyToManyField(verbose_name="Options")
    address = models.CharField(verbose_name="Street Address")
    start_date = models.DateTimeField(verbose_name="Select Start Date")
    starting_time = models.DateTimeField(verbose_name="Select Start Date")
    service_detail = models.TextField(verbose_name="Service Details")
    professional = models.ForeignKey("services.Professionals", on_delete=models.CASCADE, verbose_name="Professional")
    upload_image = models.ImageField(verbose_name="Upload Photo")
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    is_active = models.BooleanField("Is Active", default=True)
    price = models.DecimalField(verbose_name="Total Price", default=0)


    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.title  