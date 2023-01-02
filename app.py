from flask import Flask, render_template, url_for, flash, redirect
from forms import CustomerForm
import xgboost as xgb
import numpy as np
import git

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

MODEL_PATH = 'xgb_model_selected_sklearn.json'

model = xgb.XGBClassifier()
model.load_model(MODEL_PATH)

@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./Bank-Marketing-Analysis-and-Prediction')
    origin = repo.remotes.origin
    repo.create_head('master',
                     origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
    origin.pull()
    return '', 200


@ app.route("/", methods=['GET', 'POST'])
@ app.route("/home", methods=['GET', 'POST'])
def home():
    form = CustomerForm()
    if form.validate_on_submit():
        job_array = [0]*11  # remove unknown
        martial_status_array = [0]*3
        contact_array = [0]*2
        education_array = [0]*3  # remove unknown
        previous_outcome_array = [0]*3  # remove unknown

        age = form.age.data

        job_array[int(form.job.data)] = 1
        martial_status_array[int(form.martial_status.data)] = 1
        contact_array[int(form.contact.data)] = 1
        education_array[int(form.education.data)] = 1
        previous_outcome_array[int(form.previous_outcome.data)] = 1

        default = int(form.default.data)
        housing = int(form.housing.data)
        balance = int(form.balance.data)
        loan = int(form.loan.data)

        duration = int(form.duration.data)
        day = int(form.day.data)
        campaign = int(form.campaign.data)
        previous = int(form.previous.data)

        month_sin = np.sin(int(form.month.data)*(2.*np.pi/12))
        month_cos = np.cos(int(form.month.data)*(2.*np.pi/12))

        # prediction_array = [age, default,
        #                     balance, housing, loan, day, duration]
        # prediction_array.extend(
        #     job_array+contact_array+previous_outcome_array+education_array+martial_status_array)
        # prediction_array.append(month_sin)
        # prediction_array.append(month_cos)
        # prediction_array.append(campaign)
        # prediction_array.append(previous)

        # prediction_array = [prediction_array]

        # print(' '.join(map(str, prediction_array)))

        prediction_array = [[age, default, balance, housing, loan, day, duration, job_array[0], job_array[1], job_array[2],
                            job_array[3], job_array[4], job_array[5], job_array[6], job_array[7], job_array[8], job_array[9],
                            job_array[10], contact_array[0], contact_array[1], previous_outcome_array[0], previous_outcome_array[1],
                            previous_outcome_array[2], education_array[0], education_array[1], education_array[2],
                            martial_status_array[0], martial_status_array[1], martial_status_array[2], month_sin, month_cos,
                            campaign, previous]]

        prediction = model.predict(prediction_array)

        flash(f'The customer will receive the term deposit', 'success') if int(
            prediction[0]) == 1 else flash(f'The customer will not receive the term deposit', 'danger')
        return redirect(url_for('home'))
    return render_template('home.html', form=form)


@ app.route("/about")
def about():
    return render_template('about.html', title='About')


#if __name__ == '__main__':
#    app.run(debug=True)
