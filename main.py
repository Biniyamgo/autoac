''' A script to send all messages from one chat to another. '''

import asyncio
from audioop import reverse
from configparser import ConfigParser
from socks import SOCKS5, SOCKS4, HTTP
import logging
import time
from telethon.tl.patched import MessageService
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon import TelegramClient
from telethon.sessions import StringSession
from settings import API_ID, API_HASH, forwards, get_forward, STRING_SESSION
from keep_alive import keep_alive

#logging.basicConfig(
#format='%(asctime)s - %(name)s - %(levelname)s - %##(message)s', level=logging.INFO)

SENT_VIA = f'\n__Sent via__ `{str(__file__)}`'


def intify(string):
  try:
    return int(string)
  except:
    return string


async def forward_job():
  ''' the function that does the job 😂 '''
  if STRING_SESSION:
    session = StringSession(STRING_SESSION)
  else:
    session = 'forwarder'

  async with TelegramClient(
      'user',
      API_ID,
      API_HASH,
      # proxy={
      #   'proxy_type': 'socks5',
      #   'addr': '156.251.248.93',
      #   'port': 33446,
      # },
  ) as client:

    confirm = ''' IMPORTANT 🛑
            Are you sure that your `config.ini` is correct ?

            Take help of @userinfobot for correct chat ids.
            
            Press [ENTER] to continue:
            '''

    #input(confirm)
    count = 0
    value = True

    # timeout variable can be omitted, if you use specific value in the while condition
    #timeout = 519000 # [seconds]

    #timeout_start = time.time()

    while (value):
      error_occured = False
      number = [5]
      for num in number:
        for forward in forwards:
          from_chat, to_chat, offset = get_forward(forward)

          if not offset:
            offset = 0

          last_id = 0

          async for message in client.iter_messages(intify(from_chat)):
            if isinstance(message, MessageService):
              continue

            try:

              #print(message.id, 'binii')
              if message.id == num:

                await client.forward_messages(intify(to_chat), message)
                last_id = str(message.id)

                #logging.info('forwarding message with id = %s', last_id)

              # update_offset(forward, last_id)

            except FloodWaitError as fwe:
              #print(f'{fwe}')
              asyncio.sleep(delay=fwe.seconds)
            except Exception as err:
              #logging.exception(err)
              error_occured = True
              break

        count += 1
        #print('post for', count, 'time')
        delaytime = 1
        for i in range(1, delaytime):
          time.sleep(1)
    await client.send_file(
      'me',
      'config.ini',
      caption='This is your config file for telegram-chat-forward.')

    message = 'Your forward job has completed.' if not error_occured else 'Some errors occured. Please see the output on terminal. Contact Developer.'
    await client.send_message('me',
                              f'''Hi !
        \n**{message}**
        \n**Telegram Chat Forward** is developed by @AahnikDaw.
        \nPlease star 🌟 on [GitHub](https://github.com/aahnik/telegram-chat-forward).
        {SENT_VIA}''',
                              link_preview=False)


keep_alive()
if __name__ == "__main__":

  assert forwards
  asyncio.get_event_loop().run_until_complete(forward_job())
