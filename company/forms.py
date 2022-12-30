from core.form import BaseForm
from company.models import CompanyModel, GaleryCompanyModel ,ContactCompanyModel, CategoryCompanyModel
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

"""
    logo= forms.FileField(upload_to='logos')
    photo=forms.FileField(upload_to='company')
    document=forms.CharField(label="Numero de Identificación", max_length=20, unique=True)
    first_names= forms.CharField(label="Nombres", max_length= 150)
    last_names=forms.CharField(label="Apellidos", max_length=150)
    birthdate=forms.DateField(label="Fecha de Nacimiento")
    phone_number=forms.CharField(label="Numero de telefono", max_length=15)
    email=forms.CharField(label="Correo", max_length=50)
"""
"""
    civil_status= forms.CharField("Estado Civil", max_length=20, choices = CIVIL_ESTATUS_CHOICES)
    gender=forms.CharField("Genero", max_length=10, choices = GENDER_CHOICES)   
    type_document=forms.CharField("Tipo de Documento", max_length=10, choices = TYPE_DOCUMENT_CHOICES)# por que estos son distintos al foreingKEY
    user=forms.OneToOneField(User, on_delete=models.CASCADE)
    user=forms.ForeignKey(User, on_delete=models.CASCADE)
    company=forms.ForeignKey(CompanyModel, on_delete= models.CASCADE)
"""



"""# Create the form class.
class CompanyForm(BaseForm):
    
    class Meta:
       model = CompanyModel
       fields = '__all__'


class CategoryCompanyForm(BaseForm):
    
    class Meta:
       model = CategoryCompanyModel
       fields = '__all__'

    
class ContactCompanyForm(BaseForm):
    
    class Meta:
       model = ContactCompanyModel
       fields = '__all__'


class GaleryCompanyForm(BaseForm):
    
    class Meta:
       model = GaleryCompanyModel
       fields = '__all__'
"""       



