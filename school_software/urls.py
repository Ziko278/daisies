from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', include('front_cms.urls')),
    path('', include('admin_dashboard.urls')),
    path('student/', include('student.urls')),
    path('communication/', include('communication.urls')),
    path('attendance/', include('attendance.urls')),
    path('finance/', include('finance.urls')),
    path('library/', include('library.urls')),
    path('inventory/', include('inventory.urls')),
    path('result/', include('result.urls')),
    path('portal/student/', include('student_portal.urls')),
    path('portal/parent/', include('parent_portal.urls')),
    path('utility/', include('school_utility.urls')),
    path('setting/', include('school_setting.urls')),
    path('site/', include('user_management.urls')),
    path('human_resource/', include('human_resource.urls')),
    path('academic/', include('academic.urls')),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
