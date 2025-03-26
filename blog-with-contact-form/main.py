from flask import Flask, render_template
import requests
from flask import request
# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
            username = request.form['name']
            password = request.form['message']
            email = request.form['email']
            phone = request.form['phone']
            print(username, password, email, phone)
            success_message = "Successfully sent your message!"
            # return f'<h1>Successfully sent your message!<br>'
            # return f'<h1>Successfully sent your message!<br>Username: {username}, Password: {password}, </h1>'
    return render_template('contact.html', success_message = success_message)

# , name = username

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
