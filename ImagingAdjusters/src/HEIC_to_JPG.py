import os

target_folder = input('Enter the target file directory:')

for file in os.listdir(target_folder):
    if file.upper().endswith('.HEIC'):
        root = os.path.abspath(file)
        new_name = f'{file.split('.')[0]}.jpg'
        new_path = os.path.join(root, new_name)
        old_path = os.path.join(root, file)
        os.rename(old_path, new_path)

input('Finished converting HEIC files.  Press any key to continue.')