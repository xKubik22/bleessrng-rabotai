class Config:
    PATH_TO_CALC_FILE = None


    @classmethod
    def init_settings(cls):
        with open('user_settings.txt', mode='r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            if line.find('path to calc file') != -1:
                cls.PATH_TO_CALC_FILE = line.replace('path to calc file = ', '')

    @classmethod
    def change_calc_file_path(cls, path: str):
        with open('user_settings.txt', mode='r', encoding='utf-8') as file:
            lines = file.readlines()

        with open('user_settings.txt', mode='w', encoding='utf-8') as file:
            for line in lines:
                if 'path to calc file' in line:
                    file.write(f"path to calc file = {path}")
                else:
                    file.write(line)

        cls.init_settings()


Config.init_settings()
