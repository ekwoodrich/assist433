from flask import Flask, request

app = Flask(__name__)

@app.route("/api/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return "Hello World"
    else:
        payload = request.get_json()

        if payload['command'] == 'on':
            if payload['device'] == 'desk':
                logout(command, device)
        elif payload['command'] == 'off':
            if payload['device'] == 'desk':
                logout(command, device)
        elif payload['command'] == 'status':
            print("Assist433 is online")


        return '200'

def logout(command, device):
    print("Turning " + command + " " + device)

if __name__ == "__main__":
    app.run(host='0.0.0.0')


