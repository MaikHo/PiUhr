#!/usr/bin/python3
import RPi.GPIO as GPIO
import http.server
import time
import _thread

# PINS am J8-Header:
# 34 - GND
# 36 - Steuerausgang X1
# 38 - Steuerausgang X2

FACTOR = 6 # Sekunden pro Sekunde, max. 1/TIME!
PORT_NUMBER = 6543
TIME = 0.2

PIN_X1 = 36
PIN_X2 = 38

running = True

def setup_pin(pin):
    GPIO.setup(pin, GPIO.OUT)

def pin(pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(TIME)
    GPIO.output(pin, GPIO.LOW)

def calc_wait():
    return (60 / FACTOR) - TIME

class ApiHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "application/json")
        s.end_headers()
    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "application/json")
        s.end_headers()
        global FACTOR
        global running
        success = False
        if s.path.startswith("/setf/"):
            try:
                fact = int(s.path.replace("/setf/", "").strip("/"))
                if fact > 60 / TIME:
                    success = False
                else:
                    success = True
                    FACTOR = fact
            except:
                success = False
        if s.path.startswith("/status"):
            success = True
        if s.path.startswith("/start"):
            running = True
            success = True
        if s.path.startswith("/stop"):
            running = False
            success = True
        
        data = ('{"success":%s,"factor":%s,"running":%s}' % (success, FACTOR, running)).lower()
        s.wfile.write(data.encode("utf-8"))

server = http.server.HTTPServer(('localhost', PORT_NUMBER), ApiHandler)

_thread.start_new_thread(server.serve_forever, ())

print ('Server gestartet!')


# Board-Pin-Nummern verwenden
GPIO.setmode(GPIO.BOARD)

setup_pin(PIN_X1)
setup_pin(PIN_X2)

try:
    while 1:
        if running:
            pin(PIN_X1)
            time.sleep(calc_wait())
            pin(PIN_X2)
            time.sleep(calc_wait())
                        
except KeyboardInterrupt:
    server.shutdown()
    GPIO.cleanup()
