import cflib.crtp
from cflib.crazyflie import Crazyflie
import time

uri = 'radio://0/80/2M'

def main():
    cflib.crtp.init_drivers()
    cf = Crazyflie()
    cf.open_link(uri)

    for i in range(10):
        cf.param.set_value('ring.effect', '0')  # Turn off
        time.sleep(0.5)
        cf.param.set_value('ring.effect', '7')  # Solid color
        time.sleep(0.5)

    cf.close_link()

if __name__ == "__main__":
    main()
