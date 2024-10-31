from django.urls import path
from .views import CategoryListCreate, TagListCreateView, UserCreate, LoginView
from .views import home

app_name = 'albums'  

urlpatterns = [
    path('', home, name='home'),  
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'), 
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),  
    path('register/', UserCreate.as_view(), name='user-create'),  
    path('login/', LoginView.as_view(), name='login'),  
]
