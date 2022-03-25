from . import views
from django.urls import path

urlpatterns = [
    path("", views.landing_page, name="home"),
    path("article-list/", views.ArticleList.as_view(), name="article_list"),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('like/<slug:slug>/',
         views.ArticleLike.as_view(), name='article_like'),
]
