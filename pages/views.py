from django.shortcuts import render
from django.views.generic import TemplateView

from listings.choices import price_choices, bedroom_choices, state_choices, status_choices, type_home_choices

from listings.models import Listing
from team.models import TeamMembers


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'status_choices': status_choices,
        'type_home_choices': type_home_choices,
    }
    return render(request, 'pages/index.html', context)


class AboutTemplateView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['team'] = TeamMembers.objects.order_by('-hire_date')

        return context
