from django.urls import path
from . import views

app_name = 'gacha'

urlpatterns = [
    path('', views.gacha, name='gacha'),
    # path('complate/<int:id>/', views.market_complate, ),
    # path('result/', views.market_search_result, name='searchResult'),
    # path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    # path('<slug:c_slug>/<slug:sc_slug>', views.allProdCat, name='products_by_subcategory'),
    # path('<slug:c_slug>/<slug:sc_slug>/<slug:product_slug>/', views.ProdCatDetail, name='ProdCatDetail'),
]