from django.urls import path
from . import views

#urlpatterns為Django框架定義的關鍵字，所以命名必須一模一樣
#urlpatterns是一個串列(List)，也就是說，一個應用程式(APP)可以根據不同的頁面，各自設定不同的網址型式。
urlpatterns = [
    path('callback', views.callback)
]