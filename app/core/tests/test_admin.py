from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.admin = get_user_model().objects.create_superuser(
            email="admin@email.com",
            password="adminpass"
        )
        self.client.force_login(self.admin)

        self.user = get_user_model().objects.create_user(
            email="user@email.com",
            password="userpass",
            name="user name"
        )

    def test_user_listed(self):
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        url = reverse("admin:core_user_change", args=[self.user.id])
        res = self.client.get(url)

        self.assertEquals(res.status_code, 200)

    def test_user_add_page(self):
        url = reverse("admin:core_user_add")
        res = self.client.get(url)

        self.assertEquals(res.status_code, 200)
