import logging

logging.basicConfig(filename='demo03.log' , level=logging.DEBUG , format='%(asctime)s - %(levelname)s - %(message)s')


def namecheck(name):
    if len(name) < 2 :
        logging.debug("Checking for name length")
        return 'Invalid name'
    elif name.isspace():
        logging.debug("cheking for name has Space")
        return 'Invalid name'
    elif name.isalpha() :
        logging.debug("cheking for name is alphabet")
        return 'valid name'
    elif name.replace(' ','').isalpha() :
        logging.debug("Checking for full name")
        return 'name is valid'
    
    else:
        logging.debug("falied all checks")
        return 'Invalid name' 



namecheck("farshid")
namecheck('farshid Hesami')
namecheck('farshid123')
print(result)