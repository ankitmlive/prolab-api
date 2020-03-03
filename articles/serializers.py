from rest_framework import serializers
from articles.models import Article

post_detail_url = serializers.HyperlinkedIdentityField(view_name='article-detail', lookup_field='slug')

class ArticleListSerializer(serializers.ModelSerializer):
    url = post_detail_url
    #user = UserDetailSerializer(read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title', 'url', 'slug', 'content', 'created_at', 'updated_at',)

class ArticleCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = fields = ('title',  'content', 'created_at')

class ArticleDetailSerializer(serializers.ModelSerializer):
    url = post_detail_url
    #user = UserDetailSerializer(read_only=True)
    #image = SerializerMethodField()
    #html = SerializerMethodField()
    #comments = SerializerMethodField()
    class Meta:
        model = Article
        fields = ['url', 'id', 'title', 'slug', 'content',]
        #fields = ['url', 'id', 'user', 'title', 'slug', 'content', 'html', 'publish', 'image', 'comments',]

    # def get_html(self, obj):
    #     return obj.get_markdown()

    # def get_image(self, obj):
    #     try:
    #         image = obj.image.url
    #     except:
    #         image = None
    #     return image

    # def get_comments(self, obj):
    #     c_qs = Comment.objects.filter_by_instance(obj)
    #     comments = CommentSerializer(c_qs, many=True).data
    #     return comments
