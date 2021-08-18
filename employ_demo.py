import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s - %(name)s - %(message)s')

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)



class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property  
    #allow to access attr without putting setter or getter everywhere,
    #but if we need that functionality then it's easy to add in with the property decorator,
    #and if we do this correctly than people using our class won't even need to change any of their code 
    #becoz they'll still be able to access those attr in the same way that they did before
     
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Jim', 'Walker')
emp_2 = Employee('Pam', 'Smith')
emp_3 = Employee('Mikcal', 'Harward')
if __name__=="__main__":
    logger.info("hello world")
    logger.debug("root logger")
