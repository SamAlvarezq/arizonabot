import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token="vk1.a.qdAOKw1KKaWG3hGxqh8XO88lojUcdVik54lRk2E1hRp-Dzv2C4OVM423wI-MfvAkbZ7fAlHz2KNpbmPoiO43I3SIjDUUi9g41233q6cu0KtbpKkOfwRYIG3v-pz2d1Q1a67tiH5q_zhkqVcc9udJi2rInBh2eCSwxpuRcWk1annpiml62vFUhdqo9mocjbfM")
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def send_some_msg(id, some_text):
    vk_session.method("messages.send", {"user_id":id, "message":some_text,"random_id":0})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            if msg == "start":
                send_some_msg(id, "👾 Привет, друг. Для подробной информации напиши INFO ")
            if msg == "info":
                send_some_msg(id, "💥 Если тебя интересует информация по админ-правам напиши ADM ")
                send_some_msg(id, "👽 Если тебя интересует информация по лидерским правам напиши LID ")
                send_some_msg(id, "🥶 Если тебя интересует информация по донату напиши DON ")
                send_some_msg(id, "🥳 Если у тебя возникла проблема в игровом процессе напиши FORUM ")
            if msg == "adm":
                send_some_msg(id, "👿 Хочешь стать админом? Напиши в лс - https://vk.com/purplesandy ")
            if msg == "lid":
                send_some_msg(id, "😏 Желаешь занять лидерский пост? Заходи в игру и ожидай объявления администратора. ")
            if msg == "don":
                send_some_msg(id, "💚 Хочешь задонатить или есть вопросы по донату? Напиши в лс - https://vk.com/purplesandy ")
            if msg == "forum":
                send_some_msg(id, "😘 Нужна помощь или у тебя есть предложение по игре? Обращайся на наш форум - forum.arizonasunland.ru ")

