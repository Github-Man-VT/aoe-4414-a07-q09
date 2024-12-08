## Script Name: max_bitrate.py

## Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz

## Parameters:
# tx_w: Transmission power, in W
# tx_gain_db: Transmission gain, in db
# freq_hz: Transmission frequency, in Hz
# dist_km: Distance, in km
# rx_gain_db: Reciever gain, in db
# n0_j: Some random value?
# bw_hz: Bandwith, in Hz

## Output: Determines the maximum achievable bitrate given several input parameters

## Written by Carl Hayden

## Importing Libraries
import math
import sys # argv

## Defining Constants
LLoss = 1
LAtmo = 1

## Initialize Script Arguments
tx_w = float('nan')
tx_gain_db = float('nan')
freq_hz = float('nan')
dist_km = float('nan')
rx_gain_db = float('nan')
n0_j = float('nan')
bw_hz = float('nan')

## Parse Script Arguments
if len(sys.argv)==8:
    tx_w = float(sys.argv[1])
    tx_gain_db = float(sys.argv[2])
    freq_hz = float(sys.argv[3])
    dist_km = float(sys.argv[4])
    rx_gain_db = float(sys.argv[5])
    n0_j = float(sys.argv[6])
    bw_hz = float(sys.argv[7])

else:
    print(\
        'Usage: '\
        'python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
    )
    exit()

## Main Script

C = tx_w * LLoss * tx_gain_db * ((freq_hz / (4*math.pi*dist_km))**2) * LAtmo * rx_gain_db
N = n0_j * bw_hz

r_max = bw_hz * math.log2((1 + C/N)) * 1e-6 # Note: r_max given in Mbps, as noted by the 1*e-6

print(math.floor(r_max))