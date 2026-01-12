# a0.py

# Starter code for assignment 0 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Juliet Wang
# Julietw2@uci.edu
# 65183805

#main method
def main():
    #user input
    n = int(input())
    #draws rectangles
    def pattern():
        #loops based on input of # of rectangles
        for i in range(n):
            #indents based on i 
            ind = " " * i 
            #prints shape
            print(ind + "+-+")
            print(ind + "| |")
            print(ind + "+-+")
    pattern()

if __name__ == "__main__":
    main()
