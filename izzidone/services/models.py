from django.db import models

#OPTIONS
CHOOSE_BUTTON = (('checkbox','Checkbox'), ('radio', 'Radio'))
SERVICE_PRICE = (('hourly','Hourly'), ('fixed', 'Fixed'))   


class Service(models.Model):
    title=models.CharField(max_length=50, verbose_name="Title" )
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(verbose_name="Service Image")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name= 'Service'
        verbose_name_plural = 'Services'



class Subservice(models.Model):
    title=models.CharField(max_length=50, verbose_name="Title" )
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(verbose_name="Subservice Image")
    price = models.IntegerField(verbose_name="Price")
    service = models.ForeignKey("services.Service", on_delete=models.CASCADE, verbose_name="Service") 
    service_button = models.CharField(verbose_name="Service Button",  choices=CHOOSE_BUTTON, max_length=50)
    pricing = models.CharField("Pricing", choices=SERVICE_PRICE, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= 'Subservice'
        verbose_name_plural = 'Subservices'    


class ChooseService(models.Model):
    subService = models.ForeignKey("services.SubService", verbose_name="Subservice", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Title", max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


    class Meta:
        verbose_name = "ChooseService"
        verbose_name_plural = "ChooseServices"

    def __str__(self):
        return self.title



