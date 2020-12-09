from django.urls import path

from listings.views import view_listings, details_listing, search, delete_listing, \
    ListingCreateView, ListingUpdateView

urlpatterns = [
    path('', view_listings, name='view listings'),
    path('details/<int:pk>', details_listing, name='details listing'),
    path('search/', search, name='search'),
    path('create/', ListingCreateView.as_view(), name='create listing'),
    path('edit/<int:pk>', ListingUpdateView.as_view(), name='edit listing'),
    path('delete/<int:pk>', delete_listing, name='delete listing'),
    # path('create/', create_listing, name='create listing'),
    # path('edit/<int:pk>', edit_listing, name='edit listing'),
]
