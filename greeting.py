# 例えば、以下のように結合する
def greet():
    print("Hello from main!") # main ブランチでの変更
    print("Good morning!")   # main ブランチでの追加
    print("Greetings!")     # timely-message ブランチでの変更/追加

def farewell(): # timely-message ブランチで追加された関数
    print("Goodbye!")