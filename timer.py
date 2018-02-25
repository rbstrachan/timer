import time

# Asks for start time. Checks validity of input.
start = input("Enter the time you would like to count down from in seconds: ")
if start == "" or str(start).isalpha():
  start = input("\nSorry. Thats not a valid input. Please enter a time in seconds.")

# Asks for end time. Automatically sets time to 0 if no input is given or if input type is incorrect. 
end = input("Enter the time you would like to count down to in seconds: ")
if end == "" or str(end).isalpha():
  end  = 0

# Prints start time. Reduces start time by 1. Waits 1 second. Prints start time. Repeat until start time equal to end time.
print()
while int(start) > int(end):
  print(start, end=' ')
  start = int(start) - 1
  time.sleep(1)
  print("-", end=' ')
print(end)
