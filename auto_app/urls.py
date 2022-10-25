from django.urls import path

from auto_app import views, admin_views, customer_views, worksmanager_views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('products',views.products,name='products'),
    path('store',views.store,name='store'),
    path('index', views.login_view, name='index'),
    path('aaaAdmin', views.aaaAdmin, name='aaaAdmin'),
    path('login_view/', views. login_view, name='login_view'),
    path("logout_view/",views.logout_view,name='logout_view'),
    path("index1", views.index1, name='index1'),

    #admin

    path("wmregister",admin_views.worksmanager_add,name='wmregister'),
    path('worksmanager_view', admin_views.worksmanager_view, name='worksmanager_view'),
    path('delete-wm/<int:user_id>', admin_views.delete_wmmanager_view, name='delete-wm'),
    path("wm_update/<int:user_id>/",admin_views.wm_update,name='wm_update'),
    path('schedule',admin_views.schedule_add,name='schedule'),
    path('schedule_view',admin_views.schedule,name='schedule_view'),
    path('schedule_delete/<int:id>/', admin_views.schedule_delete, name='schedule_delete'),
    path('works', admin_views.works, name='works'),
    path('works_view', admin_views.works_view, name='works_view'),
    path('reply_feedback/<int:id>/',admin_views.reply_feedback,name = 'reply_feedback'),
    path('feedbacks', admin_views.feedbacks, name='feedbacks'),
    path('customerview',admin_views.customerview, name='customerview'),
    path('customer_delete/<int:user_id>', admin_views.customer_delete, name='customer_delete'),
    path('works_delete/<int:id>', admin_views.works_delete, name='works_delete'),
    # path('statusiot', admin_views.statusiot, name='statusiot'),


    #customer

    path("customer_reg",customer_views.customer_reg,name="customer_reg"),
    # path('customer-profile/<int:id>/', customer_views.customer_profile_view,name='customer-profile'),
    path("cus_home",customer_views.cus_home,name="cus_home"),
    path("schedule_cus",customer_views.schedule_cus,name="schedule_cus"),
    path('take_appointment/<int:id>/', customer_views.take_appointment, name='take_appointment'),
    path('appointments', customer_views.appointments, name='appointments'),
    path('status', customer_views.status, name='status'),
    path("feedback",customer_views.feedback,name="feedback"),
    path("feedback_view", customer_views.feedback_view, name="feedback_view"),




    #worksmanager
    path('manager_home',worksmanager_views.manager_home,name='manager_home'),
    path('appointment_admin',worksmanager_views.appointment_admin,name='appointment_admin'),
    path('approve_appointment/<int:id>/', worksmanager_views.approve_appointment, name='approve_appointment'),
    path('reject_appointment/<int:id>/', worksmanager_views.reject_appointment, name='reject_appointment'),
    path('works_view1',worksmanager_views.works_view1, name='works_view1'),
    path("wm_status/<int:id>/", worksmanager_views.wm_status, name='wm_status'),

    #chat
    path('chatview', views.chatview, name='chatview'),

]