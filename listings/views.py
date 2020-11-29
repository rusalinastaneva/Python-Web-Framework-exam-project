from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from listings.forms import ListingForm
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
    pass

def search(request):
    pass

@login_required
def create_listing(request, pk=None):
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
            return redirect('index')

        context = {
            'form': form,
        }
        return render(request, 'listings/listing_create.html', context)


def edit_listing(request):
    pass


def delete_listing(request):
    pass
