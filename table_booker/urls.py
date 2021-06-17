from django.urls import path

from . import views

# from present directory (table_booker) import views
# from .. implies a folder outside present folder

app_name = "table_booker"

urlpatterns = [
    path("", views.home_page, name="home"),
    # for a naked request, go into views and find a function called home_page - referenced as 'home'
    path("login", views.login_page, name="login"),
    path("logout", views.logout_page, name="logout"),
    path("signup", views.signup_page, name="signup"),
    path(
        "book-restaurant/<int:restaurant_id>",
        views.book_restaurant,
        name="book-restaurant",
    ),
    path("my-bookings", views.my_bookings, name="my-bookings"),
]
