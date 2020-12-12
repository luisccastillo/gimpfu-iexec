import os
import sys
import json
import time

input_directory = os.environ['IEXEC_IN']
output_directory = os.environ['IEXEC_OUT']

start_time = time.time()

for filename in os.listdir(input_directory):
    if filename.endswith(".jpg") or filename.endswith(".png"): 
        filepath = os.path.join(input_directory, filename)
        os.system("gimp -i -b '(python-fu-cartoon RUN-NONINTERACTIVE \""+ filepath +"\" \""+ filename +"\" \""+ output_directory +"\" )' -b '(gimp-quit 0)'")


end_time = time.time()

# Append some results in /iexec_out/
with open(output_directory + '/result.txt', 'w+') as fout:
    fout.write("Executed in "+ str(end_time - start_time)) 

# Declare everything is computed
with open(output_directory + '/computed.json', 'w+') as f:
    json.dump({ "deterministic-output-path" : output_directory + '/result.txt' }, f)

