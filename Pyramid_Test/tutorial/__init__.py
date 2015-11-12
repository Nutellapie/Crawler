from pyramid.config import Configurator
from pyramid_zodbconn import get_connection

from .resources import bootstrap

def root_factory(request):
    conn = get_connection(request)
    return bootstrap(conn.root())

def main(global_config, **settings):
    config = Configurator(settings=settings, root_factory=root_factory)
    config.add_route('home', '/home')
    config.include('pyramid_chameleon')
    config.add_route('contact', '/contact')
    config.add_route('sucursale', '/sucursale')
    config.add_route('detalii', '/detalii')
    config.add_route('test_2', '/test_2')
    config.add_route('test','/test')
    config.add_static_view(name = 'templates', path = 'tutorial:templates')
    config.add_static_view(name = 'resurse', path = 'tutorial:resurse')

    config.scan()
    return config.make_wsgi_app()
