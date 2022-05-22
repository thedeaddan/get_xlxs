import datetime
import requests
import vk_api
import urllib
import time
from rich.traceback import install
install()

from excel_get import get_xlsx
from checks import check, check_on_site
#My lib for VK_Tokens
from vk_tokens import alex

vk = vk_api.VkApi(token=alex())
peer_id = 2000000004


days = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье",
]


def normal_state():
    d = datetime.date.today()
    import pendulum
    tomorrow = pendulum.tomorrow('Europe/Moscow').format('DD')
    if tomorrow == 1:
        day = tomorrow
        month = d.month
        month =int(month)+1
    else:
        month = d.month
        day = d.day 

    month = str(month)

    if len(month) == 1:
        month = "0"+month

    for i in range(day+1, 32):
        if len(str(i)) == 1:
            i = "0"+i
        url = (f"http://spo-ket.ru/sites/default/files/{i}_{month}_2022.xlsx")
        if check_on_site(url):
            day_nums = datetime.datetime(2022,int(month),int(i)).weekday()
            day_week = days[day_nums]
            if check(day_week):
                urllib.request.urlretrieve(url, "/driveone/excel/file.xlsx")
                message = get_xlsx()
                if message == False:
                    print(f"{i}.{month}|{day_week} - Есть измененка, но не на нас, уведомляю")
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": peer_id,
                            "random_id": 0,
                            "message": "#"
                            + day
                            + "\n"
                            + "На нас изменёнки нет(((",
                        },
                    )
                else:
                    print(f"{i}.{month}|{day_week} - Есть измененка, и её ещё нет в беседе, отправляю")
                    vk.method( "messages.send",{"peer_id": peer_id,"random_id": 0,"message": "#" + day_week + "\n" + message})

while True:
    normal_state()
    time.sleep(5)