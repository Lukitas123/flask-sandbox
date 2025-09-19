from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = [
    {"id": "1", "title": "Primer Post", "author": "Florian", "content": "¡Hola mundo!", "date": "2025-09-18"}
]   

@app.route("/")
def home():
    return render_template('index.html', posts=posts)

@app.route("new-post", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')
        date = "Aca hay que poner algo para la fecha actual"
        posts.apend({
            "id": str(len(posts)),
            "title": title,
            "author": author,
            "content": content,
            "date": date
        })
        return redirect(url_for('index'))
    return render_template('new_post.html')


if __name__ == "__main__":
    app.run("localhost", 3000, debug=True)