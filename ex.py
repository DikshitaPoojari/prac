import logging
import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard':{
            'format': '%(levelname)s - %(name)s - %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
        'file':{
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': 'ex.log',
            'maxBytes': 1024,
            'backupCount':3,
        },
        
    },
    'loggers': {
        'model1': {
            #root logger
            'handlers': ['file', 'default'],
            'level': 'DEBUG',
            'propogate': True,
            'format': 'standard',
            

        },
    },
}
logging.config.dictConfig(LOGGING_CONFIG)



if __name__=="__main__":
    log = logging.getLogger('model1')
    log.info("hello world")
    log.debug("root logger")