import serial
import time

port = 'COM9'
baud_rate = 115200

printer = serial.Serial(port, baud_rate, timeout=1)

time.sleep(2)  # Wait for 2 seconds

gcode_command = 'G28 X0 Y0 Z0\n'
gcode_command2 = 'G1 X250 Y210 Z200\n'

printer.write(gcode_command.encode('utf-8'))
printer.write(gcode_command2.encode('utf-8'))

# printer.close()