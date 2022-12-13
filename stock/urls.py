from django.urls import path
from . import views

app_name = 'stock'
urlpatterns = [
    path('', views.StockTopView.as_view(), name='index'),
    path('buy/', views.StockBuy.as_view(), name='buy'),
    path('_buy/', views.stock_buy, name='buy_func'),

    path('purchase_list/', views.StockPurchaseList.as_view(), name='purchase_list'),

    # path('api/info/', views.StocokAllInfoAPI.as_view(), name='allinfo'),
    # path('api/info/buy/', views.stock_buy_api(), name='buyapi'),
    # path('api/info/<str:type_name>/', views.StockInfoAPI.as_view(), name='info'),

]
