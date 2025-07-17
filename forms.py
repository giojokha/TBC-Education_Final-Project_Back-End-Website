from flask_wtf import FlaskForm
from wtforms.fields import (StringField, PasswordField, SubmitField,
                            SelectField, DateField, IntegerField, RadioField, TextAreaField)
from wtforms.validators import DataRequired, length, equal_to
from flask_wtf.file import FileField


class RegisterForm(FlaskForm):
    username = StringField("შეიყვანე სახელი", validators=[DataRequired()])
    password = PasswordField("შეიყვანე პაროლი", validators=[DataRequired(),
                                                            length(min=8, max=32, message="პაროლი უნდა იყოს მინიმუმ 8 სიმბოლო")])
    confirm_password = PasswordField("გაიმეორე პაროლი", validators=[DataRequired(),
                                                                    equal_to("password", message="პაროლები არ ემთხვევა")])


    submit = SubmitField("დარეგისტრირდი")


class LoginForm(FlaskForm):
    username = StringField("შეიყვანე სახელი")
    password = PasswordField("შეიყვანე პაროლი")
    submit = SubmitField("შესვლა")


class ArticleForm(FlaskForm):
    image = FileField("დაამატეთ თქვენი სასურველი ფოტო გამოსაქვეყნებელი ინფორმაციისთვის")
    news_title = StringField("შეიყვანეთ თქვენთვის სასურველი ინფორმაცია")
    Date = IntegerField("შეიყვანეთ ინფორმაციის თარიღი")
    publish = SubmitField("ინფორმაციის გამოქვეყნება")