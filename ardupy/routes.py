# TODO write method (decorator?) that takes a site map as a dictionary and
# autmoatically adds routes from that

def dynaroute(routes, appconfigurer):
    raise

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
