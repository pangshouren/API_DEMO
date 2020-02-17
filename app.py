from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/order_request')
def order_request():
    return render_template('order_request.html')


@app.route('/order_query')
def order_query():
    return render_template('order_query.html')


@app.route('/order_close')
def order_close():
    return render_template('order_close.html')


@app.route('/order_refund')
def order_refund():
    return render_template('order_refund.html')


@app.route('/refund_query')
def refund_query():
    return render_template('refund_query.html')


@app.route('/rate_query')
def rate_query():
    return render_template('rate_query.html')


@app.route('/native_pay')
def native_pay():
    return render_template('native_pay.html')


@app.route('/jsapi_pay')
def jsapi_pay():
    return render_template('jsapi_pay.html')


@app.route('/quick_pay')
def quick_pay():
    return render_template('quick_pay.html')


@app.route('/web_alipay')
def web_alipay():
    return render_template('web_alipay.html')


@app.route('/wap_alipay')
def wap_alipay():
    return render_template('wap_alipay.html')


@app.route('/app_pay')
def app_pay():
    return render_template('app_pay.html')


@app.route('/minipro_pay')
def minipro_pay():
    return render_template('minipro_pay.html')


@app.route('/search_text')
def search_text():
    return render_template('search_result.html')


@app.route('/pay_notify')
def pay_nofify():
    return render_template('pay_notify.html')


@app.route('/error_codes')
def error_codes():
    return render_template('error_codes.html')


@app.route('/offline_CsB')
def offline_CsB():
    return render_template('offline_CsB.html')


@app.route('/offline_BsC')
def offline_BsC():
    return render_template('offline_BsC.html')


@app.route('/online_pc')
def online_pc():
    return render_template('online_pc.html')


@app.route('/mobile_web')
def mobile_web():
    return render_template('mobile_web.html')


@app.route('/inapp')
def inapp():
    return render_template('inapp.html')


@app.route('/minipro')
def minipro():
    return render_template('minipro.html')


@app.route('/official_account')
def official_account():
    return render_template('official_account.html')


@app.route('/for_test')
def for_test():
    return render_template('for_test.html')


if __name__ == '__main__':
    app.run(debug=True)
