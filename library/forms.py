from django import forms
from .models import Book,Member 

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'phone', 'outstanding_debt']

    def clean_outstanding_debt(self):
        debt = self.cleaned_data.get('outstanding_debt')
        if debt > 500:
            raise forms.ValidationError("Outstanding debt cannot exceed ₹500.")
        return debt

class IssueForm(forms.Form):
    book=forms.ModelChoiceField(queryset=Book.objects.all())
    member=forms.ModelChoiceField(queryset=Member.objects.all())