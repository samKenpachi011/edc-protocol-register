from django import forms


class RejectForm(forms.Form):
    reason = forms.Textarea()