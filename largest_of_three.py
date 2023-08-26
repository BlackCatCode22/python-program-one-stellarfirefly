# Jay C. Parangalan, CIT-95 Fall 2023
# Largest of Three Game

playing_game = True

print( "Largest of Three \"Game\"" )
player_name = input( "Hello, what is your name? " )

# keep track of largest number found so far and check others against it
def nested_ifs( n1, n2, n3 ):
    largest = n1
    if( n2 > largest ):
        largest = n2
    if( n3 > largest ):
        largest = n3
    return largest

# find largest at each check and return it
def compound_ifs( n1, n2, n3 ):
    if( n1 > n2 ) and ( n1 > n3 ):
        return n1
    if( n2 > n1 ) and ( n2 > n3 ):
        return n2
    return n3    # only solution left, no need to keep checking

# used prompt "write me a python function that will find the largest of 3 numbers"
def chatGPT_solution( n1, n2, n3):
    return max(n1, n2, n3)

while playing_game:
    first_number = input( "Enter the first integer: " )
    second_number = input( "Enter the second integer: " )
    third_number = input( "Enter the third integer: " )

    # convert to proper integers
    num1 = int( first_number )
    num2 = int( second_number )
    num3 = int( third_number )
    
    print( "The largest number found using:" )
    print( "\tNested if's:", nested_ifs( num1, num2, num3 ) )
    print( "\tCompound if's:", compound_ifs( num1, num2, num3 ) )
    print( "\tChatGPT's answer:", chatGPT_solution( num1, num2, num3 ) )

    print()
    print( "Thank you for playing,", player_name )
    replay = input( "Enter Q to Quit, or anything else to go again: " )
    if( replay.upper() == "Q" ):
        playing_game = False
    print()

print( "Goodbye", player_name + "!" )

