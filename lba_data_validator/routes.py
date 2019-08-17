def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/home')
    def home_view(request):
        return {'status': 'ok'} 
    config.add_view(home_view, name='home_view', route_name='home', renderer='json')
