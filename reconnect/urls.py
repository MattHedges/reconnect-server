from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from reconnectapi.views import register_user, login_user
from django.conf.urls import include
from rest_framework import routers
from reconnectapi.views import PostView, CommentView, FriendshipView, GroupView, MembershipView, TopicView


from django.contrib import admin
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'posts', PostView, 'post')
router.register(r'comments', CommentView, 'comment')
router.register(r'friendships', FriendshipView, 'friendship')
router.register(r'groups', GroupView, 'group')
router.register(r'memberships', MembershipView, 'membership')
router.register(r'topics', TopicView, 'topic')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]