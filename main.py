from flask import Flask, url_for, request

app = Flask(__name__)
prof = "инженер-исследователь, пилот, строитель, экзобиолог, врач," \
       " инженер по терраформированию, климатолог, специалист по радиационной защите," \
       " астрогеолог, гляциолог, инженер жизнеобеспечения, метеоролог, оператор марсохода," \
       " киберинженер, штурман"
professions = "".join([f"""<div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="{i}">
                                          <label class="form-check-label" for="{i}">{i}</label>
                                          </div>""" for i in prof.split(",")])
professions_request = []


@app.route("/")
def main_menu():
    return \
        f'''
        <h1>Миссия Колонизация Марса</h1>
        <ol>
        <li><a href="http:\\promotion">Promotion</a>
        <li><a href="http:\\index">Index</a>
        <li><a href="http:\\image_mars">Image of mars</a> 
        <li><a href="http:\\promotion_image">Promotion with image</a> 
        <li><a href="http:\\astronaut_selection">Astronaut selection</a> 
        <li><a href="http:\\choice\\Марс">Choice</a> 
        </ol>
        '''


@app.route("/index")
def index():
    return f"""<h1>И на Марсе будут яблони цвести!</h1>"""


@app.route("/promotion")
def promotion():
    return \
        f"""
        <div>Человечество вырастает из детства.<br>
        Человечеству мала одна планета.<br>
        Мы сделаем обитаемыми безжизненные пока планеты.<br>
        И начнем с Марса!<br>
        Присоединяйся!</div>"""


@app.route("/image_mars")
def image_mars():
    return \
        f'''
        <title>Привет, Марс!</title>
        <h1>Жди нас, Марс!</h1>
        <img src={url_for('static', filename='/img/Mars.jpg')} alt="Марс сломался :(" align="middle" 
        height=350 width=500>
        <div>Вот она какая, красная планета</div>
        '''


@app.route("/promotion_image")
def promotion_image():
    return \
        f'''
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='/css/style.css')}">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" 
            integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" 
            crossorigin="anonymous">
            <link rel="stylesheet">
            <title>Привет, Марс!</title>
        </head>
        <body>
            <h1>Жди нас, Марс!</h1>
            <img src={url_for('static', filename='/img/Mars.jpg')} alt="Марс сломался :(" align="middle" 
            height=350 width=500>
            <div class="alert alert-light" role="alert">Вот она какая, красная планета</div>
            <div class="alert alert-secondary" role="alert">Человечество вырастает из детства.</div>
            <div class="alert alert-success" role="alert">Человечеству мала одна планета.</div>
            <div class="alert alert-secondary" role="alert">Мы сделаем обитаемыми безжизненные пока планеты.</div>
            <div class="alert alert-warning" role="alert">И начнем с Марса!</div>
            <div class="alert alert-danger" role="alert">Присоединяйся!</div>
        </body>
        </html>
        '''


@app.route("/astronaut_selection")
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style2.css')}" />
                                <title>Отбор астранавтов</title>
                              </head>
                              <body>
                                <h1 align="center">Анкета претендента</h1>
                                <h3 align="center">на участие в миссии</h3>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="name" class="form-control" id="name" placeholder="Введите свое имя" name="name">
                                        <input type="surname" class="form-control" id="surname" placeholder="Введите свою фамилию" name="surname">
                                        <br>
                                        <input type="email" class="form-control" id="email" placeholder="Введите свою электронныю почту" name="email">
                                        <br>
                                        <div class="form-group">
                                            <label for="ObrSelect">какое у вас образование:</label>
                                            <select Obr="form-control" id="ObrSelect" name="Obr">
                                              <option>Начальное</option>
                                              <option>Среднее</option>
                                              <option>Высшее</option>
                                            </select>
                                         </div>
                                         <br>
                                         <div class="form-group">
                                         <label for="form-check">Какие у Вас есть професии?</label>
                                        {professions}
                                        </div>
                                        <br>
                                        <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                        </div>
                                        <br>
                                        <div class="form-group">
                                            <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="5" name="reason"></textarea>
                                        </div>
                                        <br>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <br>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <br>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        <br>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['name'])
        print(request.form['surname'])
        print(request.form['email'])
        print(request.form['Obr'])
        map(lambda x: print(request.form[x]), professions)
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['accept'])
        return "Форма отправлена"


@app.route("/choice/<name>")
def choice(name):
    return f"""
            <!DOCTYPE html>
            <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" 
                integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" 
                crossorigin="anonymous">
                <title>Привет, {name.capitalize()}!</title>
            </head>
            <body>
                <h1>Жди нас, {name.capitalize()}!</h1>
                <div class="alert alert-light" role="alert">Мое предложение: {name.capitalize()}</div>
                <div class="alert alert-info" role="alert">
                На этой планете много необходимых ресурсов;<br>
                На ней есть небольшое магнитное поле;<br>
                Наконец, она просто красива!<br></div>
            </body>
            """


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
