import requests
from bs4 import BeautifulSoup
import re

startIndex = 94680
endIndex = 94700
downloadPath = "./sgf_record/"

baseURL = 'http://www.go4go.net/go/games/record_request/'
downloadURL = 'http://www.go4go.net/sgf/__go4go_'
baseHeaders = {"Cookie": "cookie-agreed-version=1.0.0; cookie-agreed=2; _ga=GA1.2.1891912329.1611233853; "
                     "SESS44934a1e03ff8275732bdbfdcebdc556=c4G30SkeeJoTmu1zxicFHLh9DHb_XM-DcpmBhy32W98; has_js=1; "
                     "_gid=GA1.2.598795055.1611366601; _gat=1",
                   "Content-Type": "application/x-www-form-urlencoded",
                   "Accept": "*/*",
                   "Accept-Encoding": "gzip, deflate, br",
                   "Connection": "keep-alive",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4356.6 Safari/537.36"
               }


for index in range(startIndex, endIndex + 1):
    print("正在尝试：" + baseURL + str(index), end="")
    response = requests.get(baseURL + str(index), headers=baseHeaders)
    if response.status_code != 200:
        print("     FAILED")
        continue
    htmlDoc = response.text
    soup = BeautifulSoup(htmlDoc, "html.parser")
    info = soup.find('textarea', 'form-textarea')
    if info is not None:
        dtInfo = re.search(r'(DT\[)(.*)(])', info.text).group(2).replace('-', "")
        pbInfo = re.search(r'(PB\[)(.*)(]B)', info.text).group(2).replace(" ", "-")
        pwInfo = re.search(r'(PW\[)(.*)(]W)', info.text).group(2).replace(" ", "-")
        data = {"op": "Download", "g": index}
        response = requests.post(downloadURL + dtInfo + "_" + pbInfo + "_" + pwInfo + ".sgf", data=data, headers=baseHeaders, timeout = 3000)
        if response.status_code != 200:
            print("     FAILED")
            continue
        open(downloadPath + "_go4go_" + dtInfo + "_" + pbInfo + "_" + pwInfo + ".sgf", "wb").write(b"(" + response.content)
        print("     OK")
    else:
        print("     FAILED")
