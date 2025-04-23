# coding = utf-8
# !/usr/bin/python

"""

作者 丢丢喵 🚓 内容均从互联网收集而来 仅供交流学习使用 版权归原创者所有 如侵犯了您的权益 请通知作者 将及时删除侵权内容
                    ====================Diudiumiao====================

"""

from Crypto.Util.Padding import unpad
from urllib.parse import unquote
from Crypto.Cipher import ARC4
from urllib.parse import quote
from base.spider import Spider
from Crypto.Cipher import AES
from bs4 import BeautifulSoup
from base64 import b64decode
import urllib.request
import urllib.parse
import binascii
import requests
import base64
import json
import time
import sys
import re
import os

sys.path.append('..')

xurl = "https://pze--eephouquoc.chuvvip6m16.xyz"

xurl2 = "https://pze--eephouquoc.chuvvip6m16.xyz/hflvvip"

headerx = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'
          }

pm = ''

class Spider(Spider):
    global xurl
    global xurl2
    global headerx
    global headers

    def getName(self):
        return "首页"

    def init(self, extend):
        pass

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def extract_middle_text(self, text, start_str, end_str, pl, start_index1: str = '', end_index2: str = ''):
        if pl == 3:
            plx = []
            while True:
                start_index = text.find(start_str)
                if start_index == -1:
                    break
                end_index = text.find(end_str, start_index + len(start_str))
                if end_index == -1:
                    break
                middle_text = text[start_index + len(start_str):end_index]
                plx.append(middle_text)
                text = text.replace(start_str + middle_text + end_str, '')
            if len(plx) > 0:
                purl = ''
                for i in range(len(plx)):
                    matches = re.findall(start_index1, plx[i])
                    output = ""
                    for match in matches:
                        match3 = re.search(r'(?:^|[^0-9])(\d+)(?:[^0-9]|$)', match[1])
                        if match3:
                            number = match3.group(1)
                        else:
                            number = 0
                        if 'http' not in match[0]:
                            output += f"#{match[1]}${number}{xurl}{match[0]}"
                        else:
                            output += f"#{match[1]}${number}{match[0]}"
                    output = output[1:]
                    purl = purl + output + "$$$"
                purl = purl[:-3]
                return purl
            else:
                return ""
        else:
            start_index = text.find(start_str)
            if start_index == -1:
                return ""
            end_index = text.find(end_str, start_index + len(start_str))
            if end_index == -1:
                return ""

        if pl == 0:
            middle_text = text[start_index + len(start_str):end_index]
            return middle_text.replace("\\", "")

        if pl == 1:
            middle_text = text[start_index + len(start_str):end_index]
            matches = re.findall(start_index1, middle_text)
            if matches:
                jg = ' '.join(matches)
                return jg

        if pl == 2:
            middle_text = text[start_index + len(start_str):end_index]
            matches = re.findall(start_index1, middle_text)
            if matches:
                new_list = [f'{item}' for item in matches]
                jg = '$$$'.join(new_list)
                return jg

    def homeContent(self, filter):
        result = {}
        result = {"class": [{"type_id": "49", "type_name": "乐哥✨国产色情"},
                            {"type_id": "50", "type_name": "乐哥✨日本无码"},
                            {"type_id": "51", "type_name": "乐哥✨日本有码"},
                            {"type_id": "52", "type_name": "乐哥✨中文字幕"},
                            {"type_id": "53", "type_name": "乐哥✨欧美极品"},
                            {"type_id": "54", "type_name": "乐哥✨动漫精品"},
                            {"type_id": "55", "type_name": "乐哥✨强奸乱伦"},
                            {"type_id": "56", "type_name": "乐哥✨变态另类"},
                            {"type_id": "65", "type_name": "乐哥✨国产乱伦"},
                            {"type_id": "64", "type_name": "乐哥✨主播秀色"},
                            {"type_id": "63", "type_name": "乐哥✨黑丝诱惑"},
                            {"type_id": "61", "type_name": "乐哥✨熟女人妻"},
                            {"type_id": "62", "type_name": "乐哥✨三级乱伦"},
                            {"type_id": "57", "type_name": "乐哥✨自拍偷拍"},
                            {"type_id": "58", "type_name": "乐哥✨童颜巨乳"},
                            {"type_id": "59", "type_name": "乐哥✨女优明星"},
                            {"type_id": "72", "type_name": "乐哥✨门事件"},
                            {"type_id": "71", "type_name": "乐哥✨网红黑料"},
                            {"type_id": "73", "type_name": "乐哥✨少女萝莉"},
                            {"type_id": "70", "type_name": "乐哥✨女同性恋"},
                            {"type_id": "69", "type_name": "乐哥✨cosplay"},
                            {"type_id": "68", "type_name": "乐哥✨AV解说"},
                            {"type_id": "67", "type_name": "乐哥✨网曝吃瓜"},
                            {"type_id": "66", "type_name": "乐哥✨极品媚黑"},
                            {"type_id": "202", "type_name": "乐哥✨麻豆传媒"},
                            {"type_id": "205", "type_name": "乐哥✨天美传媒"},
                            {"type_id": "206", "type_name": "乐哥✨果冻传媒"},
                            {"type_id": "207", "type_name": "乐哥✨91制片厂"},
                            {"type_id": "208", "type_name": "乐哥✨蜜桃传媒"},
                            {"type_id": "209", "type_name": "乐哥✨精东影业"},
                            {"type_id": "210", "type_name": "乐哥✨皇家华人"},
                            {"type_id": "223", "type_name": "乐哥✨星空传媒"}],

                  }

        return result

    def homeVideoContent(self):
        videos = []

        try:
            detail = requests.get(url=xurl2, headers=headerx)
            detail.encoding = "utf-8"
            res = detail.text
            doc = BeautifulSoup(res, "lxml")

            soups = doc.find_all('ul', class_="thumbnail-group")

            for soup in soups:
                vods = soup.find_all('li')

                for vod in vods:
                    names = vod.find('div', class_="video-info")
                    name = names.find('h5').text

                    id = vod.find('a')['href']

                    pic = vod.find('img')['data-original']

                    remark1 = self.extract_middle_text(str(vod), '<p>', '</p>', 0)
                    remark2 = self.extract_middle_text(str(vod), '<!--p>', '</p-->', 0)
                    remark = remark1 + remark2
                    remark = remark.replace('&#35266;&#30475;:', '观看:')

                    video = {
                        "vod_id": id,
                        "vod_name": name,
                        "vod_pic": pic,
                        "vod_remarks": remark
                            }
                    videos.append(video)

            result = {'list': videos}
            return result
        except:
            pass

    def categoryContent(self, cid, pg, filter, ext):
        result = {}
        videos = []

        if pg:
            page = int(pg)
        else:
            page = 1

        if page == 1:
            url = f'{xurl}/vodtype/{cid}/'

        else:
            url = f'{xurl}/vodtype/{cid}-{str(page)}/'

        try:
            detail = requests.get(url=url, headers=headerx)
            detail.encoding = "utf-8"
            res = detail.text
            doc = BeautifulSoup(res, "lxml")

            soups = doc.find_all('ul', class_="thumbnail-group")

            for soup in soups:
                vods = soup.find_all('li')

                for vod in vods:
                    names = vod.find('div', class_="video-info")
                    name = names.find('h5').text

                    id = vod.find('a')['href']

                    pic = vod.find('img')['data-original']

                    remark = "精品推荐"

                    video = {
                        "vod_id": id,
                        "vod_name": name,
                        "vod_pic": pic,
                        "vod_remarks": remark
                            }
                    videos.append(video)

        except:
            pass
        result = {'list': videos}
        result['page'] = pg
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def detailContent(self, ids):
        global pm
        did = ids[0]
        result = {}
        videos = []

        if 'http' not in did:
            did = xurl + did

        res = requests.get(url=did, headers=headerx)
        res.encoding = "utf-8"
        res = res.text

        url = 'http://oxox.fun/oxid.txt'
        response = requests.get(url)
        response.encoding = 'utf-8'
        code = response.text
        name = self.extract_middle_text(code, "s1='", "'", 0)
        Jumps = self.extract_middle_text(code, "s2='", "'", 0)

        content = '乐哥的成就，如同一部波澜壮阔的史诗，让人心潮澎湃。在璀璨的聚光灯下，他终于站在了舞台的中央，成为了那颗最耀眼的星。他的成功，不仅仅是因为他的天赋异禀，更是因为他不懈的努力和坚持。从贫苦的出身到今日的辉煌，乐哥的每一步都充满了艰辛。他的童年，没有奢华的玩具，没有舒适的环境，有的只是对梦想的执着追求。在那些艰难的日子里，他以坚韧不拔的意志，一遍又一遍地磨练自己的演技。他欣赏了无数前辈的影片，从每一个角色、每一场戏中汲取灵感，不断学习，不断进步。乐哥的奋斗史，是一部充满汗水与泪水的励志篇章。他的成功，是对所有追梦人的最好启示：无论出身如何，只要有足够的努力和坚持，梦想总有实现的一天。他的成就，不仅仅是个人的荣耀，更是对所有坚持不懈、努力奋斗的人的鼓舞。今天，我们为乐哥欢呼，为他的成功喝彩。他的成功，不仅仅是因为他的才华，更是因为他的勤奋和毅力。他的故事告诉我们，成功从来不是偶然，而是无数次努力和坚持的结果。乐哥的今天，是对他过去所有努力的最好回报。我们期待乐哥在未来的日子里，能够继续以他的才华和努力，为我们带来更多优秀的作品。他的故事，将继续激励着每一个有梦想的人，去追逐，去实现。让我们为乐哥的成就鼓掌，为他的未来祝福，期待他在未来的日子里，能够继续发光发热，成为更多人心中的明星。'

        if name not in content:
            bofang = self.extract_middle_text(res, '<ul class="detail-play-list clearfix', '</ul>', 3,'href="(.*?)" class=".*?" style=".*?">(.*?)</a>')
            bofang = bofang.replace('在线播放', '妇愁者联盟')

            xianlu = "妇愁者联盟"
        else:
            bofang = self.extract_middle_text(res, '<ul class="detail-play-list clearfix', '</ul>', 3,'href="(.*?)" class=".*?" style=".*?">(.*?)</a>')
            bofang = bofang.replace('在线播放', '妇愁者联盟')

            xianlu = "妇愁者联盟"

        videos.append({
            "vod_id": did,
            "vod_content": content,
            "vod_play_from": xianlu,
            "vod_play_url": bofang
                     })

        result['list'] = videos
        return result

    def playerContent(self, flag, id, vipFlags):
        parts = id.split("http")

        xiutan = 0

        if xiutan == 0:
            if len(parts) > 1:
                before_https, after_https = parts[0], 'http' + parts[1]

            if 'ox' in after_https:
                url = after_https
            else:
                res = requests.get(url=after_https, headers=headerx)
                res = res.text

                url = self.extract_middle_text(res, '"","url":"', '"', 0).replace('\\', '')

            result = {}
            result["parse"] = xiutan
            result["playUrl"] = ''
            result["url"] = url
            result["header"] = headerx
            return result

    def searchContentPage(self, key, quick, page):
        result = {}
        videos = []

        if not page:
            page = '1'
        if page == '1':
            url = f'{xurl}/vodsearch/-------------/?wd={key}'

        else:
            url = f'{xurl}/vodsearch/{key}----------{str(page)}---/'


        detail = requests.get(url=url, headers=headerx)
        detail.encoding = "utf-8"
        res = detail.text
        doc = BeautifulSoup(res, "lxml")

        soups = doc.find_all('ul', class_="thumbnail-group")

        for soup in soups:
            vods = soup.find_all('li')

            for vod in vods:
                names = vod.find('div', class_="video-info")
                name = names.find('h5').text

                id = vod.find('a')['href']

                pic = vod.find('img')['src']

                remark = self.extract_middle_text(str(vod), '<p>', '</p>', 0)
                remark = remark.replace('IPX -', '')

                video = {
                    "vod_id": id,
                    "vod_name": name,
                    "vod_pic": pic,
                    "vod_remarks": remark
                        }
                videos.append(video)

        result['list'] = videos
        result['page'] = page
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def searchContent(self, key, quick, pg="1"):
        return self.searchContentPage(key, quick, '1')

    def localProxy(self, params):
        if params['type'] == "m3u8":
            return self.proxyM3u8(params)
        elif params['type'] == "media":
            return self.proxyMedia(params)
        elif params['type'] == "ts":
            return self.proxyTs(params)
        return None