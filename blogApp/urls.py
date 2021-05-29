from django.urls import path
from . import views
from .views import blog, commentpost, createpost, search, CategoryView, blogdetail


urlpatterns = [
path('', blog.as_view(), name="blog"),
path('search', search, name="search"),
path('createpost/', createpost, name="createpost"),
path('category/<str:cats>/', CategoryView, name="category"),
path('<slug:slug>/', blogdetail.as_view(), name="blog-detail"),
path('<slug:slug>/comment/',commentpost,name="comment")
]
