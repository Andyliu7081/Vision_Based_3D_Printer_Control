import serial

# Configure serial port settings
serial_port = "COM9"  # Replace with your printer's serial port
baud_rate = 115200

# Open the serial connection
printer = serial.Serial(serial_port, baud_rate, timeout=1)

# Define the G-code file path
gcode_file_path = "output.gcode"

# Read the entire G-code file content
with open(gcode_file_path, "r") as gcode_file:
    gcode_content = gcode_file.read()

# Send the entire G-code content to the printer
printer.write(gcode_content.encode())
printer.flush()

# Close the serial connection
printer.close()
