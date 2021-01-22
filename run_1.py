import os


def main(file_run):
    os.chdir('..')

    if not os.access(file_run, os.F_OK):
        print(f'File not exists in {os.getcwd()}')
        return
    print(f'Run {file_run}!')
    os.system(f'g++ {file_run} -o mic')
    os.system('mic.exe')
    return


main(input())
