from flask import Flask

from common.cbl.controller.cbl_controller import cbl


def create_app():
    web_app = Flask(__name__)

    web_app.register_blueprint(cbl, url_prefix='/cbl')

    web_app.template_folder = 'templates'
    web_app.static_folder = 'static'

    web_app.config['TEMPLATES_AUTO_RELOAD'] = True

    return web_app


if __name__ == '__main__':
    app = create_app()
    app.run()
