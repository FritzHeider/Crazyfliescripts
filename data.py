import cflib.crtp
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie import Crazyflie
import time

uri = 'radio://0/80/2M'

def log_stabilizer_data(timestamp, data, logconf):
    with open('sensor_data.txt', 'a') as file:
        file.write(f"{timestamp}, {data['acc.x']}, {data['acc.y']}, {data['acc.z']}\n")

def main():
    cflib.crtp.init_drivers()
    cf = Crazyflie()
    cf.open_link(uri)
    logconf = LogConfig(name='Stabilizer', period_in_ms=100)
    logconf.add_variable('acc.x', 'float')
    logconf.add_variable('acc.y', 'float')
    logconf.add_variable('acc.z', 'float')
    cf.log.add_config(logconf)
    logconf.data_received_cb.add_callback(log_stabilizer_data)
    logconf.start()

    try:
        while True:
            time.sleep(1)
    except
