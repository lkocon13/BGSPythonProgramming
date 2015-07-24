➊ birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

   while True:
       print('Enter a name: (blank to quit)')
       name = input()
       if name == '':
           break

➋     if name in birthdays:
➌         print(birthdays[name] + ' is the birthday of ' + name)
       else:
           print('I do not have birthday information for ' + name)
           print('What is their birthday?')
           bday = input()
➍         birthdays[name] = bday
           print('Birthday database updated.')
