from django.conf.urls import url

from ubertool_app.docs.views import DocsRootView, serve_docs

urlpatterns = [
    url(r'^$', DocsRootView.as_view(), name='docs_root'),
    url(r'^(?P<path>.*)$', serve_docs, name='docs_files')
]
