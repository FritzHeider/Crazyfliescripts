import cflib.crtp
from cflib.crazyflie import Crazyflie
import time

uri = 'radio://0/80/2M'

def log_battery_voltage(timestamp, data, logconf):
    print(f"Battery voltage: {data['pm.vbat']} V")

def main():
    cflib.crtp.init_drivers()
    cf = Crazyflie()
    cf.open_link(uri)
    logconf = LogConfig(name='Battery', period_in_ms=1000)
    logconf.add_variable('pm.vbat', 'float')
    cf.log.add_config(logconf)
    logconf.data_received_cb.add_callback(log_battery_voltage)
    logconf.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        cf.close_link()

if __name__ == "__main__":
    main()
