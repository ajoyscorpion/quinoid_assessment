from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='allBlogs'),
    path('addBlog',views.newBlog,name='addBlogs'),
    path('blogDetails/<int:pk>/',views.blogDetails,name='blogDetails'),
    path('blogDetails/<int:pk>/edit/', views.blogEdit, name='blogEdit'),
    path('blogDetails/<int:pk>/delete/', views.blogDelete, name='blogDelete'),
    path('register',views.register,name='register'),
    path('signIn',views.signIn,name='signIn'),
    path('logout',views.logout_view,name='logout')
]