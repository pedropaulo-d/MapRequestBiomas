import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from threading import Thread
import time

def get_water_url():
    url = 'https://dev-agua.geodatin.com/api/surface/map/monthly/2022/12?dataType=water'
    response = requests.get(url)
    return response.json()['url']

class WaterURLView(APIView):
    def get(self, request, format=None):
        return Response({"url": get_water_url()})

    def start_background_thread(self):
        while True:
            # espera 5 horas
            time.sleep(5 * 60 * 60)
            # atualiza a URL
            self.water_url = get_water_url()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.water_url = get_water_url()
        # inicia uma thread para atualizar a URL a cada 5 horas
        thread = Thread(target=self.start_background_thread)
        thread.daemon = True
        thread.start()