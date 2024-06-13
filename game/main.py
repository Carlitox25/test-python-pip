import random

def chooseOption():
  options = ('piedra', 'tijera', 'papel')
  userOption = input('Escoge entre Piedra, Papel o Tijera => ')
  userOption = userOption.lower()

  if userOption not in options:
    return None, None
  
  computerOption = random.choice(options)
  print('Jugador escogió: ', userOption)
  print('Computadora escogió: ', computerOption)

  return userOption, computerOption


def checkRules(userOption, computerOption, userWins, computerWins):
  if userOption == computerOption:
    print('Empate!')
    
  elif userOption == 'piedra':
      if computerOption == 'papel':
        print('Papel gana a Piedra')
        print('Computadora gana!')
        computerWins += 1
        
      else :
        print('Piedra gana a Tijera')
        print('Jugador gana!')
        userWins += 1
        
  elif userOption == 'papel':
    if computerOption == 'piedra':
      print('Papel gana a Piedra')
      print('Juagador gana!')
      userWins += 1
      
    else :
      print('Tijera gana a Papel')
      print('Computadora gana!')
      computerWins += 1
      
  elif userOption == 'tijera':
    if computerOption == 'piedra':
      print('Piedra gana a Tijera')
      print('Computadora gana!')
      computerWins += 1
      
    else:
      print('Tijera gana a Papel')
      print('Jugador gana!')
      userWins += 1
      
  score(computerWins, userWins)
  return userWins, computerWins

def score(computerWins, userWins):
  print ('')
  print("*"*15)
  print('Victorias computadora: ', computerWins)
  print('Victorias Jugador: ', userWins)
  print ('')
  return 

def runGame():
  rounds = 1
  userWins = 0
  computerWins = 0
  while True:
    

    print ('')
    print("*"*15)
    print('Ronda', rounds)
    print("*"*15)
    print ('')
    
    rounds += 1
    userOption, computerOption = chooseOption()
    if userOption == None:
      print('Opción no valida, vuelva a intentarlo')
      rounds -= 1
    else:
      userWins, computerWins = checkRules(userOption, computerOption, userWins, computerWins)

    if computerWins == 3:
      print ('')
      print("*"*15)
      print('El ganador de la partida es la Computadora')
      break
    if userWins == 3:
      print ('')
      print("*"*15)
      print('El ganador de la partida es el Jugador')
      break
      
runGame()
