from pyramid.view import view_config

import simplejson as json

def getLightState():
    with open('/home/ec2-user/lightstate', 'rb') as lights:
        return json.load(lights)

def writeLightState(state):
    with open('/home/ec2-user/lightstate', 'rb') as lights:
        return json.dump(state, lights)

@view_config(route_name='home', renderer='templates/lights.jinja2')
def my_view(request):

    #handle light state
    if request.method == "POST":
        #handle light state
        state = getLightState()

        lights = request.POST
        for light in lights.keys():
            state[light] = lights[light]

        #save state
        writeLightState(state)

        return {"state": state}
    else:
        # GET
        #return light state
        return {'lights': getLightState()}
