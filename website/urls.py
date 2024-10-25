from . import views
from django.urls import path

urlpatterns = [
    path("",views.index,name="index"),
    path("register",views.register,name="register"),
    path("login",views.login_user,name="login"),
    path("logout",views.logout_truc,name="logout"),
    path("articles",views.articles,name="articles"),
    path("article/new",views.create_article,name="new_article"),
    path("article/<int:id>",views.get_article,name="showArticle"),
    path("article/edit/<int:id>",views.edit_article,name="editArticle"),
    path("article/remove/<int:id>",views.delete_article,name="removeArticle"),
]