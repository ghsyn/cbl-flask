from flask import Blueprint, render_template, request, jsonify

from common.util.log_util import LogUtil
from web.cbl.service.cbl_service import CBlService

cbl = Blueprint('cbl', __name__, url_prefix='/cbl')
cbl_service = CBlService()
logger = LogUtil(__name__).make_logger()


@cbl.route('/', methods=['GET'])
def view_page():
    return render_template('views/cbl/index.html')


@cbl.route('/searchDtm', methods=["POST"])
def get_cbl_as_date():

    res = cbl_service.get_cbl_as_date(request.get_json())
    if res is None:
        logger.info('cbl value is empty')
        return jsonify(result='FAIL')
    else:
        # 차트용 데이터 형식으로 변환
        keys = res[0].keys()
        tmp = res
        chart = {}
        for k in keys:
            chart.update({k: [tmp[i][k] for i, v in enumerate(tmp)]})

        ret = {
            'result': 'SUCC',
            'grid': res,
            'chart': chart
        }
        return jsonify(ret)


@cbl.route('/setHistory', methods=["POST"])
def set_history():
    res = cbl_service.set_hist_data(request.get_json())
    if res > 0:
        return jsonify(result='SUCCESS', count=res)
    else:
        return jsonify(result='FAIL')
