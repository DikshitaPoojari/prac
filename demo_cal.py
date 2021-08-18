import logging
import employ_demo

# Debug : These are used to give Detailed information, typically of interest only when diagnosing problems.
# Info : These are used to Confirm that things are working as expected
# Warning : These are used an indication that something unexpected happened, or indicative of some problem in the near future
# Error: This tells serious error, indicating that the program itself may be unable to continue running

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(name)s - %(message)s')

file_handler = logging.FileHandler('test.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        logger.exception("Can't divide by Zero")

    else:
        return result

    

num1=10
num2=0

add_result = add(num1,num2)
logger.debug('Add: {} + {} = {}'.format(num1,num2,add_result))

sub_result = sub(num1,num2)
logger.debug('sub: {} + {} = {}'.format(num1,num2,sub_result))

mul_result = mul(num1,num2)
logger.debug('mul: {} + {} = {}'.format(num1,num2,mul_result))

div_result = div(num1,num2)
logging.debug('div: {} + {} = {}'.format(num1,num2,div_result))
