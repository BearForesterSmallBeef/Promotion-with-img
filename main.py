from flask import Flask, url_for

app = Flask(__name__)


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
            <div class="alert alert-info" role="alert">Человечество вырастает из детства.<br>
            Человечеству мала одна планета.<br>
            Мы сделаем обитаемыми безжизненные пока планеты.<br>
            И начнем с Марса!<br>
            Присоединяйся!</div>
        </body>
        </html>
        '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
