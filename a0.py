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
        
        #start of top rectangle
        print("+-+")
        
        #loops based on input of # of rectangles
        for i in range(n):
            #indents based on i 
            ind = "  " * i
            
            #prints rest of shape
            print(ind + "| |")

    #checks and prints row based on if its part of a rectangle or if its the last line of the last rectangle.
            if i == n - 1:
                print(ind + "+-+-+")#all tops of rectangles
            else:
                print(ind + "+-+")#last line/base of last rectangle
                
    #run pattern method
    pattern()

if __name__ == "__main__":
    main()
