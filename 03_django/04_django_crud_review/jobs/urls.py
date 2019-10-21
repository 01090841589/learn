from django import urls
from . import views

app_name = 'jobs'

urlpatterns = {
    path('', jobs.index, name='index'),
    path('/past_job/', jobs.past_job, name='past_job'),
}