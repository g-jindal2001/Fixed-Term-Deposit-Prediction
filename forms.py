from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange

# Don't change the numbering of the keys in key-value pairs


class CustomerForm(FlaskForm):
    age = IntegerField(
        'Age', validators=[DataRequired(), NumberRange(min=1, max=100)])
    job = SelectField('Job', validators=[DataRequired()], choices=[
        (0, 'Admin'), (1, 'Blue-Collar'), (2, 'Entrepreneur'), (3, 'Housemaid'), (4, 'Management'), (5, 'Retired'), (6, 'Self-employed'), (7, 'Services'), (8, 'Student'), (9, 'Technician'), (10, 'Unemployed')])
    martial_status = SelectField('Martial Status', validators=[DataRequired()], choices=[
        (2, 'Married'), (1, 'Single'), (0, 'Divorced')])
    education = SelectField('Education', validators=[DataRequired()], choices=[
        (0, 'Primary'), (1, 'Secondary'), (2, 'Tertiary')])
    default = SelectField('Default', validators=[DataRequired()], choices=[
                          (1, 'Yes'), (0, 'No')])
    housing = SelectField('Housing', validators=[DataRequired()], choices=[
                          (1, 'Yes'), (0, 'No')])
    balance = IntegerField('Balance present in account',
                           validators=[DataRequired()])
    loan = SelectField('Loan', validators=[DataRequired()], choices=[
        (1, 'Yes'), (0, 'No')])
    contact = SelectField('Contact Communication Type', validators=[DataRequired()], choices=[
        (0, 'Cellular'), (1, 'Telephone')])
    duration = IntegerField(
        'Duration of the call (in seconds)', validators=[DataRequired(), NumberRange(min=1, max=800)])
    day = IntegerField(
        'Last Contact Day', validators=[DataRequired(), NumberRange(min=1, max=31)])
    month = SelectField('Last Contact Month', validators=[DataRequired()], choices=[
        (0, 'January'), (1, 'February'), (2, 'March'), (3, 'April'), (4, 'May'), (5, 'June'), (6, 'July'), (7, 'August'), (8, 'September'), (9, 'October'), (10, 'November'), (11, 'December')])
    campaign = IntegerField(
        'Contacts performed during current campaign for this client', validators=[DataRequired(), NumberRange(min=1, max=10)])
    previous = IntegerField(
        'Contacts performed during previous campaign for this client', validators=[DataRequired(), NumberRange(min=1, max=10)])
    previous_outcome = SelectField('Outcome of previous campaign', validators=[DataRequired()], choices=[
        (2, 'Success'), (0, 'Failure'), (1, 'Other')])
    submit = SubmitField('Submit')
