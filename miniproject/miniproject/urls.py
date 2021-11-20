"""miniproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gallary import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login),
    url(r'^login/index/(?P<pk>\d+)$',views.index,name='index'),
    # url(r'^return_home/(?P<pk>\d+)$',views.index,name='index'),
    url(r'^$',views.index,name='index'),
    url(r'^$',views.login,name='user_logout'),
    path('user_login/',views.user_login),
    # url(r'^addto_cart/(?P<prod>\w+)/(?P<cust>\w+)/(?P<cat>\w+)$', views.addto_cart, name='addto_cart'),
    # url(r'^show_cart2/(?P<cust>\w+)$', views.show_cart2, name='show_cart2'),
    # url(r'^delete_product/(?P<pk>\d+)/(?P<cust>\w+)$', views.delete_product, name='delete_product'),
    # url(r'^place_order/(?P<cust>\w+)$', views.place_order, name='place_order'),
    url(r'^return_home/(?P<pk>\d+)$',views.return_home,name='return_home'),
    url(r'^user_profile/(?P<pk>\d+)$',views.user_profile,name='user_profile'),
    url(r'^image_view/', views.image_view, name = 'image_view'),
    url(r'^send_mail/(?P<pk>\d+)$', views.contactView, name = 'contactView'),
    url(r'^send_mail/', views.contactView, name = 'contactView'),
    url(r'^success', views.success, name = 'success'),
    url(r'^mailsent', views.mailsent, name = 'mailsent'),
    url(r'^search', views.search, name = 'search'),
    
]

# from django.conf import settings
# from django.conf.urls.static import static
# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,
#                               document_root=settings.MEDIA_ROOT)

# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# else:
#     urlpatterns += staticfiles_urlpatterns()
from . import  settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
 
# urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)