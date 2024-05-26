import subprocess
from urllib.parse import quote
import os,time

'''
測試單句下載 mp3
'''
# 設定給 google 小姐發音的文字
words = '如何讓你遇見我,在我最美麗的時刻,為這 我已在佛前,求了五百年,求他讓我們結一段塵緣,佛於是把我化作一棵樹,長在你必經的路旁,陽光下慎重地開滿了花,朵朵都是我前世的盼望,當你走近　請你細聽,那顫抖的葉是我等待的熱情,而當你終於無視地走過,在你身後落了一地,的朋友啊　那不是花瓣,是我凋零的心'
# words = '我的優點就是帥，缺點就是帥得不明顯'

# # 轉成符合 url 格式的文字
encode_url = quote(words)

cmd = [
    'curl',
    '-X',
    'GET',
    f"https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=zh-TW&q={encode_url}",
    '-o',
    f"./新詩.mp3"
]
std_output = subprocess.run(cmd)
if std_output.returncode == 0 :
    print ("下載成功")
else:
    print("下載失敗")


cmd = [
    './ffmpeg/bin/ffmpeg.exe',
    '-i',
    './新詩.mp3',
    '-filter:a',
    'atempo=1.7',
    './新詩_atempo.mp3',
]

std_output = subprocess.run(cmd)
if std_output.returncode == 0 :
    print('轉換成功')
else :
    print('轉換失敗')

if not os.path.exists('mp3'):
    os.makedirs('mp3')
list_words = [
    '人生短短幾個秋啊',
    '不醉不罷休',
    '東邊我的美人哪',
    '西邊黃河流'
]
for index , words in enumerate(list_words):
    encode_url = quote(words)
    cmd = [
        'curl',
        '-X',
        'GET',
        f'https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=zh-TW&q={encode_url}',
        '-o',
        f'./mp3/{index}.mp3'
    ]    
    std_output = subprocess.run(cmd)
    if std_output.returncode == 0 :
        print(f'{index} 轉換成功')
    else :
        print(f'{index}轉換失敗')

    cmd = [
        './ffmpeg/bin/ffmpeg.exe', # 左邊是 Windows 指令。MacOS: ./ffmpeg
        '-i',
        f'./mp3/{index}.mp3',
        '-filter:a',
        'atempo=1.5', # 'asetrate=44100*0.4,atempo=1.5'
        f'./mp3/{index}_atempo.mp3'
    ]
    std_output = subprocess.run(cmd)
    if std_output.returncode == 0:
        print(f'[{index}_atempo] 轉換成功')
    else:
        print(f'[{index}_atempo] 轉換失敗')


