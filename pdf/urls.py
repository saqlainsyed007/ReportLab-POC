from django.conf.urls import url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'ReportLabGeneratePDF.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^create/', views.generate_pdf)
]
