from dataissues.core import app
from dataissues.api import api

app.register_blueprint(api, url_prefix='/api/1')

if  __name__ == "__main__":
    app.run(port=5009)
