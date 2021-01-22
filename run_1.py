import os


def main(file_run):
    os.chdir('..')

    if not os.access(file_run, os.F_OK):
        return f'File not exists in {os.getcwd()}'
    os.system(f'g++ {file_run} -o mic')
    os.system('mic.exe')
    return f'\nRan {file_run}!'


print(main(input()))
