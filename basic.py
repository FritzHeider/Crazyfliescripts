import cflib.crtp
from cflib.crazyflie import Crazyflie

uri = 'radio://0/80/2M'  # Update URI to match your setup

def connection_callback(link_uri):
    print(f"Connected to {link_uri}")

def main():
    cflib.crtp.init_drivers()
    cf = Crazyflie()
    cf.connected.add_callback(connection_callback)
    cf.open_link(uri)

    try:
        while True:
            pass
    except KeyboardInterrupt:
        cf.close_link()

if __name__ == "__main__":
    main()
