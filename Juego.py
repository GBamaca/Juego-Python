import random
print('Bienvenidos al juego de adivinar numeros') 
# Initialise the number to be guessed 
number_to_guess = random.randint(1,10) 
# Initialise the number of tries the player has made 
count_number_of_tries = 1 
# Obtain their initial guess 
guess = int(input('Inserta un numero del 1 al 10: ')) 
while number_to_guess != guess: 
    print('Te equivocaste intenta de nuevo') 
    # Check to see they have not exceeded the maximum 
    # number of attempts if so break out of loop otherwise
    # give the user come feedback 
    if count_number_of_tries == 4: 
        break
    elif guess < number_to_guess: 
        print('Intenta con un numero mas alto') 
    else: 
        print('Intenta con un numero mas bajo') 

    # Obtain their next guess and increment number of attempts 
    guess = int(input('Intenta adivinar de nuevo: ')) 
    count_number_of_tries += 1 
# Check to see if they did guess the correct number 
if number_to_guess == guess: 
 print('Bien hecho, Ganaste!') 
 print('Usaste', count_number_of_tries , 'para completar el juego.') 
else: 
 print("Lo siento Perdiste") 
 print('El numero que necesitabas era...', 
 number_to_guess) 
print('Perdiste!') 
