from django.test import TestCase
from django.urls import reverse

from .models import Rate


class GetCurrentUSDTestCase(TestCase):
    """Тест эндпоинта для получения курса доллара. Родитель: TestCase."""

    def test_get_current_usd(self) -> None:
        """Метод для тестирования получения курса доллара."""

        response = self.client.get(reverse("get_current_usd"))
        last_rates_objects = Rate.objects.all()[:10]
        last_rates = [rate_object.rate for rate_object in last_rates_objects]
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "current_rate")
        for last_rate in last_rates:
            self.assertContains(response, last_rate)
