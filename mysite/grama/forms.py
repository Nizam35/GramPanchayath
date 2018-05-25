from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


from . import validators
from .models import UserProfile
from .models import Tender
from .models import Feedback
from .models import BirthCertificate ,DeathCertificate

class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Username', min_length=4, max_length=150)
    email = forms.EmailField(label='email')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    password1 = forms.CharField(label=' password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(
#         help_text=_(u'email address'),
#         required=True,
#
#         # validators=[
#         #     validators.validate_confusables_email,
#         # ]
#     )
#     # role = forms.CharField(required=True)
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = [
#             User.USERNAME_FIELD,
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#             'password1',
#             'password2',
#         ]
#         required_css_class = 'required'
#     def clean_email(self):
#         qs = User.objects.filter(email=self.cleaned_data['email'])
#         if self.instance:
#             qs = qs.exclude(pk=self.instance.pk)
#         if qs.count():
#             raise forms.ValidationError(
#                 'That email address is already in use')
#         else:
#             return self.cleaned_data['email']
#
#     # def clean_email(self):
#     #     email = self.cleaned_data.get('email')
#     #     username = self.cleaned_data.get('username')
#     #     if email and User.objects.filter(email=email).exclude(username=username).exists():
#     #         raise forms.ValidationError(u'Email addresses must be unique.')
#     #     return email
#
#     def save(self, commit=True):
#         user = super(RegistrationForm, self).save(commit=False)
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.email = self.cleaned_data['email']
#         # user.role = self.cleaned_data['role']
#
#         if commit:
#             user.save()
#
#         return user

class EditProfileForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )



class TenderForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    # message = forms.CharField()
    # sender = forms.EmailField()



    class Meta:
        model = Tender
        fields = (
                'title',
                'description',
            	'submitted_at',
            	'posted_on',
            	'Due_date',
                'EMD',
            	'DOC_Fee',
                'Notice_Type',
                'Authority_Type',
                'Product_Services',
                'Doc_Sale_Starts',
                'Doc_Sale_Ends'

            )


# date of Birth submission forms
class BirthCertificateForm(forms.ModelForm):
    # Options = [
    #     ('1', 'Hello'),
    #     ('2', 'World'),
    #   ]
    # title = forms.CharField(max_length=100)
    # title = forms.ChoiceField(label="select",
    #                             initial='mr',
    #                             widget=forms.Select(),
    #                             required=True)
    # message = forms.CharField()
    # sender = forms.EmailField()




    class Meta:
        model = BirthCertificate
        fields = (
                'id',
                'issue_Date',
            	'id_Card_No',
            	'name',
                'surname',
            	'address',
                'phone_number',
                'email',
                'childName',
                'Place_Of_Birth',
                'Date_Of_Birth',
                'fatherName',
                'motherName',
                'ID_card_no_child'

            )

# date of Death submission forms
class DeathCertificateForm(forms.ModelForm):
    Options = [
        ('1', 'Male'),
        ('2', 'Female'),
      ]
    # title = forms.CharField(max_length=100)
    # title = forms.ChoiceField(label="select",
    #                             initial='mr',
    #                             widget=forms.Select(),
    #                             required=True)
    # message = forms.CharField()
    # sender = forms.EmailField()




    class Meta:
        model = DeathCertificate
        fields = (

                'id',
                'issue_Date',
            	'name',
                'surname',
            	'address',
                'phone_number',
                'Date_of_Death',
                'Place_of_Death',
                'Place_Of_Birth',
                'Date_Of_Birth',
                'fatherName',
                'motherName',
                'adharcard_no'

            )

# FeedbackForm

class FeedbackForm(forms.ModelForm):
    # title = forms.CharField(max_length=100)
    # title = forms.ChoiceField(label="select",
    #                             initial='mr',
    #                             widget=forms.Select(),
    #                             required=True)
    # message = forms.CharField()
    # sender = forms.EmailField()




    class Meta:
        model = Feedback
        fields = (
                'id',
                'name',
                'subject',
            	'text',
            	'phone_number',
            	'email',
                'issue_Date'


            )
