import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import settings as env
import os.path

dog_query = 'https://www.oregonhumane.org/adopt/?type=dogs&mode=adv&breed=120'
sms_client = Client(env.ACCOUNT_SID, env.AUTH_TOKEN)

response = requests.get(dog_query)

soup = BeautifulSoup (response.text, 'html.parser')
for result in soup.find_all('div', class_='result-item'):
    for name in result.find('span', {'class': 'name'}) :
        print(name)
        if name == 'Cedar' :
            if not os.path.isfile('/tmp/sent'):
                print('Go get Cedar')
                sms_client.api.account.messages.create(
                    from_='+15034054242',
                    to=env.ANN_CELL,
                    body="Cedar is available at the Oregon Human Society"
                )
                sms_client.api.account.messages.create(
                    from_='+15034054242',
                    to=env.CHRIS_CELL,
                    body="Cedar is available at the Oregon Human Society. sudo get dog"
                )
                open('/tmp/sent', 'a').close()
