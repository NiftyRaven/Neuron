# from satorineuron import spoof
from satorineuron import config
from satorilib import logging
from satorineuron.init import engine
# from satorilib.api.wallet import RavencoinWallet
from satorilib.api.disk import Cache  # Disk
Cache.setConfig(config)
logging.setup(level=logging.WARNING)

VERSION = '0.1.21'
MOTO = 'Let your workings remain a mystery, just show people the results.'
