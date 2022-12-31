from django import forms


class RegisterCompanyForm(forms.Form):
    
    name=forms.CharField(label="Nombre", max_length=150 )
    description= forms.CharField(label="Descripción", max_length=450)#textfield
    comment=forms.CharField(label="Comentarios", max_length=500)#textfield
    address=forms.CharField(label="Direccion", max_length=50)
    cell_phone=forms.CharField(label="Celular", max_length=10)
    
    nit=forms.CharField(label="NIT", max_length=20)
    description= forms.CharField(label="Descripción")#textfield
    mision=forms.CharField(label="Misión")#textfield
    vision=forms.CharField(label="Visión")#textfield
    name=forms.CharField(label="Nombre del Emprendimiento", max_length=50)
    facebook=forms.CharField(label="Facebook", max_length=150)
    linkedin=forms.CharField(label="linkedin", max_length=150)
    instagram=forms.CharField(label="Instagram", max_length=150)
    twitter=forms.CharField(label="Twitter", max_length=150)
    web_site=forms.CharField(label="Sitio Web", max_length=150)

