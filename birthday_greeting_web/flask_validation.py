from wtforms import Form, StringField, DateField, validators


class CreateGreetingForm(Form):
    from_greeting = StringField('from_greeting', [validators.DataRequired()])
    to = StringField('to', [validators.DataRequired()])
    title = StringField('title', [validators.DataRequired()])
    content = StringField('content', [validators.DataRequired(), validators.Length(max=200)])
    date = DateField("date", format='%d/%m/%Y', description="format: day/month/year", validators=[validators.DataRequired()])