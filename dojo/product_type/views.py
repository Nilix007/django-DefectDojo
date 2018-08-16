# #  product type
import logging

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from dojo.filters import ProductTypeFilter
from dojo.forms import Product_TypeProductForm
from dojo.models import Product_Type, Product
from dojo.utils import DojoListView, DojoCreateView, DojoUpdateView

logger = logging.getLogger(__name__)

"""
Jay
Status: in prod
Product Type views
"""


class ProductTypeList(DojoListView):
    name = 'Product Type List'
    ordering = 'name'
    filterset_class = ProductTypeFilter
    context_object_name = 'product_types'

    def get_context_data(self, **kwargs):
        kwargs.update(
            metric=False,
            name_words=[x['name'] for x in Product_Type.objects.values('name')],
        )
        return super(ProductTypeList, self).get_context_data(**kwargs)


class ProductTypeCreate(DojoCreateView):
    top_level = False
    name = 'Add Product Type'
    model = Product_Type
    fields = ['name', 'critical_product', 'key_product']
    success_message = 'Product type added successfully.'
    success_url = reverse_lazy('product_type')


class ProductTypeUpdate(DojoUpdateView):
    top_level = False
    name = 'Edit Product Type'
    model = Product_Type
    fields = ['name', 'critical_product', 'key_product']
    success_message = 'Product type updated successfully.'
    success_url = reverse_lazy('product_type')


class ProductForProductTypeCreate(DojoCreateView):
    top_level = False
    model = Product
    form_class = Product_TypeProductForm
    template_name = 'dojo/new_product.html'

    def get_product_type(self):
        return get_object_or_404(Product_Type, pk=self.kwargs.get('ptid'))

    def get_name(self):
        return "New %s Product" % self.get_product_type().name

    def get_initial(self):
        return dict(
            prod_type=self.get_product_type()
        )
