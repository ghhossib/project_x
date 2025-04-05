from flask import Flask, render_template, request, redirect, session

# создать объект класса Flas
application = Flask(__name__)
application.secret_key = "BOOM"
# это объект управляет авторизацией




@application.route('/', methods=['GET','POST'])

def test():
        title = "Test"
        return render_template('123.html',
                               title=title)
@application.route('/test', methods=['GET','POST'])

def test1():
        title = "Test228"
        return render_template('123.html',
                               title=title)


if __name__ == "__main__":
    application.run(debug=True)