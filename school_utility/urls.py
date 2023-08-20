from django.urls import path
from school_utility.views import *

urlpatterns = [

    path('hostel/create', HostelCreateView.as_view(), name='hostel_create'),
    path('hostel/index', HostelListView.as_view(), name='hostel_index'),
    path('hostel/<int:pk>/detail', HostelDetailView.as_view(), name='hostel_detail'),
    path('hostel/<int:pk>/edit', HostelUpdateView.as_view(), name='hostel_edit'),
    path('hostel/<int:pk>/hostel-rep/edit', HostelRepUpdateView.as_view(), name='hostel_rep_edit'),
    path('hostel/<int:pk>/delete', HostelDeleteView.as_view(), name='hostel_delete'),

    path('hostel/room/create', HostelRoomCreateView.as_view(), name='hostel_room_create'),
    path('hostel/room/index', HostelRoomListView.as_view(), name='hostel_room_index'),
    path('hostel/room/<int:pk>/detail', HostelRoomDetailView.as_view(), name='hostel_room_detail'),
    path('hostel/room/<int:pk>/edit', HostelRoomUpdateView.as_view(), name='hostel_room_edit'),
    path('hostel/room/<int:pk>/room-rep/edit', HostelRoomRepUpdateView.as_view(), name='hostel_room_rep_edit'),
    path('hostel/room/<int:pk>/delete', HostelRoomDeleteView.as_view(), name='hostel_room_delete'),


    path('hostel/bed/create', HostelBedCreateView.as_view(), name='hostel_bed_create'),
    path('hostel/bed/index', HostelBedListView.as_view(), name='hostel_bed_index'),
    path('hostel/bed/<int:pk>/detail', HostelBedDetailView.as_view(), name='hostel_bed_detail'),
    path('hostel/bed/<int:pk>/edit', HostelBedUpdateView.as_view(), name='hostel_bed_edit'),
    path('hostel/bed/<int:pk>/delete', HostelBedDeleteView.as_view(), name='hostel_bed_delete'),


    path('get-hostel-rooms', get_hostel_rooms, name='get_hostel_rooms'),
    path('get-room-beds', get_room_beds, name='get_room_beds'),

    path('transport-vehicle/create', TransportVehicleCreateView.as_view(), name='transport_vehicle_create'),
    path('transport-vehicle/index', TransportVehicleListView.as_view(), name='transport_vehicle_index'),
    path('transport-vehicle/<int:pk>/detail', TransportVehicleDetailView.as_view(), name='transport_vehicle_detail'),
    path('transport-vehicle/<int:pk>/edit', TransportVehicleUpdateView.as_view(), name='transport_vehicle_edit'),
    path('transport-vehicle/<int:pk>/delete', TransportVehicleDeleteView.as_view(), name='transport_vehicle_delete'),

    path('transport-route/create', TransportRouteCreateView.as_view(), name='transport_route_create'),
    path('transport-route/index', TransportRouteListView.as_view(), name='transport_route_index'),
    path('transport-route/<int:pk>/detail', TransportRouteDetailView.as_view(), name='transport_route_detail'),
    path('transport-route/<int:pk>/edit', TransportRouteUpdateView.as_view(), name='transport_route_edit'),
    path('transport-route/<int:pk>/delete', TransportRouteDeleteView.as_view(), name='transport_route_delete'),

    path('transport-path/create', TransportPathCreateView.as_view(), name='transport_path_create'),
    path('transport-path/<int:pk>/edit', TransportPathUpdateView.as_view(), name='transport_path_edit'),
    path('transport-path/<int:pk>/delete', TransportPathDeleteView.as_view(), name='transport_path_delete'),

    path('utility-info', SchoolUtilitySettingView.as_view(), name='utility_info'),
    path('utility-info/create', SchoolUtilitySettingCreateView.as_view(), name='utility_info_create'),
    path('utility-info/<int:pk>/update', SchoolUtilitySettingUpdateView.as_view(), name='utility_info_update'),

    path('dashboard', UtilityDashboardView.as_view(), name='utility_dashboard'),
]

