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
def product(request):
      return FileResponse('templates/product.html')
def kvp(request):
      return FileResponse('templates/kvp.html')


if __name__ == '__main__':
    with Configurator() as config:

           # Adds different routes possible in the website
            config.add_route('main', '/')
            config.add_route('product', '/productinfo')
            config.add_route('kvp', '/kvp')
            # Directs the route to the function that can generate the view
            config.add_view(hello_world, route_name='main')
            config.add_view(product, route_name='product')
            config.add_view(kvp, route_name='kvp')
            config.add_static_view(name='/', path='./public', cache_max_age=3600)
            # This is the overall compiled app with the given configurations
            app = config.make_wsgi_app()

    # This line is used to start serving on port 6543 on the localhost
    server = make_server('0.0.0.0', 6000, app)
    server.serve_forever()