from django.test import TestCase
from usuario.models import Opcionale

# models test
        
class OpcionaleTest(TestCase):
    
    def create_opcionale(self, user="Daniel", telefono="0982933292"):
        return Opcionale.objects.create(user=user, telefono=telefono)
    
    def test_create_opcionale(self):
       o= self.create_opcionale()
       self.assertTrue(isinstance(o, Opcionale))
       self.assertEqual(o.__unicode__(),o.user)
  
