from PIL import Image
import pillow_heif
import os


target_folder = input('Enter the target file directory:')

for file in os.listdir(target_folder):
    if file.upper().endswith('.HEIC'):
        root = os.path.abspath(target_folder)
        f_path = os.path.join(root, file)
        new_path = f_path.replace('.HEIC', '.jpg')
        try:
            heif_file = pillow_heif.read_heif(f_path)
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
            )
            image.save(new_path, format("jpeg"))
        except Exception as e:
            print(f'Error: {e}.')
            print(f'File {file} may not be HEIC, attempting to save as jpeg.')
            image = Image.open(f_path)
            image.save(new_path, format("jpeg"))

input('Finished converting HEIC files.  Press any key to continue.')