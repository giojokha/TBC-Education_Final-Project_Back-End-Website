from ext import app, db, login_manager
from flask import render_template, redirect, flash
from forms import RegisterForm, LoginForm, ArticleForm
from os import path
from models import Ambavi, User
from flask_login import login_user, logout_user, login_required, current_user


@app.route("/")
def home():
    ambebi = Ambavi.query.all()
    return render_template("index.html", ambebi=ambebi)

@app.route("/axali_ambebi")
def news():
    return render_template("axali_ambebi.html")

@app.route("/ekonomika")
def economics():
    return render_template("ekonomika.html")

@app.route("/kultura")
def culture():
    return render_template("kultura.html")

@app.route("/msoflio")
def world():
    return render_template("msoflio.html")

@app.route("/politika")
def politics():
    return render_template("politika.html")

@app.route("/sporti")
def sports():
    return render_template("sporti.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(form.username.data == User.username).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("წარმატებით გაიარე ავტორიზაცია")
            print(current_user)
            return redirect("/")
        else:
            flash("სახელი ან პაროლი არასწორია. სცადეთ თავიდან")
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/profile/<int:profile_id>")
def profile(profile_id):
    return render_template("profile.html", profiles=profiles[profile_id])


@app.route("/register", methods=["get", "post"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)

        db.session.add(new_user)
        db.session.commit()
        flash("მადლობა დარეგისტრირებისთვის! ახლა შეგიძლიათ გაიაროთ ავტორიზაცია")

        return redirect("/login")

    return render_template("register.html", form=form)

@app.route("/add_article", methods=["GET", "POST"])
@login_required
def add_article():
    form = ArticleForm()
    if form.validate_on_submit():
        axali_ambavi = Ambavi(news_title=form.news_title.data, Date=form.Date.data)

        image = form.image.data
        directory = path.join(app.root_path, "static", "imagess", image.filename)
        image.save(directory)
        axali_ambavi.image = image.filename

        axali_ambavi.create()

        return redirect("/")

    return render_template("add_article.html", form=form)


@app.route("/delete_article/<int:article_id>")
@login_required
def delete_article(article_id):
    ambebi = Ambavi.query.get(article_id)
    ambebi.delete()

    return redirect("/")

if __name__ == "__main__":

    app.run(debug=True)

