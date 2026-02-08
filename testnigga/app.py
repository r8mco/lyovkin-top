from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    name = None
    if request.method == "POST":
        name = request.form.get("username")
    return render_template("index.html", name=name)

@app.route("/about")
def about():
    return render_template("about.html")

projects_list = [
    {
        "title": "Личный сайт",
        "description": "Сайт на Flask с несколькими страницами, стилями и формами.",
        "link": "/",
        "status": "Готово"
    },
    {
        "title": "Контактная форма",
        "description": "Форма обратной связи с сохранением сообщений.",
        "link": "/contact",
        "status": "Готово"
    },
    {
        "title": "Будущий проект 👀",
        "description": "Скоро тут появится что-то крутое.",
        "link": "/coming_soon",
        "status": "В разработке"
    }
]

@app.route("/projects")
def projects():
    return render_template("projects.html", projects=projects_list)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    message_sent = False
    if request.method == "POST":
        email = request.form.get("email")
        message = request.form.get("message")
        # сохраняем сообщение в файл
        with open("messages.txt", "a", encoding="utf-8") as f:
            f.write(f"Email: {email}\nMessage: {message}\n---\n")
        message_sent = True
    return render_template("contact.html", message_sent=message_sent)
@app.route("/messages")
def messages():
    with open("messages.txt", "r", encoding="utf-8") as f:
        all_messages = f.read().split('---\n')
    return render_template("messages.html", messages=all_messages)
@app.route("/coming_soon")
def coming_soon():
    return render_template("coming_soon.html")

@app.route("/about_me")
def about_me():
    skills = [
        {"name": "Python", "level": 80},
        {"name": "Flask", "level": 70},
        {"name": "HTML/CSS", "level": 75},
        {"name": "JavaScript", "level": 60},
        {"name": "Git", "level": 50}
    ]
    return render_template("about_me.html", skills=skills)

@app.route("/secret")
def secret():
    return render_template("secret.html")

@app.route("/mini_chat", methods=["GET", "POST"])
def mini_chat():
    chat_messages = []
    try:
        with open("chat.txt", "r", encoding="utf-8") as f:
            chat_messages = f.read().split('---\n')
    except FileNotFoundError:
        pass

    if request.method == "POST":
        username = request.form.get("username")
        message = request.form.get("message")
        if username and message:
            with open("chat.txt", "a", encoding="utf-8") as f:
                f.write(f"{username}: {message}\n---\n")
            chat_messages.append(f"{username}: {message}")

    return render_template("mini_chat.html", messages=chat_messages)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

