import urllib.request
import os


path = './public/'
web = 'mzitu/20191109/'
this_path = path + web
try:
    if os.path.exists(this_path) == False:
        os.makedirs(this_path)
finally:
    print('make error')

# headerd = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0")
# refer = ("Referer","https://www.mzitu.com")
# accecpt = ("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
# ae = ("Accept-Encoding","gzip, deflate, br")
# al = ("Accept-Language","zh-CN,zh;q=0.9")
# #con = ("Connection","keep-alive")
# #cook = ("Cookie","Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1573214408,1573256336,1573294494,1573305214; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1573305316")
# opener = urllib.request.build_opener()
# #opener.addheaders = [headerd,refer,accecpt,ae]
# opener.addheaders = [headerd]
# file = opener.open("https://www.mzitu.com/210776")
# data = file.read()
# print(data)
# with open('test.txt', 'wb') as fd:
#             # fd.write(str(data))
#            fd.write(data)
# exit()
start = 210776
end = 0
count = 0

while start > end:
    try:
        while count < 80:
            file_name = this_path + str(start) + '-' + str(count) + ".txt"
            if os.path.isfile(file_name):
                continue
            headerd = ("User-Agent",
                       "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0")
            refer = ("Referer", "https://www.mzitu.com")
            accecpt = (
                "Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
            ae = ("Accept-Encoding", "gzip, deflate, br")
            al = ("Accept-Language", "zh-CN,zh;q=0.9")
            # con = ("Connection","keep-alive")
            # cook = ("Cookie","Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1573214408,1573256336,1573294494,1573305214; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1573305316")
            opener = urllib.request.build_opener()
            # opener.addheaders = [headerd,refer,accecpt,ae]
            opener.addheaders = [headerd, refer, accecpt]
            html_end = '/' + str(count)
            if count == 1 or count == 0:
                html_end = ''
            print("https://www.mzitu.com/" + str(start) + html_end)
            file = opener.open("https://www.mzitu.com/" + str(start) + html_end)
            # file_name = this_path + str(start) + '-' + str(count) + ".txt"
            
            data = file.read()
            # with open(file_name, 'w', encoding='UTF-8') as fd:
            with open(file_name, 'wb') as fd:
                # fd.write(str(data))
                fd.write(data)
            count = count + 1
    except Exception as e:
        pass
    except TimeoutError as e:
        pass
    finally:
        print(start)
        if count < 45 and count > 1:
            count = count + 2
        else:
            start = start - 1
            count = 1
# import redis
#
# redisObj = redis.Redis()
# redisObj.set('xi', 'women')
# print(str(redisObj.get('xi')))
