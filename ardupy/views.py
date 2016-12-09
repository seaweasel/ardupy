from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/lights.jinj')
def my_view(request):
    return {'project': 'ardupy'}
