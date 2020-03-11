from django.urls import include, path
from django.conf.urls import url
from catags.views import CaTagList, CaTagDetail, CatagCreateAPIView

urlpatterns = [
    path('', CaTagList.as_view(), name='catag-list'),
    path('create/', CatagCreateAPIView.as_view(), name='catag-create'),
    url(r'^(?P<catag_slug>[\w-]+)/$', CaTagDetail.as_view(), name='catag-detail'),
]
