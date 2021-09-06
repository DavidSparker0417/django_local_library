import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from catalog.models import BookInstance

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text='Enter a date between now and 4 weeks (default 3).')

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        # Check if a date is not in the past
        if (data < datetime.date.today()):
            raise ValidationError(_('Invalid date - renewal in past'))
        
        # Check if a date is in the allowed range(+4 weeks from today)
        if (data > datetime.date.today() + datetime.timedelta(weeks=4)):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
        
        return data
    
class RenewBookModelForm(ModelForm):
    def clean_due_back(self):
        data = self.cleaned_data['due_back']
        if (data < datetime.date.today()):
            raise ValidationError(_('Invalid date - renewal in past'))
        
        if (data > datetime.date.today() + datetime.timedelta(weeks=4)):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
        return data
    
    class Meta:
        model = BookInstance
        fields = ['due_back']
        labels = {'due_back':_('Renewal date')}
        help_text = {'due_back':_('Enter a date between new and 4 weeks(default 3).')}
        
        