from art import logo
print (logo)

    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
   

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 



#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']







def caesar(direction_func,user_message, nr_of_shifts):
  message ="" 
  if(direction_func == "decode"):
        nr_of_shifts *=-1 #new position
     
  for letter in user_message:
    if letter in alphabet:
      index = alphabet.index(letter) #position
      position =index + nr_of_shifts
      new_letter = alphabet[position]
      message = message + new_letter
    else:
    
      message = message + letter
      
          

  print(f"User message = {user_message}")
  print (f"shift = {nr_of_shifts}")
  print(f"{direction_func} = {message}")
  print(f'print output: "The {direction_func} text is {message}"')
  run = input("Do you want to run again the program?")
  if(run =="no"):
    run_again = False
  else:
    run_again = True
    print ("Good bye")

  
run_again = True
while(run_again):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift  = shift % 26
  caesar(direction_func=direction,user_message=text, nr_of_shifts=shift)