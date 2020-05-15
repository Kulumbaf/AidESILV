
from django.conf.urls import url

from .views import (
    add_to_cart,
    delete_from_cart,
    order_details,
    checkout,
    process_payment,
    update_transaction_records,
    success
)

app_name = 'shopping_cart'

urlpatterns = [
    url(r'^ajouter-au-panier/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    url(r'^resume-des-commandes/$', order_details, name="order_summary"),
    url(r'^succes/$', success, name='purchase_success'),
    url(r'^produit/suppression/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
    url(r'^checkout/$', checkout, name='checkout'),
    url(r'^paiement/(?P<order_id>[-\w]+)/$', process_payment, name='process_payment'),
    url(r'^mis-a-jour-transaction/(?P<order_id>[-\w]+)/$', update_transaction_records,
        name='update_records')
]