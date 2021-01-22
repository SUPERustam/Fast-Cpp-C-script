import os


def main(file_run):
    os.chdir('..')

    if not os.access(file_run, os.F_OK):
        return 'File not exists'
    os.system(f'g++ {file_run} -o mic')
    os.system('mic.exe')
    return '\nComplete successfully!'


print(main(input()))
