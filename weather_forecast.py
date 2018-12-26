import re
import urllib.request

#https://www.weather-forecast.com/locations/Mumbai/forecasts/latest

city = input("Enter your city:")
url = "https://www.weather-forecast.com/locations/" + city + "/forecasts/latest"
#print(url)

from urllib.request import Request, urlopen
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

data = urlopen(req).read()
data1 = data.decode("utf-8")

m = re.search('<span class="phrase">',data1)
start = m.end()
end = m.end()+300

new1 = data1[start:end]
#print(new1)

m = re.search('</span>',new1)
end = m.start()
new2 = new1[:end]

print(new2)
