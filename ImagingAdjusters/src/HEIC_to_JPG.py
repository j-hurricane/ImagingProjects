import os

target_folder = input('Enter the target file directory:')

for root, subdir, files in os.walk(target_folder):
    for file in files:
        if file.upper().endswith('.HEIC'):
            new_name = f'{file.split('.')[0]}.jpg'
            new_path = os.path.join(root, new_name)
            old_path = os.path.join(root, file)
            os.rename(old_path, new_path)
    input('Finished converting HEIC files.  Press any key to continue.')