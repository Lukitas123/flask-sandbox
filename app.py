from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

post = []

@app.route("/")
def index():
    return render_template('index.html', posts=post)

@app.route("/new_post", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')
        date = datetime.now().strftime("%Y-%m-%d")

        post.append({
            "id": str(len(post) + 1),
            "title": title,
            "author": author,
            "content": content,
            "date": date
        })
        return redirect(url_for('index'))
    return render_template('new_post.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)