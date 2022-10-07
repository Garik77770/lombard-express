from django.urls import path
from blog import views
from blog.views import (PostDetailView,
                        PostUpdateView,
                        PostDeleteView,
                        UserPostListView,
                        PostCreateView,
                        )

urlpatterns = [path('', views.PostListView.as_view(), name='blog-home'),
               path('about/', views.about, name='blog-about'),
               path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
               path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
               path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
               path('post/new/', PostCreateView.as_view(), name='post-create'),
               path('user/<username>/', UserPostListView.as_view(), name="user-posts"),
               path('equipment/', views.equipment, name='equipment'),
               path('forms/', views.forms, name='forms'),
               path('price_list', views.price_list, name='price_list'),
               path('auto_price', views.auto_price, name='auto_price'),
               path('modal', views.modal, name='modal'),
               path('appliances', views.appliances, name='appliances'),

               ]
