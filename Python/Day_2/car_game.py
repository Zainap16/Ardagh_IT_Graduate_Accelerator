command =''

while command.lower() != 'quit':
    command = input('>').lower()
    if command.lower() == 'start':
        print('Car started...')
    elif command.lower() == 'stop':
        print('Car stopped')
    elif command.lower() == 'help':
        print('start - to start car')
        print('stop - to stop car')
        print('quit - exit program')
    elif command.lower() == 'quit':
        print('program shutting down...')
        break 
    else:
        print('invalid text')
    
 