from django.urls import path

from . import views

urlpatterns = [
    path("show-all-stream-info", views.show_all_stream_info, name="show_all_stream_info_command"),
    path("show-stream", views.show_stream, name="show_stream"),
]