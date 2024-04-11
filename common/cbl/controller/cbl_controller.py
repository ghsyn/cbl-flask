import flask
from flask import Blueprint, render_template

from common.util.db_util import DBManager

cbl = Blueprint('cbl', __name__)

db = DBManager()


@cbl.route('/', methods=['GET'])
def get_dr_use_hist60():
    result = db.select_for_date_format('dr_use_hist60', HIST_TIME='%Y-%m-%d %T', DELT_VAL=None)
    return render_template('index.html', data=result)

# @app.route('/')
# def hello_world():  # put application's code here
#     return render_template('index.html', data=result)
#
#
# @app.route('/drawChart', methods=['POST'])
# def draw_chart():
#     print(request.json)
#     print('draw chart')
#     return jsonify(result)