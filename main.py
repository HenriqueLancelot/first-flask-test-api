import classifier as c
from flask import Flask, request, json

app = Flask(__name__)

@app.route("/api/identify-contract")
def identify_contract():
  phrase = request.args.get("phrase")
  prediction = c.identify(phrase)
  response = json.dumps({ "required_security_contract": prediction.cats['CONSISTENTE'] > 0.70 })

  return app.response_class(response, 200)

if __name__ == '__main__':
  app.run(debug=True)
