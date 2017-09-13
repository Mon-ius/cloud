import requests
image_bytes = requests.get('https://plot.ly/~chris/1638.jpg').content
print(image_bytes,end='\n')




