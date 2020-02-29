from django.db.models import Q
from django.views.generic import ListView
from .models import Car

import logging

logger = logging.getLogger(__name__)


class CarList(ListView):
    model = Car
    template_name = 'carlist.html'
    context_object_name = 'cars'

    def get_queryset(self):
        logger.debug(f"CarsList from user: {self.request.user.id} with params: {self.request.GET}")
        # logger.info("CarsList.get_queryset called")
        try:
            search_query = self.request.GET.get('search', '')
            qs = Car.objects.all()
            if search_query:
                qs = Car.objects.filter(Q(production__icontains=search_query)
                                        | Q(model__icontains=search_query)
                                        | Q(color__icontains=search_query)
                                        | Q(year__icontains=search_query)
                                        | Q(transmission__icontains=search_query))
            return qs
        except Exception as exc:
            logger.error(str(exc))
            raise
