from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Replace with your prediction logic
    course = request.form['course']
    gpa = request.form['gpa']
    workshops = request.form['workshops']
    projects = request.form['projects']
    clubActivity = request.form['clubActivity']
    skills = request.form['skills']

    # Example prediction logic
    if float(gpa) > 8.5:
        pred = "You are a Good Student"
    elif float(gpa) > 7.0:
        pred = "You are an Average Student"
    else:
        pred = "You are a Poor Student"

    return render_template('Web.html', pred=pred)

if __name__ == '__main__':
    app.run(debug=True)
