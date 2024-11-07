from django.http import HttpRequest, JsonResponse
from django.views.decorators.cache import cache_page

from .models import Rate
from .utils import get_rate_from_api


@cache_page(10)
def get_current_usd(request: HttpRequest) -> JsonResponse:
    """
    Эндпоинт для получения актуального курса доллара к рублю в формате JSON и
    10 последних запросов курсов.
    :return: JsonResponse
    """
    last_rates_objects = Rate.objects.all()[:10]
    last_rates = [rate_object.rate for rate_object in last_rates_objects]
    current_rate = get_rate_from_api()
    rate = Rate(rate=current_rate)
    rate.save()
    return JsonResponse({"current_rate": current_rate, "last_rates": last_rates})
