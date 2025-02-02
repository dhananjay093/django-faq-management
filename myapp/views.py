from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class FAQListView(generics.ListAPIView):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang'] = self.request.GET.get('lang', 'en')
        return context

    @method_decorator(cache_page(60*15))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)