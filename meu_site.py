from flask import Flask, render_template, json

app = Flask(__name__)

@app.route("/api")
def index():
    response = app.response_class(
        response=json.dumps({ "message": "Application is running on port 5000" }),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/person")
def person():
    response = app.response_class(
        response=json.dumps({ "name": "Felipe", "age":"27"}),
        status=201,
        mimetype="application/json"
    )
    return response

if __name__ == '__main__':
    app.run(debug=True)
