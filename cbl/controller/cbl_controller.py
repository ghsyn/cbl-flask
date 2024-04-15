from flask import Blueprint, render_template, request, jsonify

from cbl.service.cbl_service import CBlService

cbl = Blueprint('cbl', __name__, url_prefix='/cbl')

cbl_service = CBlService()


@cbl.route('/', methods=['GET'])
def view_page():
    return render_template('index.html')


@cbl.route('/searchDtm', methods=["POST"])
def get_cbl_as_date():
    res = cbl_service.get_cbl_as_date(request.get_json())
    return jsonify(result='SUCCESS', datas=res)


@cbl.route('/setHistory', methods=["POST"])
def set_history():
    res = cbl_service.set_hist_data(request.get_json())
    if res > 0:
        return jsonify(result='SUCCESS', count=res)
    else:
        return jsonify(result='FAIL')

# @cbl.route('/setData', methods=["POST"])
# def set_data():

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
