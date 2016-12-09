from pyramid.view import view_config


def getLightState():
    pass

def writeLightState():
    pass

@view_config(route_name='home', renderer='templates/lights.jinja2')
def my_view(request):

    #handle light state
    if request.method == "POST":
        #handle light state
        state = getLightState()
        return {"types": type(request.POST.items())}
    else:
        # GET
        #return light state
        return {}
