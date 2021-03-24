from django.contrib import admin
from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.admin import UserAdmin
from .models import User, Child

class ChildInline(admin.TabularInline):
    model = Child

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('__all__')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_pasword(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = (
        (None, { 'fields' : (
            'username',
            'password',
        )}),
        ("Personal Info", { 'fields' : (
            'email',
            'first_name',
            'last_name',
            'age',
            'children',
        )}),
        ("Permissions", { 'fields' : (
            'is_active',
            'is_staff',
            'is_superuser',
        )}),
        ("important Dates", { 'fields' : (
            'date_joined',
            'last_login',
        )}),
        ("Additional Fields", {'fields': (
            'diaries',
            'transfer_groups',
            'done_transfer_groups'
        )}),
    )
    # The forms to add and change user instances

# Register your models here.

admin.site.register(User, CustomUserAdmin)
admin.site.register(Child)