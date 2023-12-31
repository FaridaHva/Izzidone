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
    price = models.IntegerField(verbose_name="Price", default=0)
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
   
    
#  Professionals

class Professional(models.Model):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, verbose_name="User")
    image = models.ImageField(verbose_name="Professional's Image")
    about = models.TextField(verbose_name="About")
    verified = models.BooleanField( verbose_name="Verified Profile", default=True)
    is_available = models.BooleanField(verbose_name="Is Available", default=False)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    top_pro = models.BooleanField(verbose_name="Top Pro", default=False)
    certificate = models.ManyToManyField("services.Certificate")
    portfolio = models.ImageField("services.Portfolio")

    class Meta:
        verbose_name = "Professional"
        verbose_name_plural = "Professionals"

    def __str__(self):
        return self.image
    

class Certificate(models.Model):

    certificate = models.CharField(verbose_name="Certificate", max_length=30)
    image = models.ImageField(verbose_name="Certificate Image")

    class Meta:
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"

    def __str__(self):
        return self.certificate


class Portfolio(models.Model):

    portfolio = models.CharField(verbose_name="Portfolio", max_length=30)
    image = models.ImageField(verbose_name="Portfolio Image")

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"

    def __str__(self):
        return self.portfolio


class MySkills(models.Model):
    service = models.ForeignKey("services.SubService", verbose_name="Subservice", on_delete=models.CASCADE)
    reviews = models.CharField(max_length=50, verbose_name="Reviews" )
    rating = models.DecimalField(default="0", decimal_places=2, verbose_name="Service Rating", max_digits=5)
    price = models.CharField(verbose_name="Service Price", max_length=50)


    class Meta:
        verbose_name = "MySkills"
        verbose_name_plural = "MySkills"

    def __str__(self):
        return self.service


class AllPros(models.Model):

    all_services = models.ForeignKey("services.ChooseService", verbose_name="Service", on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name="Title")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    filter = models.BooleanField(verbose_name="Filter", default=False)


    class Meta:
        verbose_name = "AllPros"
        verbose_name_plural = "AllPros"

    def __str__(self):
        return self.title     
    

#Orders


class Order(models.Model):
    title = models.ForeignKey("services.SubService", verbose_name="Title", related_name="title_orders", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name="User")
    subService = models.ForeignKey("services.SubService", verbose_name="Subservice", related_name="subservice_orders", on_delete=models.CASCADE)
    options = models.ManyToManyField("services.AllPros", verbose_name="Options")
    address = models.CharField(verbose_name="Street Address", max_length=50)
    start_date = models.DateTimeField(verbose_name="Select Start Date")
    starting_time = models.DateTimeField(verbose_name="Select Starting Time")
    service_detail = models.TextField(verbose_name="Service Details")
    professional = models.ForeignKey("services.Professional", on_delete=models.CASCADE, verbose_name="Professional")
    upload_image = models.ImageField(verbose_name="Upload Photo")
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    is_active = models.BooleanField("Is Active", default=True)
    price = models.IntegerField(verbose_name="Total Price", default=0)


    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.title      
    


#Blogs

class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title" )
    user = models.ForeignKey("users.User", verbose_name="User", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Blog Content")
    image = models.ImageField(verbose_name="Service Image")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name= 'Blog'
        verbose_name_plural = 'Blogs'



class BlogDetails(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title" )
    content = models.TextField(verbose_name="Blog Content")
    blog = models.ForeignKey("services.Blog", on_delete=models.CASCADE, verbose_name="Blog") 
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= 'BlogDetails'
        verbose_name_plural = 'BlogDetails'    

