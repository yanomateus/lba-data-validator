from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='data', renderer='../templates/data.jinja2')
def data_view(request):

    return {'name': 'moisés'}
