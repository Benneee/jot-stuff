from django.test import TestCase
from django.contrib.auth.models import User
from .models import Jotting
# Create your tests here.

class JotStuffTest(TestCase):

  @classmethod
  def setUpTestData(cls):
    testuser1 = User.objects.create_user(
      username='testuser1', password='abc123'
    )
    testuser1.save()

    # Create a new test jotting
    test_jotting = Jotting.objects.create(
      owner=testuser1, title='Jotting Title', body='a certain content....'
    )

    test_jotting.save()

  def test_jotting_creation(self):
    jotting = Jotting.objects.get(id=1)
    expected_author = f'{jotting.owner}'
    expected_title =  f'{jotting.title}'
    expected_body = f'{jotting.body}'
    self.assertEqual(expected_author, 'testuser1'),
    self.assertEqual(expected_body, 'a certain content....')
    self.assertEqual(expected_title, 'Jotting Title')
