from django import forms


class CreateMovieForm(forms.Form):
    title = forms.CharField(min_length=1, max_length=255, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Movie name'
                                                          }))
    description = forms.CharField(min_length=1, max_length=3000, required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Movies description '
                                                                }))
    due_date = forms.DateField(required=True,
                               widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control',
                                                             'placeholder': 'Movies due_date'
                                                             }))
    status = forms.BooleanField(required=False,)
