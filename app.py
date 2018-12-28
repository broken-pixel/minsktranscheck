import requests, bs4


def hello():
    url = 'https://kogda.by/routes/minsk/'
    type = str(input('Введите желаемый вид транспорта: '))
    if type == 'автобус':
        type = 'autobus/'
        url = url + type
    elif type == 'троллейбус':
        type = 'trolleybus/'
        url = url + type
    elif type == 'трамвай':
        type = 'tram/'
        url = url + type
    return url
def get_number(url):
    number = str(input('Введите номер: '))+'/'
    url = url + number
    return url
def get_station(url):
    stations = []
    count = 0
    response = requests.get(url)
    web_page = response.text
    soup=bs4.BeautifulSoup(web_page, "html.parser") 
    print("Выбери направление из списка:\n1. туда\n2. обратно")
    naprav = int(input())
    naprav-=1
    naprav = str(naprav)
    head = soup.find(attrs={"id":"direction-"+naprav+"-heading"})
    url = url + head.getText().rstrip().lstrip()+'/'
    soup = soup.find(attrs={"id":"direction-"+naprav})
    for i in soup.findAll(attrs={"class":"list-group-item"}):
        stations.append(i.getText().rstrip().lstrip())    
    return url,stations
def gete(url, stops):
    print("Выбери остановку из списка:\n")
    i = 1
    for stop in stops:
        print(str(i)+'.',stop)
        i+=1
    choice = int(input())-1
    url = url+str(stops[choice])
    return url
def get_time(url):
    response = requests.get(url)
    web_page = response.text
    soup = bs4.BeautifulSoup(web_page, "html.parser") 
    time_next = soup.find(attrs={"class":"future"})
    time_pass = soup.find(attrs={"class":"passed"})
    time_next =str(time_next.getText().rstrip().lstrip())
    time_pass = str(time_pass.getText().rstrip().lstrip())
    print('Следующий прибудет в',time_next)
    print('Предыдущий ушел в',time_pass)  
def gettt():
    url = hello()
    url = get_number(url)
    url, stops = get_station(url)
    url = gete(url, stops) 
    get_time(url)
    print('Посмотреть ещё расписание?')
    answ = int(input('1 - да\n2 - нет'))
    if answ == 1:
        gettt()
gettt()