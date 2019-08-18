from lba_data_validator.views.authors import authors_view
def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/home')
    config.add_route('authors', '/authors')
    config.add_view(authors_view, route_name='authors', renderer="json")
