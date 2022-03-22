from django.urls import path

from demo_app.web.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
)
