import os

class InvalidValues(Exception):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def invalid_cover(self):
        print('Invalid answer provided regarding presence of Book Cover. Please Answer Yes or No.')
        input('Stopping. Press any key to continue.')

    def invalid_scan_side(self):
        print('Invalid answer provided regarding First Side Scanned. Please Answer Left or Right.')
        input('Stopping. Press any key to continue.')

    def invalid_page_order(self):
        print('Invalid answer provided regarding First Side Page Order. Please Answer Left or Right.')
        input('Stopping. Press any key to continue.')


class ImageReorder(InvalidValues):
    def __init__(self, target_folder, cover_exists, first_side_scanned, first_side_order):
        self.target_folder = target_folder
        if cover_exists.lower() in ['yes','no']:
            self.cover_exists = str(cover_exists)
        else:
            raise InvalidValues().invalid_cover()
        if first_side_scanned.lower() in ['left', 'right']:
            self.first_side_scanned = str(first_side_scanned)
        else:
            raise InvalidValues().invalid_scan_side()
        if first_side_order.lower() in ['left', 'right']:
            self.first_side_order = str(first_side_order)
        else:
            raise InvalidValues().invalid_page_order()


    def cover_left_right(self):
        file_count = 0
        file_name = f'ScannedPages_{file_count}_cover.jpg'

        new_cover_path = os.path.join(self.root, file_name)
        old_cover_path = os.path.join(self.root, self.cover)

        os.rename(old_cover_path, new_cover_path)

        for i in range(0, self.book_length):
            file_count += 1
            try:
                file_name = f'ScannedPages_{file_count}_0.jpg'
                new_left_path = os.path.join(self.root, file_name)
                old_left_path = os.path.join(self.root, self.left_pages[i])
                os.rename(old_left_path, new_left_path)
            except IndexError as e:
                print(e)
                input('Press any key to continue.')

            try:
                file_name = f'ScannedPages_{file_count}_1.jpg'
                new_right_path = os.path.join(self.root, file_name)
                old_right_path = os.path.join(self.root, self.right_pages[i])
                os.rename(old_right_path, new_right_path)
            except IndexError as e:
                print(e)
                input('Press any key to continue.')

    def no_cover_left_right(self):
        file_count = 0

        for i in range(0, self.book_length):
            try:
                file_name = f'ScannedPages_{file_count}_0.jpg'
                new_left_path = os.path.join(self.root, file_name)
                old_left_path = os.path.join(self.root, self.left_pages[i])
                os.rename(old_left_path, new_left_path)
            except IndexError as e:
                print(e)
                input('Press any key to continue.')

            try:
                file_name = f'ScannedPages_{file_count}_1.jpg'
                new_right_path = os.path.join(self.root, file_name)
                old_right_path = os.path.join(self.root, self.right_pages[i])
                os.rename(old_right_path, new_right_path)
                file_count += 1
            except IndexError as e:
                print(e)
                input('Press any key to continue.')

    def cover_right_left(self):
        file_count = 0
        file_name = f'ScannedPages_{file_count}_cover.jpg'

        new_cover_path = os.path.join(self.root, file_name)
        old_cover_path = os.path.join(self.root, self.cover)

        os.rename(old_cover_path, new_cover_path)

        for i in range(0, self.book_length):
            file_count += 1
            try:
                file_name = f'ScannedPages_{file_count}_0.jpg'
                new_right_path = os.path.join(self.root, file_name)
                old_right_path = os.path.join(self.root, self.right_pages[i])
                os.rename(old_right_path, new_right_path)
            except IndexError as e:
                print(e)
                input('Press any key to continue.')

            try:
                file_name = f'ScannedPages_{file_count}_1.jpg'
                new_left_path = os.path.join(self.root, file_name)
                old_left_path = os.path.join(self.root, self.left_pages[i])
                os.rename(old_left_path, new_left_path)
            except IndexError as e:
                print(e)
                input('Press any key to continue.')

    def no_cover_right_left(self):
        file_count = 0

        for i in range(0, self.book_length):
            try:
                file_name = f'ScannedPages_{file_count}_0.jpg'
                new_right_path = os.path.join(root, file_name)
                old_right_path = os.path.join(root, self.right_pages[i])
                os.rename(old_right_path, new_right_path)
            except IndexError as e:
                print(e)
                input('Press any key to continue.')

            try:
                file_name = f'ScannedPages_{file_count}_1.jpg'
                new_left_path = os.path.join(root, file_name)
                old_left_path = os.path.join(root, self.left_pages[i])
                os.rename(old_left_path, new_left_path)
                file_count += 1
            except IndexError as e:
                print(e)
                input('Press any key to continue.')

    def separate_pages_w_cover(self):
        for root, subdir, files in os.walk(target_folder):
            self.root = root
            cover = files[0]
            self.cover = cover
            pages = files[1:]
            if len(pages) % 2 == 0:
                pass
            else:
                print('Odd Number of pages found.  Please review for errors.')
            book_length = (len(pages)//2)
            self.book_length = book_length
            if self.first_side_scanned.lower() == 'right':
                self.left_pages = pages[book_length:]
                self.right_pages = pages[:book_length]
            elif self.first_side_scanned.lower() == 'left':
                self.left_pages = pages[:book_length]
                self.right_pages = pages[book_length:]
            input('Press any key to continue.')

    def separate_pages_wo_cover(self):
        for root, subdir, files in os.walk(target_folder):
            self.root = root
            pages = files
            if len(pages) % 2 == 0:
                pass
            else:
                print('Odd Number of pages found.  Please review for errors.')
            book_length = (len(pages)//2)
            self.book_length = book_length
            if self.first_side_scanned.lower() == 'right':
                self.left_pages = pages[book_length:]
                self.right_pages = pages[:book_length]
            elif self.first_side_scanned.lower() == 'left':
                self.left_pages = pages[:book_length]
                self.right_pages = pages[book_length:]

    def configure_work_order_and_run(self):
        try:
            if self.first_side_order.lower() == 'left':
                if self.cover_exists.lower() == 'yes':
                    self.separate_pages_w_cover()
                    self.cover_left_right()
                elif self.cover_exists.lower() == 'no':
                    self.separate_pages_wo_cover()
                    self.no_cover_left_right()

            elif self.first_side_order.lower() == 'right':
                if self.cover_exists.lower() == 'yes':
                    self.separate_pages_w_cover()
                    self.cover_right_left()
                elif self.cover_exists.lower() == 'no':
                    self.separate_pages_wo_cover()
                    self.no_cover_right_left()
        except Exception as e:
            input(f'{e}')


target_folder = input('Enter the target file directory:')
cover_exists = input('Do the images include the Book Cover (Yes/No):')
first_side_scanned = input('Which page set was scanned first (Left/Right):')
first_side_order = input('Which page should be first per-pair (Left/Right):')
ir = ImageReorder(target_folder, cover_exists, first_side_scanned, first_side_order)
ir.configure_work_order_and_run()
input('Finished.  Press any key to continue.')