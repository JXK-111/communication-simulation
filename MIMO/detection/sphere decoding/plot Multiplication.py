import numpy as np
import matplotlib.pyplot as plt

Nr = 4
constellation_num = 3

if constellation_num == 1:
    constellaion_name = 'QPSK'
elif constellation_num == 2:
    constellaion_name = '16QAM'
elif constellation_num == 3:
    constellaion_name = '64QAM'

if Nr == 2:
    if constellaion_name == 'QPSK':
        snr = [3.010299956639812 ,5.0102999566398125, 7.0102999566398125, 9.010299956639813, 11.010299956639813 ,13.010299956639813, 15.010299956639813, 17.010299956639813, 19.010299956639813 ,21.010299956639813 ,23.010299956639813 ,25.010299956639813 ,27.010299956639813  ]
    if constellaion_name == '16QAM':
        snr = [3.010299956639812, 5.5102999566398125, 8.010299956639813, 10.510299956639813, 13.010299956639813, 15.510299956639813, 18.010299956639813, 20.510299956639813, 23.010299956639813, 25.510299956639813, 28.010299956639813, 30.510299956639813, 33.01029995663981  ]
    if constellaion_name == '64QAM':
        snr = [3.010299956639812, 6.0102999566398125, 9.010299956639813, 12.010299956639813, 15.010299956639813 ,18.010299956639813, 21.010299956639813, 24.010299956639813 ,27.010299956639813 ,30.010299956639813 ,33.01029995663981 ,36.01029995663981 ,39.01029995663981 ]
elif Nr == 4:
    if constellaion_name == 'QPSK':
        snr =  [0.0, 1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0, 13.5, 15.0, 16.5, 18.0]
    if constellaion_name == '16QAM':
        snr = [0.0 ,1.9 ,3.8 ,5.699999999999999 ,7.6 ,9.5 ,11.399999999999999, 13.299999999999999, 15.2, 17.099999999999998, 19.0, 20.9 ,22.799999999999997 ]
    if constellaion_name == '64QAM':
        snr = [0.0, 2.3, 4.6, 6.8999999999999995, 9.2, 11.5, 13.799999999999999, 16.099999999999998, 18.4, 20.7, 23.0, 25.299999999999997, 27.599999999999998]

visit1 = [2056.986374 ,1382.089646 ,932.498158 ,637.273938 ,444.66123 ,316.442674 ,226.103282 ,160.148508 ,112.955426 ,82.99214 ,63.93401 ,53.295064 ,46.606602 ]
plt.plot(snr,visit1,marker = 'o',label='branch=[2,2,4,4,4,4,8,8]'.format(constellaion_name))
visit1 = [3256.799632 ,2133.880366 ,1416.548554 ,963.810098 ,658.253172 ,460.387804 ,322.438044 ,222.54003 ,156.62746 ,110.618864 ,83.937484 ,66.459666 ,55.424052 ]
plt.plot(snr,visit1,marker = 'o',label='branch=[2,2,4,4,6,6,8,8]'.format(constellaion_name))
visit1 = [4322.946738 ,2857.560298 ,1886.757158 ,1272.121402 ,866.668702 ,597.988144 ,410.489694 ,279.433402 ,196.217278 ,140.456076 ,101.692384 ,80.671392 ,66.07663  ]
plt.plot(snr,visit1,marker = 'o',label='branch=[2,2,4,4,8,8,8,8]'.format(constellaion_name))
visit1 = [2675.293328 ,1637.898704 ,1037.583212 ,710.813756 ,492.930072 ,356.448844 ,259.898372 ,186.096536 ,129.256564 ,96.812456 ,76.03458 ,65.57284 ,57.722252 ]
plt.plot(snr,visit1,marker = 'o',label='branch=[4,4,4,4,8,8,8,8]'.format(constellaion_name))


ticks = [0] * 20
for i in range(20):
    ticks[i] = 2 * i
plt.xticks(ticks)
plt.xlim(min(snr) - 1, max(snr) + 1)

plt.xlabel('Eb/No , dB')
plt.ylabel('Multiplication complexity')
plt.grid(True, which='both')
plt.legend()
plt.show()