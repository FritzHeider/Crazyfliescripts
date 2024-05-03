import time
import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.commander import Commander

# URI to the Crazyflie to connect to
uri = 'radio://0/80/2M'

def position_callback(timestamp, data, logconf):
    x = data['stateEstimate.x']
    y = data['stateEstimate.y']
    z = data['stateEstimate.z']
    print(f"Position: x={x}, y={y}, z={z}")

def main():
    cflib.crtp.init_drivers()

    with Crazyflie() as cf:
        cf.open_link(uri)
        print('Connected to Crazyflie')

        # Wait for the Crazyflie to initialize (optional)
        time.sleep(2)

        with Commander(cf) as commander:
            # Take off and hover at 0.5 meters
            commander.take_off(0.5, 0.6)
            time.sleep(3)

            # Move in a square pattern
            for _ in range(4):
                commander.go_to(1, 0, 0.5, 0, 2.0)
                time.sleep(2)
                commander.go_to(1, 1, 0.5, 0, 2.0)
                time.sleep(2)
                commander.go_to(0, 1, 0.5, 0, 2.0)
                time.sleep(2)
                commander.go_to(0, 0, 0.5, 0, 2.0)
                time.sleep(2)

            # Land and disconnect
            commander.land(0.0, 0.6)
            time.sleep(2)

        print('Demo terminated!')

if __name__ == '__main__':
    main()
