'''
 https://gist.github.com/ivansaul/ac2794ecbddec6c54f1c2e62cccfc175#file-get_youtube_id-py
 https://qiita.com/268iop/items/80b67b3147e1a2f0d89e
'''
from pytube import extract  # pip install pytube
import pytchat
import time


def main():
    URL = input('YouTubeライブのURLを入力: ')
    livechat = pytchat.create(getVideoID(URL))

    while livechat.is_alive():
        # チャットデータの取得
        chatdata = livechat.get()
        for c in chatdata.items:
            print(f"{c.datetime} {c.author.name} {c.message} {c.amountString}")
            '''
            JSON文字列で取得:
            print(c.json())
            '''
        time.sleep(1)


def getVideoID(URL):
    id = extract.video_id(URL)
    return id


if __name__ == '__main__':
    main()
