from mockito import when, mock, unstub
import os

# when(os.path).exists('/foo').thenReturn(True)

# or
import requests
response = mock({'status_code': 200, 'text':'ok'})

when(requests).get(...).thenReturn(response)

requests.get('http://google.com/')

unstub()