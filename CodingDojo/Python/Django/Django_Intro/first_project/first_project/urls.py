from django.conf.urls import url, include	# added an import!
# from django.contrib import admin              # comment out, or just delete
urlpatterns = [
    url(r'^', include('apps.first_app.urls')),	# use your app_name here
    # url(r'^admin/', admin.sites.urls)         # comment out, or just delete
]
