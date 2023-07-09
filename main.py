import requests
import json
from flask import Flask, render_template, request

app = Flask(__name__)

url = "https://api.apilayer.com/keyword"
headers = {
"apikey" : "5eiM27UU4ZFRdIq5qmIfSH7Ix9bTujuR"
}


def send_request(body):
    payload = body.encode('utf-8')
    response = requests.post(url, headers=headers, data=payload)
    status_code = response.status_code
    result = json.loads(response.text)
    return status_code, result

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        user_input = request.form["input_body"]
        status_code, result = send_request(user_input)
        print(f"Status Code : {status_code}")
        print(f"result : {result}")
        return render_template('index.html', status_code=status_code, result=result)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)