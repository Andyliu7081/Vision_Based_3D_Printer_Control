import serial
import time

port='COM9'
baud_rate=115200

def send_gcode_line_by_line(gcode_lines):
    print("Starting")
    printer = serial.Serial(port, baud_rate, timeout=1)
    print("Serial object\n", printer)
    time.sleep(10)  # Wait for 2 seconds
    print("end sleep")
    for line in gcode_lines:
        gcode_command = f'{line}'+'\n'
        # print(line, type(line))
        # print(gcode_command)
        printer.write(gcode_command.encode('utf-8'))
        # Wait for a short duration between commands (adjust as needed)
        # time.sleep(0.1)

    printer.close()

if __name__ == "__main__":
    # Read G-code lines from the file
    gcode_lines = []
    with open("output.gcode", "r") as gcode_file:
        for line in gcode_file:
            gcode_lines.append(line.strip())
            # gcode_lines.append(line)

    # Send G-code to the printer
    send_gcode_line_by_line(gcode_lines)