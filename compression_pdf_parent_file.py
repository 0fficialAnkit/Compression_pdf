import os
import subprocess

input_folder = 'To Compress'
output_folder = 'Compressed'

os.makedirs(output_folder, exist_ok=True)

for item in os.listdir(input_folder):
    if item.endswith('.pdf'):
        input_path = os.path.join(input_folder, item)
        output_path = os.path.join(output_folder, item)
        
        try:
            subprocess.run([
                'gswin64c',
                '-sDEVICE=pdfwrite',
                '-dCompatibilityLevel=1.4',
                '-dPDFSETTINGS=/screen',
                '-dNOPAUSE',
                '-dQUIET',
                '-dBATCH',
                f'-sOutputFile={output_path}',
                input_path
            ], check=True)
            print(f"Compressed: {item}")
        except subprocess.CalledProcessError:
            print(f"Failed to compress: {item}")
