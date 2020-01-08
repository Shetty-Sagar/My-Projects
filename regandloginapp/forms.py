from django import forms
class RegistrationForm(forms.Form):
    firstname=forms.CharField(
        label="enter your first name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your first name'
            }
        )
    )
    lastname=forms.CharField(
        label="enter your last name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your last name'
            }
        )
    )
    username=forms.CharField(
        label="enter your user name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your user name'
            }
        )
    )
    password=forms.CharField(
        label="enter your password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'your password'
            }
        )
    )
    mobile=forms.IntegerField(
        label="enter your mobile number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your mobile number',
            }
        )
    )
    email=forms.EmailField(
        label="enter your email id",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'your email id'
            }
        )
    )
    GENDER_CHOICES=(
        ('male','MALE'),
        ('female','FEMALE')
    )
    gender=forms.ChoiceField(
        widget=forms.RadioSelect(),
         choices=GENDER_CHOICES,
         label="select your gender"

    )
    y=range(1997,2018)
    date_of_birth=forms.DateField(
        widget=forms.SelectDateWidget(years=y),
        label="enter your date of birth"
    )
class LoginForm(forms.Form):
    username = forms.CharField(
        label="enter your user name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your user name'
            }
        )
    )
    password = forms.CharField(
        label="enter your password",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your password'
            }
        )
    )


