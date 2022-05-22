import requests
import vk_api
from vk_tokens import alex

vk = vk_api.VkApi(token=alex())
peer_id = 2000000004

def check(day):
    message = vk.method("messages.getHistory", {"peer_id": peer_id, "count": 7}).get("items")
    num = 0
    for i in message:
        message_text = message[num].get("text")
        if day in message_text:
            check_ = False
            break
        else:
            check_ = True
        num = num + 1
    return check_

def check_on_site(url):
    req = requests.get(url)
    if str(req.status_code) == "200":
        check_on_site_status = True
    else:
        check_on_site_status = False
    return check_on_site_status