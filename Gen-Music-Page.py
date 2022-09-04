import os
import re
import glob
import pyperclip
def Getinf(FilePath):
    with open(FilePath, "rb") as input_file:
        mp3_data = input_file.read(500).hex()
    if mp3_data[:6] == "494433" and mp3_data[6:8] == "03":
        tag_name_list = {"TIT2": "54495432", "TPE1": "54504531", "TALB": "54414c42"}
        #title 标题
        tag_hex = tag_name_list["TIT2"]  # 标签的 16 进制数据
        tag_len = int(re.search(tag_hex + "(.{8})", mp3_data).group(1), 16)
        tag_index = mp3_data.find(tag_hex)
        tag_data_type = mp3_data[(tag_index + 2 * (4 + 4 + 2)):(tag_index + 2 * (4 + 4 + 2 + 1))]
        tag_data_hex = mp3_data[(tag_index + 2 * (4 + 4 + 2 + 1)):(
        tag_index + 2 * (4 + 4 + 2 + 1) + tag_len * 2 - 2)]  # 取标签内容(16进制)
        tag_data_bytes = bytes.fromhex(tag_data_hex)  # 将字符串转换为字节流数据
        encoding_type="utf-16-le"
        tag_info = tag_data_bytes.decode(encoding_type, 'ignore')  # 根据编码类型解码
        t="| "+tag_info
        #TPE1 创作者
        tag_hex = tag_name_list["TPE1"]  # 标签的 16 进制数据
        tag_len = int(re.search(tag_hex + "(.{8})", mp3_data).group(1), 16)
        tag_index = mp3_data.find(tag_hex)
        tag_data_type = mp3_data[(tag_index + 2 * (4 + 4 + 2)):(tag_index + 2 * (4 + 4 + 2 + 1))]
        tag_data_hex = mp3_data[(tag_index + 2 * (4 + 4 + 2 + 1)):(
        tag_index + 2 * (4 + 4 + 2 + 1) + tag_len * 2 - 2)]  # 取标签内容(16进制)
        tag_data_bytes = bytes.fromhex(tag_data_hex)  # 将字符串转换为字节流数据
        encoding_type="utf-16-le"
        tag_info = tag_data_bytes.decode(encoding_type, 'ignore')  # 根据编码类型解码
        t=t+" | "+tag_info+" | "
        return t
    elif mp3_data[:6] == "494433" and mp3_data[6:8] == "04":
        tag_name_list = {"TIT2": "54495432", "TPE1": "54504531", "TALB": "54414c42"}
        #title
        tag_hex = tag_name_list["TIT2"]  # 标签的 16 进制数据
        tag_len = int(re.search(tag_hex + "(.{8})", mp3_data).group(1), 16)
        tag_index = mp3_data.find(tag_hex)
        tag_data_type = mp3_data[(tag_index + 2 * (4 + 4 + 2)):(tag_index + 2 * (4 + 4 + 2 + 1))]
        tag_data_hex = mp3_data[(tag_index + 2 * (4 + 4 + 2 + 1)):(
        tag_index + 2 * (4 + 4 + 2 + 1) + tag_len * 2 - 2)]  # 取标签内容(16进制)
        tag_data_bytes = bytes.fromhex(tag_data_hex)  # 将字符串转换为字节流数据
        encoding_type="utf-8"
        tag_info = tag_data_bytes.decode(encoding_type, 'ignore')  # 根据编码类型解码
        t="| "+tag_info
        #TPE1
        tag_hex = tag_name_list["TPE1"]  # 标签的 16 进制数据
        tag_len = int(re.search(tag_hex + "(.{8})", mp3_data).group(1), 16)
        tag_index = mp3_data.find(tag_hex)
        tag_data_type = mp3_data[(tag_index + 2 * (4 + 4 + 2)):(tag_index + 2 * (4 + 4 + 2 + 1))]
        tag_data_hex = mp3_data[(tag_index + 2 * (4 + 4 + 2 + 1)):(
        tag_index + 2 * (4 + 4 + 2 + 1) + tag_len * 2 - 2)]  # 取标签内容(16进制)
        tag_data_bytes = bytes.fromhex(tag_data_hex)  # 将字符串转换为字节流数据
        tag_info = tag_data_bytes.decode(encoding_type, 'ignore')  # 根据编码类型解码
        t=t+" | "+tag_info+" | "
    else:
        print(FilePath+"error")
    return t
list=[("D:\\Store\\music\\c1\\","### 这个列表大多数演唱者都是女性"),
("D:\\Store\\music\\c2\\","### 这个列表大多数演唱者都是男性"),
("D:\\Store\\music\\d\\","### 这个列表大多数为对唱"),
("D:\\Store\\music\\e\\","### 这个列表收集了一些英文歌曲"),
("D:\\Store\\music\\y\\","### 这个列表大多数为粤语"),
("D:\\Store\\music\\f\\","### 这个列表都是除了中文和英文的歌曲"),
("D:\\Store\\music\\l\\","### 这个列表收集了一些轻音乐，多为钢琴曲和小提琴曲，还有一些中国传统乐器"),
("D:\\Store\\music\\la\\","### 这个列表收藏的是在ACG中出现的轻音乐"),
("D:\\Store\\music\\o\\","### 这个列表大多数为作者认为的老歌曲\n(对，不要你认为，我要我认为/doge)")]
def scan():
    t='''---
title: 博主的乐库
date: 2015-08-01
categories: Essay
pid: 1009
tags: Essay
keywords:
- hexo
- javascript
thumbnailImage: "cover.jpg"
thumbnailImagePosition: left
---
博主收藏的音乐，只想安安静静听个歌，并不想对艺人的行为做过多的评论，也不代表对歌词内容有过多的考究
<!-- more -->
此页面由[Python代码](https://github.com/panxiuwen/Gen-Music-Page)自动生成
'''
    a=0
    for i in list:
            Dir=i[0]
            if Dir=="D:\\Store\\music\\la\\":
                print("do nothing")
            else:
                t=t+i[1]+"\n| 歌曲 | 作者 |\n"
                t=t+"| :-: | :-: |\n"
            ln=Dir[Dir.rfind("/",0,-1)+1:-1]
            files=glob.glob(os.path.join(Dir, "*.mp3"))
            for file in files:
                t=t+Getinf(file)+"\n"
                a=a+1
    t=t+"\n乐库共"+str(a)+"首歌"
    print(a)
    pyperclip.copy(t)
scan()
