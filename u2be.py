import os
import subprocess
import sys


def download_audio(directory, url):
    if not os.path.exists(directory):
        os.makedirs(directory)

    print('URL: ', url)
    os.chdir(directory)

    u2be_dl = 'youtube-dl -ci --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" ' + url
    subprocess.call(u2be_dl, shell=True)


if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2], sys.argv[3])
