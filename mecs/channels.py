import numpy as np
import matplotlib.pyplot as plt
import logging
from constants import *

channel_info = {
    LTE : {'bw': [],
        'max_coverage':[],
        'up': 75*MBPS,
        'down': 300*MBPS
    },WIFI : {'bw': [],
        'rate':135*MBPS
    },BT : {'bw': [],
        'rate': 22*MBPS
    },NFC : {'bw': [],
        'rate': 212*KBPS
    },WIRED : {'bw': [],
        'rate': 5*GBPS
    }
}

logger = logging.getLogger(__name__)

def get_channel_info (channel, info = 'rate', index = 0, uplink=True):
    if info == 'bw':
        return channel_info[channel]['bw']

    if channel == LTE:
        if uplink:
            return channel_info[channel]['up']
        else:
            return channel_info[channel]['down']
    else:
        return channel_info[channel]['rate']


# values = plt.hist(np.random.rayleigh(3, 100000), bins=200, normed=True)
# plt.show()
#
# meanvalue = 1
# modevalue = np.sqrt(2 / np.pi) * meanvalue
# s = np.random.rayleigh(modevalue, 1000000)

# Rayleigh distribution에서 채널게인 샘플 생성
def channel_model(model_name="Rayleigh", sample_number=1000):
    def rayleigh(scale):
        return np.random.rayleigh(scale, sample_number)
    # def rician(scale):
    #     return np.random.rayleigh(scale, sample_number)
    if model_name == "Rayleigh":
        logger.info('Rayleigh channel model with %d samples' % (sample_number))
        return rayleigh
    # elif model_name == "Rician":
    #     logger.info('Rician channel model with %d samples' % (sample_number))
    #     return rician
    else:
        logger.warning("Rayleigh or Rician is possible. Default is Rayleigh")
        return rayleigh


# 대역폭, 백색소음파워, 거리, 송신파워, 채널게인, 거리 exponent, Encoding에 따른 SNR_margin 설정
# def compute_rate(BW, noise_power, distance, tx_power, channel_gain, beta=3.5, SNR_margin=1):
#     rate = BW*np.log2(1+tx_power*channel_gain**2/(SNR_margin*noise_power*distance**beta))
