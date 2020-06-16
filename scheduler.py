from youtube_search import YoutubeSearch
import youtube_dl
import time
from path import Path
import os
import schedule
import traceback
from random import randint
import logging

search_terms = [
    "reggea mix",
    "trap mix",
    "hiphop mix",
    "edm mix",
    "dancehall mix",
    "workout mix",
    "relaxation mix",
    "party mix",
    "gospel mix",
    "travel mix",
    "car music mix",
    "hindi mix"
]

DIRECTORY = './'  # music source Directory
COPY_DIRECTORY = './static'  # Destination directory

d = Path(DIRECTORY)
copy_directory = Path(COPY_DIRECTORY)


def download_yt_mp3():
    results = YoutubeSearch(search_terms[randint(0, len(search_terms) - 1)], max_results=10).to_dict()
    time.sleep(10)
    print(results.__len__())
    # for id in results:
    #     print(id, results[id])

    for num in range(len(results)):
        try:

            yt_id = results[num].get('id')

            yt_vid_url = "https://www.youtube.com/watch?v=" + yt_id
            print(yt_vid_url)
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([yt_vid_url])
                break

        except Exception as e:
            print(e)

        try:
            os.remove(COPY_DIRECTORY + '/' + "a.mp3")
            print("moving Files from %s to %s" % (d, copy_directory))
            file_count = 0
            for i in d.walk():
                if i.isfile() and i.endswith('mp3'):
                    file_count += 1
                    print("moving %s" % i)
                    i.move(copy_directory)
                    os.rename(COPY_DIRECTORY + '/' + i, COPY_DIRECTORY + '/' + "a.mp3")

            print('Transferred %s files' % file_count)

        except Exception as e:
            print(e)


def custom__scheduler():
    try:
        # scheduling the pin and follow  and infinite scroll times
        print("starting custom scheduler")
        schedule.every().day.at("01:25").do(download_yt_mp3)
        schedule.every().day.at("05:44").do(download_yt_mp3)
        schedule.every().day.at("08:23").do(download_yt_mp3)
        schedule.every().day.at("13:44").do(download_yt_mp3)
        schedule.every().day.at("17:23").do(download_yt_mp3)
        schedule.every().day.at("21:23").do(download_yt_mp3)

        while 1:
            schedule.run_pending()
            time.sleep(1)

    except Exception as e:
        print('custom_scheduler Error occurred ' + str(e))
        print(traceback.format_exc())
        pass


custom__scheduler()