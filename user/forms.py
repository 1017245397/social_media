from core.form import BaseForm
from user.models import ProfileUserModel



# Create the form class.
class ProfileUserForm(BaseForm):
    
    class Meta:
       model = ProfileUserModel
       fields = '__all__'




