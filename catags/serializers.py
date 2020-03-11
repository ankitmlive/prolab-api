from rest_framework import serializers
from catags.models import CaTag

catag_detail_url = serializers.HyperlinkedIdentityField(view_name='catag-detail', lookup_field='catag_slug')


class CaTagSerializer(serializers.ModelSerializer):
    url = catag_detail_url
    class Meta:
        model = CaTag
        fields = ('catag_name', 'catag_slug', 'url')

class CaTagCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaTag
        fields = ('catag_name', 'catag_slug')

class CaTagDetailSerializer(serializers.ModelSerializer):
    url = catag_detail_url
    class Meta:
        model = CaTag
        fields = ('url', 'catag_name', 'catag_slug')