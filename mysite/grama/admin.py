from django.contrib import admin

from .models import (
    UserProfile, Post , Comment, Tender,BirthCertificate,VDetails,Feedback, DeathCertificate
)

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(VDetails)
admin.site.register(Tender)
admin.site.register(Feedback)
admin.site.register(BirthCertificate)
admin.site.register(DeathCertificate)
# admin.site.register(OfficeEmployee)
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms.models import inlineformset_factory
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


def upgrade_user_admin(UserProfile=None, unique_email=False,
                       list_display=None):
    """This helper function enhances the built in auth.user admin as follows:
       - If given a UserProfile class, allow it to be edited inline in the
         user admin.
       - Add "make active" and "make inactive" actions to the actions dropdown
       - Alters list_display if provided
       - Add date joined and last login filters
       - Add the email field to the first step when creating a user
       - Optionally enforce unique emails at the form level
       Usage:
           from upgrade_user_admin import upgrade_user_admin
           from myapp.models import MyUserProfile
           upgrade_user_admin(
               UserProfile=MyUserProfile, unique_email=True,
               list_display=['email', 'first_name', 'last_name'])
    """
    if UserProfile:
        class UserProfileFormSet(inlineformset_factory(User, UserProfile)):
            def __init__(self, *args, **kwargs):
                super(UserProfileFormSet, self).__init__(*args, **kwargs)
                self.can_delete = False

        # Allow user profiles to be edited inline with User
        class UserProfileInline(admin.StackedInline):
            model = UserProfile
            fk_name = 'user'
            max_num = 1
            extra = 0
            formset = UserProfileFormSet

    # use these form classes to enforce unique emails, if required
    class UniqueEmailForm:
        def clean_email(self):
            qs = User.objects.filter(email=self.cleaned_data['email'])
            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.count():
                raise forms.ValidationError(
                    'That email address is already in use')
            else:
                return self.cleaned_data['email']

    class MyUserChangeForm(UniqueEmailForm, UserChangeForm):
        email = forms.EmailField(required=True)

    class MyUserCreationForm(UniqueEmailForm, UserCreationForm):
        email = forms.EmailField(required=True)

    class MyUserAdmin(UserAdmin):
        # add the email field in to the initial add_user form
        add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('username', 'email', 'password1', 'password2')
            }),
        )

        inlines = [UserProfileInline, ] if UserProfile else []
        actions = ['make_active', 'make_inactive']
        list_filter = ['is_active', 'is_staff', 'is_superuser', 'date_joined',
                       'last_login']

        form = MyUserChangeForm if unique_email else UserChangeForm
        add_form = MyUserCreationForm if unique_email else UserCreationForm

        def make_active(self, request, queryset):
            rows_updated = queryset.update(is_active=True)
            if rows_updated == 1:
                message_bit = "1 person was"
            else:
                message_bit = "%s people were" % rows_updated
            self.message_user(
                request, "%s successfully made active." % message_bit)

        def make_inactive(self, request, queryset):
            rows_updated = queryset.update(is_active=False)
            if rows_updated == 1:
                message_bit = "1 person was"
            else:
                message_bit = "%s people were" % rows_updated
            self.message_user(
                request, "%s successfully made inactive." % message_bit)

    if list_display:
        MyUserAdmin.list_display = list_display

    # Re-register UserAdmin with custom options
    admin.site.unregister(User)
    admin.site.register(User, MyUserAdmin)
