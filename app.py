from flask import Flask
from web.cbl.controller.cbl_controller import cbl
from web.user.controller.user_controller import user


def create_app():
    web_app = Flask(__name__)
    # CORS(web_app)
    web_app.register_blueprint(cbl)
    web_app.register_blueprint(user)
    web_app.template_folder = 'templates'
    web_app.static_folder = 'static'
    web_app.config['TEMPLATES_AUTO_RELOAD'] = True
    return web_app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0')
