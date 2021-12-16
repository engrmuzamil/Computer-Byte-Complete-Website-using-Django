from django.test import TestCase
from Categories.models import CATEGORY
class TestModels(TestCase):
    def setUp(self):
        self.CATEGORY = CATEGORY.objects.create(
            Category_Name= "RANDOM NAME FOR CAT",
            slug = "RANDOM-NAME-FOR-CAT"
        )

    def test_CATEGORY(self):
        self.assertEquals(self.CATEGORY.Category_Name, "RANDOM NAME FOR CAT" )
