from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from listings.choices import price_choices, bedroom_choices, state_choices, status_choices, type_home_choices
from listings.forms.listing_form import ListingForm
from listings.models import Listing


def view_listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
    }
    return render(request, 'listings/listings.html', context)


def details_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk)

    context = {
        'listing': listing
    }
    return render(request, 'listings/details_listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Status
    if 'status' in request.GET:
        status = request.GET['status']
        if status:
            queryset_list = queryset_list.filter(state__iexact=status)

    # Type of home
    if 'type_home' in request.GET:
        type_home = request.GET['type_home']
        if type_home:
            queryset_list = queryset_list.filter(state__iexact=type_home)

    # Bedrooms / lte - less equal to
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Max Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'status_choices': status_choices,
        'type_home_choices': type_home_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)


@login_required
def create_listing(request):
    if request.method == 'GET':
        form = ListingForm()

        context = {
            'form': form,
        }
        return render(request, 'listings/listing_create.html', context)
    else:
        form = ListingForm(request.POST, request.FILES)

        if form.is_valid():
            listing = form.save(commit=False)
            listing.created_by = request.user
            listing.save()
            return redirect('/')

        context = {
            'form': form,
        }
        return render(request, 'listings/listing_create.html', context)


def edit_listing(request):
    pass


def delete_listing(request):
    pass
