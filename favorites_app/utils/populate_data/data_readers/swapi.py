import os
from urllib.parse import urljoin
import requests


SWAPI_END_POINT = os.environ["SWAPI_END_POINT"]


class SwapiReader(object):

    def __init__(self, url_path, num_of_pages):
        self._end_point = SWAPI_END_POINT
        self._url_path = url_path
        self._num_of_pages = num_of_pages
        self._session = requests.session()
        self._headers = {}
        self.result = []
        self._serializer = None

    def get_end_point(self):
        return self._end_point

    def get_num_of_pages(self):
        return self._num_of_pages

    def get_session(self):
        return self._session

    def get_url_path(self):
        return self._url_path

    def get_url(self):
        return urljoin(self.get_end_point(), self.get_url_path())

    def get_page_url(self, page_num):
        return urljoin(self.get_url(), page_num)

    def set_result(self, result):
        self.result = result

    def get_result(self):
        return self.result

    def get_serializer(self):
        return self._serializer


    def fetch_page(self, url):
        response = self.get_session().get(url, headers=self._headers).json()
        return response

    def get_data(self):
        result = []
        response = self.get_session().get(self.get_url(), headers=self._headers).json()
        next_url = response.get("next")
        result.extend(response.get("results", []))
        while next_url:
            response = self.fetch_page(next_url)
            next_url = response.get("next")
            result.extend(response.get("results", []))
        self.set_result(result)
        return self.get_result()

    def save_to_db(self):
        if not self.result:
            raise Exception("No data found")
        if self.get_serializer() is None:
            print(self.get_serializer())
            raise Exception("No Serializer class found")
        serialized_data = self.get_serializer()(data=self.result, many=True)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()




