import datetime
import json
import serial
import sys
import os

class Tk:

    #//
    #// CONFIG
    #//

    __config = None

    __this_path = os.path.dirname(os.path.realpath(__file__))

    print(__this_path)
    with open( os.path.join( __this_path, '../config/config.json' ) ) as config_file:
        __config = json.load( config_file )

    #// TODO: ALSO READ /ect/sensaweb/node_id AND ADD NODE_ID __config

    @staticmethod
    def get_config( key, default_value ):
        if key in Tk.__config:
             return Tk.__config[ key ]
        return default_value

    #//
    #// LOGGING
    #//

    __log_level = 2
    __log_level_text = [ 'DEBUG', 'INFO', 'WARN',  'ERROR', 'FAULT' ]

    DEBUG = 1
    INFO = 2
    WARN = 3
    ERROR = 4
    FAULT = 5

    @staticmethod
    def __validate_level(level):
        if level<1:
            return 1
        if level>5:
            return 5
        return level

    @staticmethod
    def set_log_level( level ):
        __log_level = Tk.__validate_level( level )

    @staticmethod
    def is_logging(level):
        lev = Tk.__validate_level( level )
        return ( lev >= Tk.__log_level )

    @staticmethod
    def log( msg, level=2 ):
        if Tk.is_logging( level ):
            stm = datetime.datetime.now().strftime( '%Y%m%d.%H%M%S%z' )
            print( stm + ' ' + Tk.__log_level_text[ level-1 ] + ': ' + msg )

    @staticmethod
    def debug( msg ):
        Tk.log( msg, 1 )

    @staticmethod
    def info( msg ):
        Tk.log( msg, 2 )

    @staticmethod
    def warn( msg ):
        Tk.log( msg, 3 )

    @staticmethod
    def error( msg ):
        Tk.log( msg, 4 )

    @staticmethod
    def fault( msg ):
        Tk.log( msg, 5 )

    #//
    #// SERIAL COMMS
    #//

    @staticmethod
    def open_serial( port, baud, timeout=1.0 ):
        try:
            comport = serial.Serial( port, baudrate=baud, timeout=timeout )
            return comport
        except serial.serialutil.SerialException:
            Tk.fault( 'cannot open serial connection, port: {}, baud: {}.'.format( port, baud ) )
            sys.exit(408)

    #//
    #// FILES
    #//

    @staticmethod
    def read_text_file( path ):
        #// # TODO:
        return 'STUFF!'

    @staticmethod
    def write_text_file( path, txt ):
        #// # TODO:
        return
