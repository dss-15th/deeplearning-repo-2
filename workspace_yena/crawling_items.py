import os 
import requests

if not os.path.exists("datas"):
    os.makedirs("datas")

def save_file(title,link):
    response = requests.get(link)
    with open ("datas/{}.png".format(title),"wb") as f:
        f.write(response.content)
    
for num in range(5):
    url = 'https://ohou.se/store/category.json?v=2&category=0_{}&page=1&per=24'.format(num)
    response = requests.get(url)
    items = response.json()['productions']
    for item in items:
        img_url = item['resized_image_url']
        item_id = str(item['id'])
        save_file('chair_'+item_id, img_url)