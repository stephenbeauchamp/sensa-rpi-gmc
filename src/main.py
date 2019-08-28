
from toolkit import Tk

serial_port      = Tk.get_config( 'SERIAL_PORT', '/dev/ttyUSB0' )
serial_baud      = Tk.get_config( 'SERIAL_BAUD', 115200 )
serial_timeout   = Tk.get_config( 'SERIAL_TIMEOUT', 1.0 )
run_continuously = Tk.get_config( 'RUN_CONTINUOUSLY', False )
run_interval_sec = Tk.get_config( 'RUN_INTERVAL_SECONDS', 2.5 )
sensor_id        = Tk.get_config( 'SENSOR_ID', '04' )
node_id          = Tk.get_sensa_node_id()

def main():
    Tk.info( "Application Starts [node_id: {}]...".format( Tk.get_sensa_node_id() ) )
    #//
    comport = Tk.serial_open( serial_port, serial_baud, serial_timeout )
    #//
    while Tk.is_running:
        #//
        raw = Tk.serial_command( comport, '<GETCPM>>', 2 )
        if raw=='' or len(raw)<2:
            Tk.error( "cpm reading not valid '{}'".format(val) )
        else:
            val = Tk.convert_msf_unsgned_short_to_string( raw )
            Tk.save_sensa_datafile( node_id, sensor_id, '{:.4f}'.format(val) )
        #//
        if not run_continuously:
            Tk.is_running = False
        if Tk.is_running:
            sleep( run_interval_sec )
    #//
    Tk.info( 'Application Ends...' )
