# Import WSGI ref for importing the serving library
from wsgiref.simple_server import make_server

# Configurator defines all the settings and configs in your web app
from pyramid.config import Configurator

# Response is used to respond to requests to the server
from pyramid.response import FileResponse

# The function is added as a view in the app.
# The response module returns the info to be shown on the webpage
def hello_world(request):
      print('Incoming request')
      return FileResponse('templates/index.html') # the HTML file to be shown
def productf(request):
      return FileResponse('templates/product.html')
def KVPf(request):
      return FileResponse('templates/KVP.html')
def uif(request):
      return FileResponse('templates/ui.html')
def iaf(request):
      return FileResponse('templates/ia.html')
def featf(request):
      return FileResponse('templates/features.html')
def interf(request):
      return FileResponse('templates/interactions.html')


if __name__ == '__main__':
    with Configurator() as config:

           # Adds different routes possible in the website
            config.add_route('main', '/')
            config.add_route('product', '/product')
            config.add_route('KVP', '/KVP')
            config.add_route('ui', '/ui')
            config.add_route('ia', '/ia')
            config.add_route('features', '/features')
            config.add_route('interactions', '/interactions')
            # Directs the route to the function that can generate the view
            config.add_view(hello_world, route_name='main')
            config.add_view(productf, route_name='product')
            config.add_view(KVPf, route_name='KVP')
            config.add_view(uif, route_name='ui')
            config.add_view(iaf, route_name='ia')
            config.add_view(featf, route_name='features')
            config.add_view(interf, route_name='interactions')
            config.add_static_view(name='/', path='./public', cache_max_age=3600)
            # This is the overall compiled app with the given configurations
            app = config.make_wsgi_app()

    # This line is used to start serving on port 6543 on the localhost
    server = make_server('0.0.0.0', 6000, app)
    server.serve_forever()