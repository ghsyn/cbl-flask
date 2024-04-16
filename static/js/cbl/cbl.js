let grid = null;

$(function () {
    initComponents();
    initParams();
    initDatas();
})

function initComponents() {
    document.getElementById("commandDate").value = new Date().format("yyyy-MM-dd");
}

function initParams() {}

function initDatas() {}

function shiftDate(v) {
    let date = new Date($("#commandDate").val());

    if (v === '<') {
        date.setDate(date.getDate() - 1);
    }
    if (v === '>') {
        date.setDate(date.getDate() + 1);
    }

    document.getElementById("commandDate").valueAsDate = date;

    if (date.format("yyyy-MM-dd") >= new Date().format("yyyy-MM-dd")) {
        document.getElementById('afterBtn').disabled = true;
    } else if (date.format("yyyy-MM-dd") < new Date().format("yyyy-MM-dd")) {
        document.getElementById('afterBtn').disabled = false;
    }
}

function btnSearch(v, req) {
    if (v === '오늘' || v === '검색') {
        request('/cbl/searchDtm', 'POST', {'command_date': req})
            .then(function (res) {
                if (res['result'] === 'FAIL') {
                    alert("Data Unsaved")
                } else {
                    drawChart(v + ": " + req, res.chart)
                    drawGrid(res.grid)
                }
            }).catch(function (err) {
            alert("request 오류 발생")
            console.log(err)
        })
    } else if (v === '최근') {
        alert('최근')
    }
}

/**
 * 차트 그리는 함수
 * val 형식
 * {
 *    'CBL_TIME': ['yyyy-mm-dd 00:00:00', 'yyyy-mm-dd 01:00:00', 'yyyy-mm-dd 02:00:00', ... ],
 *    'MID610': [x.xx, x.xx, x.xx, ...],
 *    ...
 * }
 * @param title 버튼명: yyyy-mm-dd
 * @param val
 */
function drawChart(title, val) {

    let mid610 = {
        x: val['CBL_TIME'],
        y: val['MID610'],
        mode: 'lines+markers',
        name: 'MID610'
    };

    let mid46 = {
        x: val['CBL_TIME'],
        y: val['MID46'],
        mode: 'lines+markers',
        name: 'MID46'
    };

    let mid810 = {
        x: val['CBL_TIME'],
        y: val['MID810'],
        mode: 'lines+markers',
        name: 'MID810'
    };

    let data = [mid610, mid46, mid810];

    let layout = {
        title: title,
        xaxis: {
            title: 'command datetime'
        },
        yaxis: {
            title: 'cbl values'
        }
    };

    Plotly.newPlot('cblChart', data, layout);
}

/**
 * 그리드 그리는 함수
 * @param data
 */
function drawGrid(data) {
    if (grid == null) {
        grid = new tui.Grid({
            el: document.getElementById('cblGrid'),
            columns: [
                {header: 'datetime', name: 'CBL_TIME'},
                {header: 'MID610', name: 'MID610'},
                {header: 'MID46', name: 'MID46'},
                {header: 'MID810', name: 'MID810'},
            ]
        });
    }
    grid.resetData(data);
}