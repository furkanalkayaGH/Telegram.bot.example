
import json

text = '{"url":{"status":7,"fullLink":"https:\/\/twitter.com\/furkan_alkaya_","date":"2022-06-08","shortLink":"https:\/\/cutt.ly\/XJDV1G8","title":"Furkan Alkaya (@furkan_alkaya_) | Twitter"}}'

d = json.loads(text)

output = d['url']['shortLink']

print(output)

