from django.db import models
from django.contrib.auth.models import User ,AbstractUser
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
from django.utils import timezone
from django.dispatch import receiver
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    place=models.CharField(max_length=200,default='NULL')
    text = models.TextField(null=True, default='NULL')
    Due_date = models.DateTimeField(default=timezone.now)
    EMD =models.IntegerField(default=0,)
    DOC_Fee =models.IntegerField(default=0)
    Notice_Type=models.CharField(max_length=100,default='NULL')
    Authority_Type=models.CharField(max_length=100,default='NULL')
    Product_Services=models.CharField(max_length=100,default='NULL')
    Doc_Sale_Starts= models.DateTimeField(default=timezone.now)
    Doc_Sale_Ends= models.DateTimeField(default=timezone.now)
    Doc_Submit_Before=models.DateTimeField(default=timezone.now)
    def publish(self):
        self.Due_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    email = models.EmailField(max_length=70,blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)
    role = models.CharField(max_length=25, default='NULL')



    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)



# tender Model
class Tender(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255, blank=False)
    submitted_at = models.DateTimeField(default=timezone.now)
    posted_on = models.DateTimeField(default=timezone.now)
    Due_date = models.DateTimeField(default=timezone.now)
    EMD =models.IntegerField(default=0,)
    DOC_Fee =models.IntegerField(default=0)
    Notice_Type=models.CharField(max_length=100,default='NULL')
    Authority_Type=models.CharField(max_length=100,default='NULL')
    Product_Services=models.CharField(max_length=100,default='NULL')
    Doc_Sale_Starts= models.DateTimeField(default=timezone.now)
    Doc_Sale_Ends= models.DateTimeField(default=timezone.now)
    Doc_Submit_Before=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
#
# def create_tender(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = Tender.objects.create(user=kwargs['instance'])
#
# post_save.connect(create_profile, sender=User)
class Comment(models.Model):
    post = models.ForeignKey('grama.Post', related_name='comments')
    username = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


# Details of the village Model
class Details(models.Model):
    village=models.CharField(max_length=100,default='')
    total_men =models.IntegerField()
    total_ladies =models.IntegerField()
    total_sc =models.IntegerField()
    total_st =models.IntegerField()
    total_Physical_Disabled =models.IntegerField()


    def __str__(self):
        return self.village
    class Meta:
        verbose_name_plural = "Details"

 # Details of the village Model
class VDetails(models.Model):
    village=models.CharField(max_length=100,default='')
    total_men =models.IntegerField()
    total_ladies =models.IntegerField()
    total_sc =models.IntegerField()
    total_st =models.IntegerField()
    total_Physical_Disabled =models.IntegerField()


    def __str__(self):
        return self.village
    class Meta:
        verbose_name_plural = "VDetails"

# Birth Certicate

class BirthCertificate(models.Model):
    issue_Date = models.DateField(default=timezone.now)
    id_Card_No=models.IntegerField(default=0)
    title = models.CharField(choices=((1,("Mr")),
                                            (2,("Mrs")),
                                            ),max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.TextField(max_length=255, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    email = models.EmailField(max_length=70,blank=True)
    childName =models.CharField(max_length=100)
    Place_Of_Birth=models.CharField(max_length=100)
    Date_Of_Birth= models.DateField(default=timezone.now)
    fatherName =models.CharField(max_length=100)
    motherName =models.CharField(max_length=100)
    ID_card_no_child= models.CharField(max_length=100)
    def __str__(self):
        return self.title


# Death Certicate

class DeathCertificate(models.Model):

    issue_Date = models.DateField(default=timezone.now)
    Sex = models.CharField(choices=((1,("Male")),
                                            (2,("Female")),
                                            ),max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.TextField(max_length=255, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    Date_of_Death=models.DateField(default=timezone.now)
    Place_of_Death =models.CharField(max_length=100)
    Place_Of_Birth=models.CharField(max_length=100)
    Date_Of_Birth= models.DateField(default=timezone.now)
    fatherName =models.CharField(max_length=100)
    motherName =models.CharField(max_length=100)
    adharcard_no= models.CharField(max_length=100)
    def __str__(self):
        return self.title



class Feedback(models.Model):
    name= models.CharField(max_length=100,default='')
    subject  = models.CharField(max_length=100)
    text = models.TextField(max_length=255, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    email = models.EmailField(max_length=70,blank=True)
    issue_Date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.name
