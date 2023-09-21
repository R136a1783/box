# Streamlitライブラリをインポート
import random
import requests

# 軍歌のURLリストを取得する
def get_military_song_urls():
    response = requests.get("https://www.japanese-military-songs.com/")
    html = response.text

    song_urls = []
    for a in html.split("<a href=\""):
        if "/song/" in a:
            song_urls.append("https://www.japanese-military-songs.com" + a)

    return song_urls

# ランダムで軍歌を再生する
def play_random_military_song():
    song_urls = get_military_song_urls()
    song_url = random.choice(song_urls)

    response = requests.get(song_url)
    mp3_data = response.content

    with open("military_song.mp3", "wb") as f:
        f.write(mp3_data)

    # 再生する
    subprocess.call(["mpg123", "military_song.mp3"])

# アプリケーションを起動する
if __name__ == "__main__":
    play_random_military_song()
