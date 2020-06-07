import os
import subprocess
import sys
import time

from pytube import Playlist


def download_audio(directory, url):
    if not os.path.exists(directory):
        os.makedirs(directory)

    print('Playlist URL: ', url)
    os.chdir(directory)
    playlist = Playlist(url)
    print('Number of videos in playlist: %s' % len(playlist.video_urls))

    for vid in playlist.videos:
        first = vid.streams.first()
        basename = os.path.splitext(first.default_filename)[0]
        first.download(output_path=directory)
        mp4 = "'%s'.mp4" % basename
        mp3 = "'%s'.mp3" % basename
        print('Url: ', first.url)
        print('Filename: ', basename)
        print('Mp4 Filename: ', mp4)
        print('Mp3 Filename: ', mp3)
        ffmpeg = ('ffmpeg -i %s ' % mp4 + mp3)
        subprocess.call(ffmpeg, shell=True)
        time.sleep(1)

    # for filename in os.listdir(directory):
    #     if filename.endswith('.mp4'):
    #         os.remove(filename)


if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2], sys.argv[3])
