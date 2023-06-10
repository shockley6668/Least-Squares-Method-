import csv
import numpy as np
import matplotlib.pyplot as plt
import math
WHEEL_RADIUS = 0.05
odom_x = 0
odom_y = 0
odom_yaw=0
last_enc = [0 for _ in range(4)]
real_x=0
real_y=0
errx=[]
erry=[]
realVx=[]
realVy=[]
enVx=[]
enVy=[]
rawEnVx=[]
rawEnVy=[]
t=0.01
csv_writer = csv.writer(f)
with open('new.csv') as csv_file:
    row = csv.reader(csv_file, delimiter=',')
    next(row)  # 读取首行
    encoder = []  # 建立一个数组来存encoder
    last_enc = [0 for _ in range(4)]
    for r in row:
        w = [0, 0, 0, 0]
        encoder.append(float(r[4]))
        encoder.append(float(r[5]))
        encoder.append(float(r[6]))
        encoder.append(float(r[7]))
        Vx = float(r[1])
        Vy = float(r[2])
        for i in range(4):
            if (encoder[i] - last_enc[i] > 3.14):
                w[i]=( encoder[i] - 2 * 3.1415926 - last_enc[i])
            elif (encoder[i] - last_enc[i] < -3.14):
                w[i]=( encoder[i] + 2 * 3.1415926 - last_enc[i])
            else:
                w[i]=( encoder[i] - last_enc[i])
        rawdx = (w[0] + w[1] + w[2] + w[3]) * WHEEL_RADIUS / 4
        rawdy = (-w[0] + w[1] + w[2] - w[3]) * WHEEL_RADIUS / 4
        rawEnVx.append(rawdx)
        rawEnVy.append(rawdy)
        w[0] = 0.98284149 * (w[0] - 0.004916151)
        w[1] = 0.98708168 * (w[1] + 0.00114977)
        w[2] = 0.98601081 * (w[2] - 0.000181461)
        w[3] = 0.98734884 * (w[3] - 0.004097596)
        last_enc = encoder
        encoder = []
        dx = (w[0] + w[1] + w[2] + w[3]) * WHEEL_RADIUS / 4
        dy = (-w[0] + w[1] + w[2] - w[3]) * WHEEL_RADIUS / 4
        vx=Vx/100
        vy=Vy/100
        realVx.append(vx)
        realVy.append(vy)
        enVx.append(dx)
        enVy.append(dy)
        errx.append(dx-vx)
        erry.append(dy-vy)
plt.plot(realVy, label='realVy')
plt.plot(enVy, label='enVy')
plt.plot(rawEnVy, label='rawEnVy')
plt.legend()
plt.show()
print('errx平均值',np.mean(errx))
print('errx标准差',np.std(errx,ddof=1))
print('erry平均值',np.mean(erry))
print('erry标准差',np.std(erry,ddof=1))

