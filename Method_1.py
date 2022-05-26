# Start with an empty array

array = [] 


# Function to sort for the biggest element in the array

def reverse_array(array):
  
  # Creating a new array to store the reversed values
  
  reverse_array = []
  
  # The reversing algorithm
  
  for i in range(len(array) - 1 ,-1,-1):
    
    reverse_array.append(array[i])
    
  return reverse_array
  
  
# User input to fill the array

choice = "y"

while True:
  
  
  
  if choice == "y":
    user_input = int(input("Enter a number to app to the array: "))
    array.append(user_input)
    choice = input("Do you wish to continue y/n : ")
    
  else:
    break


# Initiating the function  

print(reverse_array(array))
