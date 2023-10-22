# Евгения Ширманова, 9я когорта - Финальный проект. Инженер по тестированию
import sender_stand_request
import data

track = sender_stand_request.post_create_new_order(data.order_body).json()["track"]
def get_order_body():
    current_body = data.order_body
    return current_body

# Создание заказа и проверка
def create_order():
    order_body = get_order_body()
    order_response = sender_stand_request.post_create_new_order(order_body)
    assert order_response.status_code == 201
    assert order_response.json()["track"] != ""

create_order()

# Проверка кода при получении заказа
def positive_asserts(track):
    order_response = sender_stand_request.get_order_with_track(track)
    assert order_response.status_code == 200
def test_pickup_order_with_track():
    positive_asserts(track)

test_pickup_order_with_track()


