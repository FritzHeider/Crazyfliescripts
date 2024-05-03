import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.commander import Commander
import time

uri = 'radio://0/80/2M'
hover_height = 0.5  # meters

def main():
    cflib.crtp.init_drivers()
    cf = Crazyflie()
    cf.open_link(uri)
    commander = Commander(cf)
    time.sleep(3)  # Give it some time to connect

    commander.take_off(hover_height, 0.3)
    time.sleep(5)  # Hover for 5 seconds
    commander.land(0.0, 0.3)
    time.sleep(1)

    cf.close_link()

if __name__ == "__main__":
    main()
