# -*- coding: utf-8 -*-

import requests

from base.base_singleton import BaseSingleton
from common.logger import logger


class BaseRequests(metaclass=BaseSingleton):
    def get(self, url, params=None, **kwargs):
        r"""Sends a GET request.

        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary, list of tuples or bytes to send
            in the query string for the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
        request_information = f"""============ 接口请求信息 ============
        url:{url}
        params: {params}
        kwargs: {kwargs}
            """
        logger.info(request_information)
        resp = requests.get(url, params=params, **kwargs)
        response_information = f"""============ 接口返回信息 ============
        status_code: {resp.status_code}
        response_text: {resp.text}
            """
        logger.info(response_information)
        return resp

    def post(self, url, data=None, json=None, **kwargs):
        r"""Sends a POST request.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json data to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
        request_information = f"""============ 接口请求信息 ============
    url:{url}
    data: {data}
    json: {json}
    kwargs: {kwargs}
        """
        logger.info(request_information)
        resp = requests.post(url, data=data, json=json, **kwargs)
        response_information = f"""============ 接口返回信息 ============
    status_code: {resp.status_code}
    response_text: {resp.json()}
        """
        logger.info(response_information)
        return resp
