from django.urls import path

from . import views

urlpatterns = [
    path("", views.portfolio, name="portfolio"),
    path(
        "dataanalysiswithpython/",
        views.dataanalysiswithpython,
        name="dataanalysiswithpython",
    ),
    path("genai/", views.genai, name="genai"),
    path("mldlcv/", views.mldlcv, name="mldlcv"),
    path("pythonpackages/", views.pythonpackages, name="pythonpackages"),
    path("sqlandpowerbi/", views.sqlandpowerbi, name="sqlandpowerbi"),
    path(
        "webscrapingandothers/", views.webscrapingandothers, name="webscrapingandothers"
    ),
]
