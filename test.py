import serial, time, syslog, string

def scoredisp(score):
	port='/dev/ttyACM0'
	ard=serial.Serial(port,9600)
	ard.write(str(score).encode('ascii'))