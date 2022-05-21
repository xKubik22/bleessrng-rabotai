with open('user_settings.txt', mode='r', encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    if line.find('path_to_calc_file') != -1:
        path_to_calc_file = line.replace('path_to_calc_file = ', '')


