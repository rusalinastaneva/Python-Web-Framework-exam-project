from django.urls import path

from listings.views import view_listings, details_listing, search, \
    ListingCreateView, ListingUpdateView, DeleteListingView

urlpatterns = [
    path('', view_listings, name='view listings'),
    path('details/<int:pk>', details_listing, name='details listing'),
    path('search/', search, name='search'),
    path('create/', ListingCreateView.as_view(), name='create listing'),
    path('edit/<int:pk>', ListingUpdateView.as_view(), name='edit listing'),
    path('delete/<int:pk>', DeleteListingView.as_view(), name='delete listing'),
]
