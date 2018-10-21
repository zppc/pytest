import  requests
import  json

heads = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
link='http://www.santostang.com/2018/07/04/hello-world/'
r = requests.get(link,headers=heads)
json_data= json.loads(r.text)
print(json_data)
# comment_list = json_data['data']['comments']
# for eachone in  comment_list:
#     message =  comment_list[eachone]['content']
#     print(message)
