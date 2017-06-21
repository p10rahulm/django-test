from django.conf.urls import url

from . import views
app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='poll_index'),
    url(r'^([0-9]+)/$', views.detail, name='poll_detail'),
    # or you can pass the regex with a name as follows
    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name='poll_results'),
    url(r'^([0-9]+)/vote$', views.vote, name='poll_vote'),
]