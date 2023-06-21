from django.test import TestCase
from django.urls import reverse
from .models import CusomUser




class SingupTestCase(TestCase):
    def test_singup_view(self):
        response = self.client.post(
            reverse('user:singup'),
            data ={
                'first_name' : 'shopuser1',
                'username' : 'shopuser1',
                'email' : 'shopser@gamil.com',
                'password' : 'user13#!',
                'password2' : 'user13#!',
                }
            )
        user =CustomUser.objects.get(username ='shopuser1')
        serlf.AssertEqual(user.first_name, 'shopuser1') 
        serlf.AssertEqual(user.email, 'shopser@gamil.com')
        serlf.AssertTrue(user.check_password('user13#!')) 