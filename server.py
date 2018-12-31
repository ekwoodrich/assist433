from flask import Flask, request, abort
import serial
from time import sleep
app = Flask(__name__)

ser = serial.Serial('/dev/ttyUSB0', 9600)
secret = "8808fc52"

@app.route("/api/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return "Server running."
    else:
        payload = request.get_json()
        print(payload)
        
        device = ''
        if 'secret' in payload:
            if payload['secret'] == secret:
                print("Secret verified.")
            else:
                print("Secret verification failed")
                abort(403) 
        else:
            print("Secret missing.")
            abort(403)
        if 'device' in payload:
            device = payload['device']
            device = device.strip()
            device = device.lower()
        command = payload['command']
        
        if command == 'on':
            if device == 'desk' or device == 'bench' or device == 'desk light' or device == 'bench light':
                logit(command, device)
                ser.write('19'.encode())
            elif device == 'bedroom' or device == 'bedroom light':
                logit(command, device)
                ser.write('16777203'.encode())
            elif device == 'bathroom' or device == 'bathroom light':
                logit(command, device)
                ser.write('349955'.encode())
                #lamp 349955 on / 349964 off
                #etek: 357635 on / 357644 off
            elif device == 'living' or device == 'living room' or device == 'living room light':
                logit(command, device)
                ser.write('349635'.encode())
            elif device == 'kitchen' or device == 'kitchen light' or device == 'stove' or device == 'microwave' or device =='stove light':
                logit(command, device)
                ser.write('335491'.encode())

            elif device == 'desk and living':
                logit(command, device)
                ser.write('349635'.encode())
                sleep(2.4)
                ser.write('19'.encode())

            elif device == 'all':
                ser.write('19'.encode())
                sleep(2.4)
                ser.write('16777203'.encode())
                sleep(2.4)
                ser.write('349635'.encode())
                sleep(2.4)
                ser.write('335491'.encode())
                sleep(2.4)
                ser.write('349955'.encode())
            elif device == 'all 2':
                ser.write('335491'.encode())
                sleep(2.4)
                ser.write('19'.encode())
                sleep(2.4)
                ser.write('349635'.encode())
                sleep(2.4)
                ser.write('16777203'.encode())
                sleep(2.4)
                ser.write('349955'.encode())
            else:
                print("Device '" + device + "' not found")
        
        elif command == 'off':
            if device == 'desk' or device == 'bench' or device == 'desk light' or device == 'bench light':
                logit(command, device)
                ser.write('28'.encode())
            elif device == 'bedroom' or device == 'bedroom light':
                logit(command, device)
                ser.write('16777212'.encode()) 
            elif device == 'living' or device == 'living room' or device == 'living room light':
                logit(command, device)
                ser.write('349644'.encode())

            elif device == 'kitchen' or device == 'kitchen light' or device == 'microwave' or device == 'stove' or device == 'stove light':
                logit(command, device)
                ser.write('335500'.encode())
            elif device == 'bathroom' or device == 'bathroom light':
                logit(command, device)
                ser.write('349964'.encode())
            elif device == 'all':

                ser.write('28'.encode())
                sleep(2.4)
                ser.write('16777212'.encode()) 
                sleep(2.4)
                ser.write('349644'.encode())
                sleep(2.4)
                ser.write('335500'.encode())
                sleep(2.4)
                ser.write('349964'.encode())
            elif device == 'desk and living':
                logit(command, device)
                ser.write('349644'.encode())
                sleep(2.4)
                ser.write('28'.encode())
            else:
                print("Device '" + device + "' not found")
        elif command  == 'status':
            print("Assist433 is online")


        return '200'

def logit(command, device):
    print("Turning " + command + " " + device)

if __name__ == "__main__":
    app.run(host='0.0.0.0')


