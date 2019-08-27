
from toolkit import Tk

serial_port = Tk.get_config( 'SERIAL_PORT', '/dev/ttyUSB0' )
serial_baud = Tk.get_config( 'SERIAL_BAUD', 115200 )
serial_timeout = Tk.get_config( 'SERIAL_TIMEOUT', 1.0 )
run_continuosly = Tk.get_config( 'RUN_CONTINUOUSLY', False )
run_interval_sec = Tk.get_config( 'RUN_INTERVAL_SECONDS', 2.5 )

def main():
    Tk.info( 'Application Starts...' )
    #//
    device = Tk.open_serial( serial_port, serial_baud, serial_timeout )
    while run_continuously:
        #// TODO: Read in values and save to file
        #//
        if run_continuously:
            sleep( run_interval_sec )
    #//
    Tk.info( 'Application Ends...' )
