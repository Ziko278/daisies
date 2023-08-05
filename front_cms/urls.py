from django.urls import path
from front_cms.views import *

urlpatterns = [

    path('select-template', select_frontend_template_view, name='select_frontend_template'),

    path('slider/create', FrontSliderCreateView.as_view(), name='frontend_slider_create'),
    path('slider/index', FrontSliderListView.as_view(), name='frontend_slider_index'),
    path('slider/<int:pk>/edit', FrontSliderUpdateView.as_view(), name='frontend_slider_edit'),
    path('slider/<int:pk>/delete', FrontSliderDeleteView.as_view(), name='frontend_slider_delete'),

]

