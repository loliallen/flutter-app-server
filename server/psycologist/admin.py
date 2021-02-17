from django.contrib import admin
from .models import User
from account.models import User as Patient
from django import forms
from .serializer import PsycologistSerializer

# Register your models here.
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'password', 'patients']
    
    name = forms.CharField()
    username = forms.CharField()
    password = forms.CharField()
    patients = forms.ModelMultipleChoiceField(
        queryset=Patient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    def save(self, commit=True):
        m = super(UserForm, self).save(commit=False)
        print("save method")
        print(m)
        if commit:
            m.save()
        return m

class UserAdmin(admin.ModelAdmin):
    form = UserForm
    class Meta:
        model = User
        fields = "__all__"
    def save_model(self, request, obj, form, change):
        print("save from modeladmin")
        print(obj)
        return super(UserAdmin, self).save_model(request, obj, form, change)

admin.site.register(User, UserAdmin)