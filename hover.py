import logging
import time
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crtp.crtpstack import CRTPPort, CRTPPacket  # Import CRTP dependencies
from cflib.utils import uri_helper

# Try importing the init_drivers function directly
from cflib.crtp import init_drivers

# Initialize the low-level drivers
init_drivers()

# URI to the Crazyflie to connect to
uri = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)

def simple_hover(cf, duration, height):
    """
    Simple hover function.
    cf: Crazyflie object
    duration: Hover time in seconds
    height: Height in meters
    """
    try:
        print('Taking off...')
        cf.param.set_value('kalman.resetEstimation', '1')
        time.sleep(0.1)
        cf.param.set_value('kalman.resetEstimation', '0')
        time.sleep(2)  # Wait for the estimator to stabilize

        cf.high_level_commander.takeoff(height, 2.0)
        time.sleep(2 + duration)  # Give it some time to hover
        print('Landing...')
        cf.high_level_commander.land(0.0, 2.0)
        time.sleep(2)  # Time for landing before disconnecting
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
        cf = scf.cf
        # Setting high level commander (required for takeoff and landing)
        cf.high_level_commander.set_group_mask(0)
        
        # Hover the Crazyflie
        simple_hover(cf, 10, 0.5)

if __name__ == '__main__':
    main()
