from core.form import BaseForm
from company.models import CompanyModel, GaleryCompanyModel ,ContactCompanyModel, CategoryCompanyModel



# Create the form class.
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
       



