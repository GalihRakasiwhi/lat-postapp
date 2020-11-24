from wtforms import Form, StringField, validators, PasswordField, SubmitField

class RegisterForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=64)])
    full_name = StringField('Full Name', [validators.Length(min=4, max=128)])
    email = StringField('Email', [validators.Length(min=4, max=128)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Submit')