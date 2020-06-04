import os
import sys


def rename(dir):
    for filename in os.listdir(dir):
        if filename.endswith('.mp3'):
            basename = os.path.splitext(filename)[0]
            print('Basename: ', basename)
            mylist = basename.split('-')[:-1]
            correct_list = []
            for s in mylist:
                correct_list.append(s.strip())

            oldfile = os.path.join(dir, filename)
            newfile = os.path.join(dir, '_'.join(correct_list) + '.mp3')
            print('New File: ', newfile)
            os.rename(oldfile, newfile)
        else:
            print('File is not ending with .mp3')


if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
