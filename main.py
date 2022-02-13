from flask import Flask, url_for, request

app = Flask(__name__)
prof = "инженер-исследователь, пилот, строитель, экзобиолог, врач," \
       " инженер по терраформированию, климатолог, специалист по радиационной защите," \
       " астрогеолог, гляциолог, инженер жизнеобеспечения, метеоролог, оператор марсохода," \
       " киберинженер, штурман"
professions = "".join([f"""<div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="{i}" name="pro">
                                          <label class="form-check-label" for="{i}">{i}</label>
                                          </div>""" for i in prof.split(",")])
planets = {"Меркурий": """<div class="alert alert-light" role="alert">Ближайшая к Солнцу планета</div>
                          <div class="alert alert-success" role="alert">Её период обращения вокруг Солнца составляет всего 87,97 земных суток</div>
                          <div class="alert alert-secondary" role="alert">Ось Меркурия имеет наименьший наклон из всех планет Солнечной системы</div>
                          <div class="alert alert-warning" role="alert">Отсутствие внутренней геологической активности в последние миллиарды лет</div>
                          <div class="alert alert-danger" role="alert">Известных природных спутников у планеты нет</div>
                       """,
           "Венера": """<div class="alert alert-light" role="alert">Вторая по удалённости от Солнца планета</div>
                          <div class="alert alert-success" role="alert">Шестая по размеру планета</div>
                          <div class="alert alert-secondary" role="alert">Названа в честь древнеримской богини любви Венеры</div>
                          <div class="alert alert-warning" role="alert">Венерианский год составляет 224,7 земных суток</div>
                          <div class="alert alert-danger" role="alert">Она имеет самый длинный период вращения вокруг своей оси среди всех планет Солнечной системы и<br> вращается в направлении, противоположном направлению вращения большинства планет.</div>
                       """,
           "Земля": """<div class="alert alert-light" role="alert">Третья по удалённости от Солнца планета</div>
                          <div class="alert alert-success" role="alert">Самая плотная планета</div>
                          <div class="alert alert-secondary" role="alert">Пятая по диаметру и массе среди всех планет</div>
                          <div class="alert alert-warning" role="alert">Крупнейшая среди планет земной группы</div>
                          <div class="alert alert-danger" role="alert">Есть биосфера и мы здесь живем!</div>
                       """,
           "Марс": """<div class="alert alert-light" role="alert">Четвертая по удалённости от Солнца планета</div>
                          <div class="alert alert-success" role="alert">седьмая по размеру планета</div>
                          <div class="alert alert-secondary" role="alert">Названа в честь Марса — древнеримского бога войны</div>
                          <div class="alert alert-warning" role="alert">есть два естественных спутника</div>
                          <div class="alert alert-danger" role="alert">есть вулканы, долины, пустыни</div>
                       """,
           "Юпитер": """<div class="alert alert-light" role="alert">крупнейшая планета Солнечной системы</div>
                          <div class="alert alert-success" role="alert">пятая по удалённости от Солнца</div>
                          <div class="alert alert-secondary" role="alert">Юпитер классифицируется как газовый гигант</div>
                          <div class="alert alert-warning" role="alert">Юпитер имеет, по крайней мере, 80 спутников</div>
                          <div class="alert alert-danger" role="alert">название Юпитера происходит от имени древнеримского верховного бога-громовержца</div>
                       """,
           "Плутон": """<div class="alert alert-light" role="alert">крупнейшая известная карликовая планета Солнечной системы</div>
                          <div class="alert alert-success" role="alert">состоит в основном из камня и льда</div>
                          <div class="alert alert-secondary" role="alert">его масса меньше массы Луны примерно в шесть раз</div>
                          <div class="alert alert-warning" role="alert">Плутон считался девятой планетой Солнечной системы</div>
                          <div class="alert alert-danger" role="alert">В честь Плутона был назван химический элемент плутоний</div>
                       """,
           "Сатурн": """<div class="alert alert-light" role="alert">шестая планета по удалённости от Солнца</div>
                          <div class="alert alert-success" role="alert">вторая по размерам планета</div>
                          <div class="alert alert-secondary" role="alert">классифицируется как газовый планета-гигант</div>
                          <div class="alert alert-warning" role="alert">Сатурн назван в честь римского бога земледелия</div>
                          <div class="alert alert-danger" role="alert">В основном Сатурн состоит из водорода</div>
                       """,
           "Уран": """<div class="alert alert-light" role="alert">седьмая планета по удалённости от Солнца</div>
                          <div class="alert alert-success" role="alert">третья по диаметру и четвёртая по массе</div>
                          <div class="alert alert-secondary" role="alert">названа в честь греческого бога неба Урана</div>
                          <div class="alert alert-warning" role="alert">Уран стал первой планетой, обнаруженной в Новое время и при помощи телескопа</div>
                          <div class="alert alert-danger" role="alert">В отличие от газовых гигантов — Сатурна и Юпитера, состоящих в основном из водорода<br>
                                                                        и гелия, в недрах Урана и схожего с ним Нептуна отсутствует металлический водород, <br>
                                                                        но зато много льда в его высокотемпературных модификациях.</div>
                       """,
           "Нептун": """<div class="alert alert-light" role="alert">восьмая и самая дальняя от Солнца планета</div>
                          <div class="alert alert-success" role="alert">Его масса превышает массу Земли в 17,2 раза и является третьей среди планет Солнечной системы</div>
                          <div class="alert alert-secondary" role="alert">Планета названа в честь Нептуна — римского бога морей</div>
                          <div class="alert alert-warning" role="alert">Нептун стал первой планетой, открытой благодаря математическим расчётам</div>
                          <div class="alert alert-danger" role="alert">Нептун по составу близок к Урану, и обе планеты отличаются от более крупных планет-гигантов — Юпитера и Сатурна</div>
                       """}


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
        <li><a href="http:\\results\\_\\0\\0.0">Results</a> 
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


@app.route("/astronaut_selection", methods=['POST', 'GET'])
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
        print(f"name: {request.form.get('name')}")
        print(f"surname: {request.form.get('surname')}")
        print(f"email: {request.form.get('email')}")
        print(f"Obr: {request.form.get('Obr')}")
        print(f"prof: {request.form.get('pro')}")
        print(f"sex: {request.form.get('sex')}")
        print(f"reason: {request.form.get('reason')}")
        print(f"file: {request.form.get('file')}")
        print(f"accept: {request.form.get('accept')}")
        return """
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet"
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
            crossorigin="anonymous">
        </head>
        <body>
        <div class="alert alert-info" role="alert">Форма отправлена</div>
        </body>"""


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
                <h1>Мое предложение: {name.capitalize()}</h1>
                {planets[name.capitalize()]}
            </body>
            """


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    print(0)
    return \
        f"""
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" 
            integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" 
            crossorigin="anonymous">
            <link rel="stylesheet">
            <title>Результат</title>
        </head>
        <body>
            <h1>Результат отбора</h1>
            <h3>Претендента на участие в миссии {nickname}</h3>
            <div class="alert alert-success" role="alert">Поздравляем! Ваш рейтинг после {level} этапа отбора</div>
            <div class="alert alert-light" role="alert">составляет {rating}!</div>
            <div class="alert alert-warning" role="alert">Желаем удачи!</div>
        </body>
        </html>
        """


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
