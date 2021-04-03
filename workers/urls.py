from django.urls import path
from . import views

app_name = "workers"

urlpatterns = [
    path('', views.index,name='index'),
    path('upload', views.upload, name='upload'),
    path('pay-salary', views.pay_salary, name='pay_salary'),
    path('upload-salary-sheet', views.upload_salary_sheet, name='upload_salary_sheet'),
    path('proceed-to-pay', views.proceed_to_pay, name='proceed_to_pay'),
    path('pay', views.pay, name='pay'),
    path('payment-status', views.payment_status, name='payment_status'),
    path('transfers', views.transfers, name='transfers'),
    path('app', views.app, name='app'),
]