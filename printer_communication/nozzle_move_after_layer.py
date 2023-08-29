import time

MAX_X = 250
MAX_Y = 210
MAX_Z = 200

# Function to add the nozzle movement G-code
def add_nozzle_movement(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            # Write each line from the input file to the output file
            f_out.write(line)
            
            # Check if it's the end of a layer
            if line.startswith(";LAYER_CHANGE"):
                # Add G-code to move nozzle to the camera position
                f_out.write("G1 X160 Y175 Z25\n") 
                # wait for 5 seconds
                f_out.write("G4 P5000\n")
                # move nozzle back to starting position

input_file = "gcode/SmallBellow_0.4n_0.3mm_FLEX_MK3S_1h14m.gcode"
output_file = "gcode/SmallBellow_0.4n_0.3mm_FLEX_MK3S_move.gcode"

add_nozzle_movement(input_file, output_file)