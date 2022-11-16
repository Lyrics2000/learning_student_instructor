from django import forms


class SignINForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "id":"email_2","type":"email" , "class":"form-control form-control-prepended", "placeholder":"john@doe.com",
             "required":""

        }
    ))

    password = forms.CharField(
        widget=forms.PasswordInput(
           attrs={"id":"password_2", "type":"password", "class":"form-control form-control-prepended", "placeholder":"Enter your password",
            "required":""}
        )
    )


class SignUpForm(forms.Form):

    email = forms.CharField(widget=forms.TextInput(
        attrs={
            "name":"emailaddress", "class":"form-control style3", "type":"email" , "placeholder":"Email", "id":"username",
             "required":""

        }
    ))

    firstName = forms.CharField(widget=forms.TextInput(
        attrs={
            "name":"emailaddress", "class":"form-control style3", "type":"text" , "placeholder":"First Name", "id":"username",
             "required":""

        }
    ))

    lastName = forms.CharField(widget=forms.TextInput(
        attrs={
            "name":"emailaddress", "class":"form-control style3", "type":"text" , "placeholder":"Last Name", "id":"username",
             "required":""

        }
    ))

    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            "name":"emailaddress", "class":"form-control style3", "type":"tel" , "placeholder":"Phone", "id":"username",
             "required":""

        }
    ))

    password = forms.CharField(
        widget=forms.PasswordInput(
           attrs={ "type":"password" ,"placeholder":"Password", "id":"password","class":"form-control style3",
            "required":""}
        )
    )
    