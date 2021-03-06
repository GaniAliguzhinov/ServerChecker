import re

import requests
from requests.exceptions import ConnectionError, Timeout

from django.utils import timezone

from django.db import models


class Query(models.Model):
    """
    Class that holds both query url and results of the query.
    """
    url = models.TextField(max_length=250)
    exists = models.BooleanField(default=True)
    timeout = models.BooleanField(default=False)
    ipaddress = models.TextField(max_length=250)
    httpcode = models.TextField(max_length=250)
    querytime = models.DateTimeField()

    def __str__(self):
        """
        Convert to string. For now, pack all data into string.
        """
        result = "[" + ("" if self.exists else "Cannot Connect|")
        result += ("Timeout" if self.timeout else "") + "]:\t"
        result += "[" + str(self.querytime.isoformat()) + "]\t"
        result += self.url + " (" + self.ipaddress + ")"
        result += ":\t" + self.httpcode
        return result

    def fixurl(self, url):
        """
        Fix incomplete url: Add http://www. to a malformed url
        """

        if 'www' not in url:
            url = 'www.' + url
        if re.match(r'^[a-zA-Z]+://', url) is None:
            url = 'http://' + url
        return url

    def __init__(self, *args, **kwargs):
        """
        On initialization of a query, execute a request.
        """

        # If no url argument, then initialize empty Object
        # If bad url, do not initialize
        try:
            url = self.fixurl(kwargs['url'])
            print(url)
        except KeyError:
            super().__init__(*args, **kwargs)
            return
        # Initialize url field with a valid url, and time with current time
        kwargs['url'] = url
        kwargs['querytime'] = timezone.localtime()

        # Attempt connection with a long timeout (1s), and set appropriate
        # flags on failure. If connected, write ip and status code to the model
        try:
            response = requests.get(url, timeout=1, stream=True)
        except ConnectionError:
            kwargs['exists'] = False
        except Timeout:
            kwargs['timeout'] = True
        else:
            ip = response.raw._original_response.fp.raw._sock.getpeername()[0]
            kwargs['ipaddress'] = ip
            kwargs['httpcode'] = str(response.status_code)

        super().__init__(*args, **kwargs)
