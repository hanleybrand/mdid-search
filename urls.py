import haystack
from django.conf.urls import url, include, patterns
from rooibos.urls import urls

urls.append(url(r'^search/', include('haystack.urls')),)
