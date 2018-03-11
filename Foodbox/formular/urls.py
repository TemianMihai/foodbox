from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^lose_weigth', views.formular1, name="form1"),
    url(r'^balanced_eating', views.formular2, name="form2"),
    url(r'^mass_building', views.formular3, name="form3"),
    url(r'^sport_program', views.formular4, name="form4"),
    url(r'^vegetarian_food', views.formular5, name="form5")
]