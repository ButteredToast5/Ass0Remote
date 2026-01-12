# a0.py

# Starter code for assignment 0 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Juliet Wang
# Julietw2@uci.edu
# 65183805

#main method
def main():
    #user input #of rectangles
    n = int(input())
    
    #draws rectangles
    def pattern():
        #checks if the the program reached the bottom of the last rectangle as a boolean
        lastrow = False
        
        #start of top rectangle
        print("+-+")
        
        #loops based on input of # of rectangles
        for i in range(n):
            #indents based on i 
            ind = "  " * i
            #prints rest of shape
            print(ind + "| |")

            #checks if the the program reached the bottom of the last rectangle
            while lastrow == False:
                print(ind + "+-+-+")
                    if lastrow  == True:
                        print(ind + "+-+")
    #run pattern method
    pattern()

if __name__ == "__main__":
    main()
