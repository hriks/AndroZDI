from flask import Flask, flash, redirect, render_template, request, url_for
import filters
import db

app = Flask(__name__, static_url_path='')
app.secret_key = 'random string'


@app.route("/")
def hello():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'Deepak' or \
           request.form['password'] != 'Deepak':
            error = 'Invalid username or password \
            Combination. Please try again!'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))

    return render_template('login.html', error=error)


@app.route("/")
@app.route("/status")
def status_train():
    error = None
    data = None
    if 'trainno' in request.args and 'date' in request.args:
        trainno = request.args.get('trainno')
        date = request.args.get('date')
        print 'date is', date
        print 'Train no is ', trainno
        data = filters.filter_status(trainno, date)
        print type(data), data, len(data)
        return render_template('q/status.html', error=error, data=data)
    else:
        return render_template('q/status.html')


@app.route("/")
@app.route("/route")
def route_train():
    error = None
    data = None
    if 'train' in request.args:
        train = request.args.get('train')
        print 'Train no ', train
        data = filters.route_train(train)
        print type(data), data, len(data)
        return render_template('q/route.html', error=error, data=data)
    else:
        return render_template('q/route.html')


@app.route("/")
@app.route("/seat")
def load_seats():
    error = None
    data = None
    if 'traine' in request.args and 'src' in request.args\
            and 'dest' in request.args and 'datee' in request.args\
            and 'quota' in request.args and 'clas' in request.args:
        traine = request.args.get('traine')
        src = request.args.get('src')
        dest = request.args.get('dest')
        datee = request.args.get('datee')
        quota = request.args.get('quota')
        clas = request.args.get('clas')
        data = filters.filter_seat(traine, src, dest, datee, quota, clas)
        print type(data), data, len(data)
        return render_template('q/seat.html', error=error, data=data)
    else:
        return render_template('q/seat.html')


@app.route("/")
@app.route("/pnr")
def load_pnr():
    error = None
    data = None
    if 'pnr' in request.args:
        pnr = request.args.get('pnr')
        data = filters.filter_pnr(pnr)
        print type(data), data, len(data)
        return render_template('q/pnr.html', error=error, data=data)
    else:
        return render_template('q/pnr.html')


@app.route('/login')
def index():
    return render_template('index.html')


@app.route('/contact')
def inde():
    return render_template('contactus.html')


@app.route("/contact_sub", methods=['POST'])
def contact():
    data = db.insert_catagories(request.form['email'], request.form[
                                'Phone'], request.form['message'])
    print data
    flash('SUBMITTED SUCCESSFULLY')
    return render_template('contactus.html', dataformalert="true")


@app.route('/aajtak')
def aajtak():
    return render_template('aajtak.html')


@app.route('/bollywood')
def bollywood():
    return render_template('bollywood.html')


@app.route('/music')
def music():
    return render_template('music.html')


@app.route('/besties')
def besties():
    return render_template('besties.html')


@app.route('/dk')
def dk():
    return render_template('dk.html')


@app.route('/main')
def log():
    return render_template('login.html')


@app.route('/running?Status')
def status():
    return render_template('status.html')


@app.route('/train_route?')
def rout():
    return render_template('route.html')


@app.route('/pnr?query')
def pnra():
    return render_template('pnr.html')


@app.route('/seatt')
def seata():
    return render_template('seat.html')


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404


@app.errorhandler(500)
def special_exception_handler(error):
    return ' Unuthorized Database connection failed', 500


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8086, debug=True)
