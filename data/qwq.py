"""
topic:豆瓣是异步加载的，更神奇的是response的内容是json，我试着抓取
author:小灵子
date:2019-6-4
"""
import requests
import time

def build_url():
    for page in range(31): #查询三十页即可
        url = 'http://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=' + str(page) + '&limit=20'
        yield url

headers = {'Cookie': "has_js=1; _ga=GA1.2.1891912329.1611233853; _gid=GA1.2.1418182284.1611233853; SESS44934a1e03ff8275732bdbfdcebdc556=c4G30SkeeJoTmu1zxicFHLh9DHb_XM-DcpmBhy32W98; _gat=1",
           'Content-Type': 'application/x-www-form-urlencoded',
           'Accept': '*/*',
           'Connection': 'keep-alive',
           'Accept-Encoding': 'gzip, deflate, br'}


def get_wb_data(films):
    for url in build_url():
        r = requests.get(url, headers)
        wb_data = r.json()
        #print(type(wb_data))

        for item in wb_data:
            rating = item["rating"][0]
            cover_url = item["cover_url"]
            title = item["title"]
            if float(rating) >= 9:
                films.append({"片名：": title, "评分：": rating})
                with open('D:\\douban\\{}.jpg'.format(title), 'wb') as f:
                    img = requests.get(cover_url,headers).content
                    f.write(img)

        time.sleep(1)


def main():
    good_films = []
    get_wb_data(good_films)
    print("9分以上剧情电影 %d 部" % len(good_films))
    for film in good_films:
        print(film)


if __name__ == "__main__":
    main()