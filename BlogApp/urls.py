
from django.urls import path
from . views import AddCategoryView, AddPostView, ArticleDetailView, CategoryView, DeletePostView, HomeView, LikeView, UpdatePostView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('addpost/', AddPostView.as_view(), name='add-post'),
    path('addcat/', AddCategoryView.as_view(), name='add-cat'),
    path('artcile/edit/<int:pk>', UpdatePostView.as_view(), name="update-post"),
    path('artcile/<int:pk>/delete', DeletePostView.as_view(), name="delete-post"),
    path('category/<str:cats>', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like-post'),
]
