import time
import os
import random

def display_lyrics(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # コンソールから邪魔な文字列をクリア
            os.system('clear')
            # ファイル先頭から1行ずつ処理
            for line in lines:
                # 1文字ずつ表示
                for char in line.strip():
                    print(char, end='', flush=True)
                    # 等間隔だとリアル感(?)に欠けるためランダムな秒数待って表示する
                    sleep_time = random.uniform(0.05, 0.1)
                    time.sleep(sleep_time)
                input_key = input("")
                # スペースキー入力+エンターキーで改行し、次の行を表示
                if input_key == ' ':
                    # 新しい行
                    print()
                # エンターキー入力で増やしていた行を全てクリア
                elif input_key == '':
                    os.system('clear')
                else:
                    print("Invalid input. Press Enter or Space.")
                    continue
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # コンソールから邪魔な文字列をクリア
    os.system('clear')
    # 歌詞ファイルを指定する
    file_path = input("Enter the path to the text file: ")
    display_lyrics(file_path)
