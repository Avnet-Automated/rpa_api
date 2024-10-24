import pyodbc
import logging

def getConnection(tier, database):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    if tier == 'RMR':
        server = 'CIS2090VMSQL' 
        username = 'SCDevApp1' 
        password = '456Sc@pps#' 
    elif tier == 'QMR':
        server = 'CIS2449VMSQL' 
        username = 'SCTestApp1' 
        password = '456Sc@pps#' 
    elif tier == 'PMR':
        server = 'CIS2517PRDAAAG1'
        username = 'SCPrdApp1'
        password = '#PRODSC5781@pp'
    else:
        raise Exception(tier +  ' is not valid.')
    
    try:
        conn = pyodbc.connect('Driver={SQL Server};Server='+server+';Database='+database+';UID='+username+';PWD='+ password+';', autocommit=True)
    except Exception as e:
        logger.error({'error': server + ' Database Connection failed', 'message': e.args})
        print("Error: %s" %e)
        raise Exception(server + ' DB Connection failed.')
    
    return conn

def getDbConnection(tier, server, database, user, password):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.info("Connecting to database tier: " + tier)

    try:
        conn = pyodbc.connect('Driver={SQL Server};Server='+server+';Database='+database+';UID='+user+';PWD='+ password+';', autocommit=True)
    except Exception as e:
        logger.error({'error': server + ' Database Connection failed', 'message': e.args})
        print("Error: %s" %e)
        raise Exception(server + ' DB Connection failed.')
    
    return conn