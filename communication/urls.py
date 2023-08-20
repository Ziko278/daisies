from django.urls import path
from communication.views import *

urlpatterns = [

    path('smtp-configuration/create', SMTPConfigurationCreateView.as_view(), name='smtp_configuration_create'),
    path('smtp-configuration/index', SMTPConfigurationListView.as_view(), name='smtp_configuration_index'),
    path('smtp-configuration/<int:pk>/edit', SMTPConfigurationUpdateView.as_view(), name='smtp_configuration_edit'),
    path('smtp-configuration/<int:pk>/delete', SMTPConfigurationDeleteView.as_view(), name='smtp_configuration_delete'),

    path('sms-configuration/create', SMSConfigurationCreateView.as_view(), name='sms_configuration_create'),
    path('sms-configuration/index', SMSConfigurationListView.as_view(), name='sms_configuration_index'),
    path('sms-configuration/<int:pk>/edit', SMSConfigurationUpdateView.as_view(), name='sms_configuration_edit'),
    path('sms-configuration/<int:pk>/delete', SMSConfigurationDeleteView.as_view(), name='sms_configuration_delete'),

    path('message/create', MessageCreateView.as_view(), name='message_create'),
    path('message/index', MessageListView.as_view(), name='message_index'),
    path('message/<int:pk>/edit', MessageUpdateView.as_view(), name='message_edit'),
    path('message/<int:pk>/detail', MessageDetailView.as_view(), name='message_detail'),
    path('message/<int:pk>/delete', MessageDeleteView.as_view(), name='message_delete'),

    path('email/send', send_email, name='send_email'),
    path('email/user-account-auto-send', send_user_account_auto_mail, name='user_account_auto_mail'),
    path('email/fee-reminder-auto-send', send_fee_reminder_auto_mail, name='fee_reminder_auto_mail'),

    path('communication-info', CommunicationSettingView.as_view(), name='communication_info'),
    path('communication-info/create', CommunicationSettingCreateView.as_view(), name='communication_info_create'),
    path('communication-info/<int:pk>/update', CommunicationSettingUpdateView.as_view(), name='communication_info_update'),

]

