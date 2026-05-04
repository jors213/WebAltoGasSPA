from django.contrib import admin
from django.urls import path
from core.views import (
    home, asesoria_online,
    servicio_sello_verde, servicio_tramites_sec, servicio_proyectos,
)
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
    <url>
        <loc>https://www.altogasspa.cl/servicios/sello-verde/</loc>
        <changefreq>monthly</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>https://www.altogasspa.cl/servicios/tramites-sec/</loc>
        <changefreq>monthly</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>https://www.altogasspa.cl/servicios/proyectos-ingenieria/</loc>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://www.altogasspa.cl/asesoria-online/</loc>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
</urlset>
"""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('asesoria-online/', asesoria_online, name='asesoria_online'),
    path('servicios/sello-verde/',         servicio_sello_verde,  name='servicio_sello_verde'),
    path('servicios/tramites-sec/',        servicio_tramites_sec, name='servicio_tramites_sec'),
    path('servicios/proyectos-ingenieria/',servicio_proyectos,    name='servicio_proyectos'),

    path('robots.txt', lambda request: HttpResponse(robots_txt, content_type='text/plain')),
    path('sitemap.xml', lambda request: HttpResponse(sitemap_xml, content_type='application/xml')),
]
