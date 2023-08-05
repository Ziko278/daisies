from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from front_cms.views import *

urlpatterns = [
    # path('', include('front_cms.urls')),
    path('myadmin/', include('admin_dashboard.urls')),
    path('myadmin/student/', include('student.urls')),
    path('myadmin/communication/', include('communication.urls')),
    path('myadmin/attendance/', include('attendance.urls')),
    path('myadmin/examination/', include('exam.urls')),
    path('myadmin/finance/', include('finance.urls')),
    path('myadmin/front-cms/', include('front_cms.urls')),
    path('myadmin/library/', include('library.urls')),
    path('myadmin/inventory/', include('inventory.urls')),
    path('myadmin/result/', include('result.urls')),
    path('portal/student/', include('student_portal.urls')),
    path('portal/parent/', include('parent_portal.urls')),
    path('myadmin/utility/', include('school_utility.urls')),
    path('myadmin/setting/', include('school_setting.urls')),
    path('myadmin/site/', include('user_management.urls')),
    path('myadmin/human_resource/', include('human_resource.urls')),
    path('myadmin/academic/', include('academic.urls')),
    path('admin/', admin.site.urls),

    path('', HomePageView.as_view(), name='homepage'),
    path('about-us', AboutPageView.as_view(), name='about'),
    path('contact-us', ContactPageView.as_view(), name='contact_us'),
    path('our-staff', StaffPageView.as_view(), name='our_staff'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
