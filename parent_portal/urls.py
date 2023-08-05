from django.urls import path
from parent_portal.views import *


urlpatterns = [
    path('dashboard', ParentDashboardView.as_view(), name='parent_dashboard'),

]

