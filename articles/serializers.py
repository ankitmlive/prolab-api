from rest_framework import serializers
from articles.models import Article
#from . import models

"""
class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Article
        fields = ('id', 'title', 'slug', 'content', 'created_at', 'updated_at',)
"""

class ArticleListSerializer(serializers.ModelSerializer):
    #url = post_detail_url
    #user = UserDetailSerializer(read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title', 'slug', 'content', 'created_at', 'updated_at',)

class ArticleCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = fields = ('title',  'content', 'created_at')


# post_detail_url = HyperlinkedIdentityField(
#         view_name='posts-api:detail',
#         lookup_field='slug'
#         )


# class PostDetailSerializer(ModelSerializer):
#     url = post_detail_url
#     user = UserDetailSerializer(read_only=True)
#     image = SerializerMethodField()
#     html = SerializerMethodField()
#     comments = SerializerMethodField()
#     class Meta:
#         model = Post
#         fields = [
#             'url',
#             'id',
#             'user',
#             'title',
#             'slug',
#             'content',
#             'html',
#             'publish',
#             'image',
#             'comments',
#         ]

#     def get_html(self, obj):
#         return obj.get_markdown()

#     def get_image(self, obj):
#         try:
#             image = obj.image.url
#         except:
#             image = None
#         return image

#     def get_comments(self, obj):
#         c_qs = Comment.objects.filter_by_instance(obj)
#         comments = CommentSerializer(c_qs, many=True).data
#         return comments
