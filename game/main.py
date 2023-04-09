import random

# options = ('piedra', 'papel', 'tijera')

user_wins = 0
computer_wins = 0

rounds = 0


def start_header(user_wins=0, computer_wins=0, rounds=0):
  print('\n')
  print('****' * 10)
  print('ROUND', rounds)
  print('****' * 10)
  print('\n')
  print('El user va ==> ', user_wins)
  print('La compu va ==> ', computer_wins)
  print('\n')


def choose_option():
  options = ('piedra', 'papel', 'tijera')
  computer_option = random.choice(options)
  # print('la opcion de la compu es => ' + computer_option)
  user_option = input('piedra, papel o tijera ==> elige una opción ')
  user_option = user_option.lower()
  
  if not user_option in options:
    print('Boludo elegí algo de acá: ', options)
    #continue
    return None, computer_option    
  
  print('User options ==> ', user_option)
  print('Computer options ==> ', computer_option)
  return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):

  if user_option == None:
    print(' Copate y escribí bien nabo ! !')
  if user_option == computer_option:
    print('Empataron chicos !')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('gano el user')
      user_wins += 1
    else:
      print('Papel gana a piedra')
      print('Gano la computadora')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'tijera':
      print('Papel PIERDE con la tijera')
      print('Gano la computadora')
      computer_wins += 1
    else:
      print('Piedra PIERDE con papel')
      print('Gano el user')
      user_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('Tijera gana a papel')
      print('Gano el user')
      user_wins += 1
    else:
      print('Piedra gana a tijera')
      print('gano la compu')
      computer_wins += 1
  return user_wins, computer_wins

  
while True:
  rounds += 1
  start_header(user_wins, computer_wins, rounds)
  user_option, computer_option = choose_option()
  user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
  
  if computer_wins == 2:
    print('\n' * 2)
    print ('El ganador total es LA COMPU')
    print('\n' * 2)
    break
  
  if user_wins == 2:
    print('\n' * 2)
    print ('El ganador total fuiste TU')
    print('\n' * 2)
    break

print('-------------------- se acabo-----------' + '\n \n')




