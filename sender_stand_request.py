import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def post_create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)

def get_order_with_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.PICK_UP_ORDER_WITH_TRACK_PATH + str(track))
