# Streamlitライブラリをインポート
import random
import requests

def get_random_military_song():
  """日本の軍歌をランダムで取得する"""
  military_songs = ["軍艦マーチ", "皇国の守護者", "愛国行進曲", "海ゆかば", "出征壮行曲", "暁の水平線", "戦友", "新しき朝", "進め、進め", "南海の花"]
  return military_songs[random.randint(0, len(military_songs) - 1)]

def play_military_song(military_song):
  """日本の軍歌を再生する"""
  url = f"https://www.youtube.com/results?search_query={military_song}"
  response = requests.get(url)
  video_id = response.json()["items"][0]["id"]["videoId"]
  return f"https://www.youtube.com/watch?v={video_id}"

if __name__ == "__main__":
  military_song = get_random_military_song()
  url = play_military_song(military_song)
  print(url)
