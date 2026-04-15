from django.contrib import admin
from django.urls import path
from core.views import home
from django.http import HttpResponse

robots_txt = """User-agent: *
Disallow: /admin/
Allow: /
Sitemap: https://www.altogasspa.cl/sitemap.xml
"""

sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://www.altogasspa.cl/</loc>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
</urlset>
"""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('robots.txt', lambda request: HttpResponse(robots_txt, content_type='text/plain')),
    path('sitemap.xml', lambda request: HttpResponse(sitemap_xml, content_type='application/xml')),
]
