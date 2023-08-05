from django.urls import path
from admin_dashboard.views import *

urlpatterns = [
    path('', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('site-is-under-maintenance', AdminMaintenanceView.as_view(), name='maintenance_view'),

]

