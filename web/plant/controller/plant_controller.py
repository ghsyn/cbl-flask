from flask import Blueprint, render_template, jsonify

from common.util.data_parsing import parse_xml

blp_plant = Blueprint('plant', __name__, url_prefix='/plant')


@blp_plant.route('', methods=['GET'])
def view_page():
    return render_template('views/plant/view_power.html')


@blp_plant.route('', methods=['POST'])
def get_data():
    data = parse_xml('./static/data/khnp.xml', 'body')
    if data is None:
        return jsonify(result='FAIL', data=data)
    else:
        return jsonify(result='OK', data=data)
