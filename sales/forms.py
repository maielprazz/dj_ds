from django import forms


CHART_CHOICES= (
  ('#1','Bar Chart'),
  ('#2','Pie Chart'),
  ('#3','Line Chart'),
)

class SalesSearchForm(forms.Form):
  date_from_ = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
  date_to_= forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
  chart_type_ = forms.ChoiceField(choices=CHART_CHOICES)