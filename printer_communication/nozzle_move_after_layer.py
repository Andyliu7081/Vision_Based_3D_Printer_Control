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
                # Add G-code to move nozzle to the top-right corner
                # !!! need to determine the coordinates; maybe 250mm x 210mm x 200mm - the prev coord?
                f_out.write("G1 X250 Y210\n") 
                # wait for 5 seconds
                f_out.write("G4 P5000\n")
                # move nozzle back to starting position
                # !!! may be optional; maybe can move directly back to the prev coord
                f_out.write("G1 X0 Y0\n")

input_file = "SmallBellow_0.2mm_FLEX_MK3S_3h48m.gcode"
output_file = "output.gcode"

add_nozzle_movement(input_file, output_file)