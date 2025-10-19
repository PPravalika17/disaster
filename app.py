from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


# Simple precaution database
PRECAUTIONS = {
"earthquake": [
"Drop, Cover and Hold On",
"Stay away from windows and heavy furniture",
"If outdoors, move to an open area away from buildings"
],
"flood": [
"Move to higher ground",
"Avoid walking or driving through flood waters",
"Turn off utilities if instructed"
],
"cyclone": [
"Secure loose outdoor objects",
"Stay indoors away from windows",
"Keep emergency kit ready"
],
"fire": [
"Evacuate immediately using the nearest exit",
"Stop, drop and roll if clothes catch fire",
"Call emergency services"
]
}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        disaster = request.form.get('disaster', '').strip().lower()
        if not disaster:
            return render_template('index.html', error='Please enter a disaster name')
# redirect to precautions page
        return redirect(url_for('precautions', disaster_name=disaster))
    return render_template('index.html')


@app.route('/precautions/<disaster_name>')
def precautions(disaster_name):
    key = disaster_name.strip().lower()
    notes = PRECAUTIONS.get(key)
    if notes is None:
        notes = [
"No predefined precautions for: {}".format(disaster_name),
"General advice: Follow local authority instructions and stay safe."
]
    return render_template('precautions.html', disaster=disaster_name, precautions=notes)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)