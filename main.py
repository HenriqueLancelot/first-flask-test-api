import classifier as c
from flask import Flask, request, json

app = Flask(__name__)

@app.route("/api/identify-contract")
def identify_contract():
  phrase = request.args.get("phrase")
  prediction = c.identify(phrase)

  return app.response_class(
      response = json.dumps({ "required": prediction.cats }),
      status=200,
      mimetype="application/json"
  )

if __name__ == '__main__':
  app.run(debug=True)
