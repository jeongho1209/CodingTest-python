import re
import sys

target = sys.stdin.readline().rstrip()

main = re.findall('<main>(.*)</main>', target)[0]
div_list = re.findall('<div title="(.*?)">(.*?)</div>', main)

for title, text in div_list:
    print(f'title : {title}')
    p_list = re.findall('<p>(.*?)</p>', text)

    for p in p_list:
        p = re.sub('(<.*?>)', '', p)
        p = re.sub('\s+', ' ', p.strip())
        print(p)
