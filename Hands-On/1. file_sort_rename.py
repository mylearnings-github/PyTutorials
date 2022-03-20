import os 
os.chdir('K:\DSA\CoreySchafer-PythonCourse\Experiment\FileSorting')

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_version, f_sequence = f_name.split('_')
    
    f_sequence = f_sequence.strip().zfill(2)
    new_f_name = f'{f_sequence}-{f_title}{f_ext}'

    os.rename(f,new_f_name)