from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^control/event/(?P<organizer>[^/]+)/(?P<event>[^/]+)/shapdfoutput/editor/$', views.EditorView.as_view(),
        name='editor'),
    url(r'^control/event/(?P<organizer>[^/]+)/(?P<event>[^/]+)/shapdfoutput/editor/webfonts.css',
        views.FontsCSSView.as_view(),
        name='css'),
    url(r'^control/event/(?P<organizer>[^/]+)/(?P<event>[^/]+)/shapdfoutput/editor/(?P<filename>[^/]+).pdf$',
        views.PdfView.as_view(), name='shapdf'),
]
