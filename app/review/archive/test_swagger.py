from flask import Flask, request, render_template
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__,
            static_folder='dist',
            template_folder='templates')


SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'http://petstore.swagger.io/v2/swagger.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

# Register blueprint at URL
# (URL must match the one given to factory function above)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/test')
def test_return_json():
    return '''

    '''

@app.route('/display/<project_name>')
def display(project_name):
    if project_name == 'tegar':
        app_name = "Tegar File"
        api_url = 'http://petstore.swagger.io/v2/swagger.json'
    else:
        app_name = "Not Tegar File"
        api_url = 'http://localhost:5000/test'

    default_config = {
        'dom_id': '#swagger-ui',
        'url': api_url,
        'layout': 'StandaloneLayout'
    }

    fields = {
        'app_name': app_name,
        'config_json': default_config
    }

    return render_template('index.template.html', **fields)

app.run(debug=True)

# Now point your browser to localhost:5000/api/docs/