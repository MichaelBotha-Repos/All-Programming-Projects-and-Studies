import logging

logging.basicConfig(
                    filename = 'c:/users/michael botha/desktop/log.log',
                    level = logging.DEBUG,
                    format = '%(asctime)s'
                    )

for elem in ['amy', 'michael', 'wesley']:
    print(elem)
    print(logging.info('normal'))

    
