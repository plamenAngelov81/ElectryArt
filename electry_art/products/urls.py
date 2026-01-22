from django.urls import path, include
from electry_art.products.views import (index, ProductCreateView, ProductListView, ProductDetailsView, ProductEditView, \
    PhotoCreateView, ToggleLikeView, WishlistView, ProductCategoryListView, PhotoDetailsView, PhotoEditView, \
    PhotoDeleteView, SearchView, ProductTypeCreateView, ProductMaterialCreateView, ProductColorCreateView,
    ProductPropsListView, ProductTypeEditView, ProductTypeDeleteView, ProductColorEditView, ProductMaterialEditView,
    ProductMaterialDeleteView, ProductColorDeleteView
    )


urlpatterns = [
    path('', index, name='index'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),

    path('products/', include([
        path('', ProductListView.as_view(), name='product list'),
        path('create/', ProductCreateView.as_view(), name='product create'),
        path('photo-create/', PhotoCreateView.as_view(), name='photo create'),
        path('type-create/', ProductTypeCreateView.as_view(), name='type create'),
        path('material-create/', ProductMaterialCreateView.as_view(), name='material create'),
        path('color-create/', ProductColorCreateView.as_view(), name='color create'),

        path('props/', include([
            path("",  ProductPropsListView.as_view(), name='props list'),
            path('type-edit/<int:pk>/', ProductTypeEditView.as_view(), name='type edit'),
            path('type-delete/<int:pk>/', ProductTypeDeleteView.as_view(), name='type delete'),
            path('color-edit/<int:pk>/', ProductColorEditView.as_view(), name='color edit'),
            path('color-delete/<int:pk>/', ProductColorDeleteView.as_view(), name='color delete'),
            path('material-edit/<int:pk>/', ProductMaterialEditView.as_view(), name='material edit'),
            path('material-delete/<int:pk>/', ProductMaterialDeleteView.as_view(), name='material delete'),
        ])),

        path('search/', SearchView.as_view(), name='search'),
        # 👇 Specific photo-related routes first!
        path('<int:product_pk>/photo/edit/<int:pk>/', PhotoEditView.as_view(), name='photo edit'),
        path('product/<int:product_pk>/photo/<int:pk>/', PhotoDetailsView.as_view(), name='photo details'),
        path('<int:product_pk>/photo/delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo delete'),
        # 👇 More generic product routes below
        path('category/<str:category>/', ProductCategoryListView.as_view(), name='product category'),
        # path('<str:category>/', ProductCategoryListView.as_view(), name='product category'),
        path('<int:pk>/like/', ToggleLikeView.as_view(), name='toggle_like'),
        path('details/<int:pk>/', ProductDetailsView.as_view(), name='product details'),
        path('edit/<int:pk>/', ProductEditView.as_view(), name='product edit'),
    ])),
]
