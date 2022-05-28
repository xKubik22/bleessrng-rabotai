class Config:
    SETTINGS = \
        {
            'PATH_TO_CALC_FILE': None,
            'PATH_TO_FOLDER_TEMPLATES': None,
            'PATH_TO_WORK_FOLDER': None
        }


    @classmethod
    def init_settings(cls):
        with open('user_settings.txt', mode='r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            for field in cls.SETTINGS.keys():
                if line.find(field) != -1:
                    cls.SETTINGS[field] = line.replace(f'{field} = ', '').strip()

    @classmethod
    def change_file_path(cls, path: str, flag: str) -> None:
        """
        :param path: Строка с новым маршрутом до файла
        :param flag: Флаг, который определяет перезапись настроек
        где 'w' - флаг для изменения пути до файлов рабочей директории
        где 'с' - флаг для изменения пути до файлов расчетки
        где 't' - флаг для изменения пути до файлов шаблонов
        """
        if flag == 'c':
            flag = 'PATH_TO_CALC_FILE'
        elif flag == 't':
            flag = 'PATH_TO_FOLDER_TEMPLATES'
        elif flag == 'w':
            flag = 'PATH_TO_WORK_FOLDER'

        with open('user_settings.txt', mode='r', encoding='utf-8') as file:
            lines = file.readlines()

        with open('user_settings.txt', mode='w', encoding='utf-8') as file:
            for line in lines:
                if flag in line:
                    file.write(f"{flag} = {path}\n")
                else:
                    file.write(line)

        cls.init_settings()

    @classmethod
    def get_calc_path(cls):
        return cls.SETTINGS['PATH_TO_CALC_FILE']

    @classmethod
    def get_work_folder_path(cls):
        return cls.SETTINGS['PATH_TO_WORK_FOLDER']

    @classmethod
    def get_templates_path(cls):
        return cls.SETTINGS['PATH_TO_FOLDER_TEMPLATES']



Config.init_settings()
Config.change_file_path('1111\n', 'w')
# for field in dir(Config):
#     if field.isupper():
#      print(field)
