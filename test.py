import serial, time, syslog, string

def scoredisp(score):
	
	# initializes the serial port 
	port = '/dev/ttyACM0'
	ard = serial.Serial(port,9600)
	
	# writes the inputted score to the serial port
	ard.write(str(score).encode('ascii'))
