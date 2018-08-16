from django.conf.urls import url

from dojo.product_type import views

urlpatterns = [
    #  product type
    url(r'^product/type$', views.ProductTypeList.as_view(), name='product_type'),
    url(r'^product/type/(?P<pk>[0-9]+)/edit$',
        views.ProductTypeUpdate.as_view(), name='edit_product_type'),
    url(r'^product/type/add$', views.ProductTypeCreate.as_view(),
        name='add_product_type'),
    url(r'^product/type/(?P<ptid>\d+)/add_product',
        views.ProductForProductTypeCreate.as_view(),
        name='add_product_to_product_type'),
]
