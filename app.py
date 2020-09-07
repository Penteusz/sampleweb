from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__) #tak tworzymy instancje klasy Flask
# print(__name__)  #tu __name__ == __main__, czyli to głowny plik aplikacji i tak sie ta aplikacja nazywa

#uzycie dekoratora wzbogacajacego funkcje ponizej
#tu chodzi o wyswietlenie okreslonej tresindex.htmlci dla strony glownej "/"
# @app.route('/')
# def hello_world():
#     return 'Hello, Kamil!'

#Zamiast zwykłego tekstu moge w funkcji zwrocic plik html za pomoca funkcji "render_template"
#render template zczytuje tekst w formacie html
#render_template domyslnie przeszukuje zawartość katalogu o nazwie "templates" w katalogu srodowiska wirtualnego/projektu
#wiec taki folder trzeba utworzyc i umiescic w nim pliki html

# @app.route('/')
# @app.route('/<username>')
# def hello_world(username=None):
#     return render_template("index.html", username=username)

# @app.route('/about/')
# @app.route('/about/<username>')
# def about(username=None):
#     return render_template("about.html", username=username)
#
# @app.route('/blog/')
# def blog():
#     return 'Some text!'
#
# @app.route('/blog/dogs/')
# def blog2():
#     return 'This is my dog'
#
# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)

#With added template
# @app.route('/')
# def my_home():
#     return render_template('index.html')
#
# @app.route('/index.html')
# def my_home2():
#     return render_template('index.html')
#
# # @app.route('/work.html/')
# # def my_work():
# #     return render_template('work.html')
#
# @app.route('/works.html')
# def work():
#     return render_template('works.html')
#
# @app.route('/works.html/')
# def work2():
#     return render_template('works.html')
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
# @app.route('/about.html/')
# def about2():
#     return render_template('about.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
# @app.route('/contact.html/')
# def contact2():
#     return render_template('contact.html')
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')
#
# @app.route('/components.html/')
# def components2():
#     return render_template('components.html')

#Mozna to zrobic dynamicznie tak:
@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/index.html')
def my_home2():
    return render_template('index.html')

@app.route('/<string:page_name>/')
def html_page(page_name):
    return render_template(page_name)

#Ta funkcja moze byc zapisana w innym pliku .py jako module i stamdad zaimportowana
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

#Zapis do pliku csv
def write_to_csv(data):
    with open('./database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        #utworzenie obiektu do zapisu do pliku csv
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            # email = request.form['message']
            data = request.form.to_dict()
            # print(data)
            # write_to_file(data)
            write_to_csv(data)
            return redirect('submit_form.html')
        except:
            return 'did not wite to database'
    else:
        return 'something went wrong'