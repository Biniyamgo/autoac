from configparser import ConfigParser
import json
from typing import List
from dotenv import load_dotenv
import os
import logging
# from keep_alive import keep_alive

load_dotenv()
#21129632
API_ID = 10897219
#tse f life 18488809
#tse g life 03deff21f87a1a3d345f57f739b60465
#yoni herbale api the same
#21251941
# moos 12069804
#10897219+
#17421852
#
#os.getenv('api_id')
API_HASH = 'fb627bc739f63f5f61eb2f5667a07445'
#os.getenv('api_hash')
STRING_SESSION = os.getenv('STRING_SESSION')

assert API_ID and API_HASH

configur = ConfigParser()

# groups = [
#   '@sheger1_gebeya', '@Home_Marketo', '@Goldn_mareket', '@bnshopping',
#   '@golden_mareket1', '@marketineg', '@BHP_MARKET_CENTER', '@ethiomarts12',
#   '@Moosmarket10', '@golden_mareket', '@Ethio_fast_market ', '@Ethi0_market',
#   '@ahadumarket12', '@market_0nline', '@sellsgroup', '@market_center21',
#   '@marketcenter11', '@ethioo_markett', '@sinamarket0', '@ethio_Gebeeya',
#   '@norgebeya', '@Maahllet', '@AHADUMARKET122', '@Etmart1', '@samri077',
#   '@zembilshoppingcenter', '@one1_Market', '@habeshamart_et',
#   '@ethio_smart_Market', '@sina_gebeya1'
# ]
groups = [
  '@Expresshop1', '@New_marketdv', '@Esssentstore', '@Express_shooping',
  '@EssentialMarket', '@Merkatoahoppp', '@EliteBallers1', '@kingpromotion1',
  '@kingpromotion2', '@kingpromotion3', '@kingpromotion4',
  '@qualitymarketplaces', '@ethio_smart_Market', '@zembilshoppingcenter',
  '@Etmart1', '@ethioexpres12', '@bnshopping', '@addis_shopp',
  '@AHADUMARKET122', '@EthioEbay12', '@lehulummarket', '@Digital_Market_Team',
  '@ethio_amazon_group2', '@SHEMETAZONE', '@NIGUSMARKET', '@market_0nline',
  '@ahadumarket12', '@shegermarket21', '@norgebeya', '@SHEMETAZONE1',
  '@yetm_yetm12', '@Elkexpress', '@ritimarketing', '@ADVERTISERS_GROUP',
  '@abuuchuu', '@CTech_Promotion_Agency', '@marketineg', '@Gojo_Fashion',
  '@adisssmarket', '@addisMarketBuyAnything2', '@addisgebeyaonline',
  '@Gomarket12', '@abonlinemarket22', '@gulitonlinemarket2', '@enzosStore',
  '@ethio_Gebeeya', '@ethioo_markett', '@golden_mareket1', '@Goldn_mareket',
  '@sina_gebeya1', '@sinamarket0', '@onlineshop_45', '@addisMarketBuyAnything',
  '@etmarketon', '@sartmart'
]

for d in groups:
  title = str(d)
  buna = {
    title: {
      'from': 'https://t.me/seneselasa30',
      'to': d,
      'offset': 1,
    }
  }

  configur.read_dict(buna)

#ConfigParser()
#configur.read()

forwards = configur.sections()


def get_forward(forward: str) -> tuple:
  try:
    from_chat = configur.get(forward, 'from')
    to_chat = configur.get(forward, 'to')
    offset = configur.getint(forward, 'offset')
    return from_chat, to_chat, offset
  except Exception as err:
    print(err)


if __name__ == "__main__":

  #testing
  for forward in forwards:
    print(forward, get_forward(forward))
