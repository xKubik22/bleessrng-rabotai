import os

for k,v in os.environ.items():
    print(f'{k} = {v}')



if __name__ == '__main__':
    with open('works_indexes.py', mode='r', encoding='utf-8') as file:
        lines = file.readlines()

    with open('works_indexes.py', mode='w', encoding='utf-8') as file:
        for line in lines:
            if 'path_to_calc_file' in line:
                file.write("path_to_calc_file = 'ZP1.xlsx'\n\n")
            else:
                file.write(line)
