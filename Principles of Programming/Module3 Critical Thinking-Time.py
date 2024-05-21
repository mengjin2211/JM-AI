"""
Ask for time now and time delta to wait for alarm. Calculate the time alarm will go off in 24-hour format.
Approach: 
Use datetime module to calculate and display future time calculated from two inputs: hour and time delta from user. Use try and except to handle input errors.  

Challenges: 
•	It was challenging to convert user input from integer to standard time format. I do not want to make users to type in the standard date time "%Y-%m-%d %H:%M:%S" which is complex & prone to error. I only asked for two digit integer representing the hours. Solution was the combine function, taking in today’s date and concatenate the date with the user input time.
•	Just when I thought I was done, I found out I didn’t check the hour input range 0-24. 
 
•	Experimented where to place if statement to check 0-23 hour range and keywords such as “continue”, “break” and “return”.   
"""
#from datetime import datetime, time, timedelta 
import datetime
def alarm_time():
    
    while True:
        try:
            input1=input("Enter the time now in 24 hour format. 2 digit integers please.") 
            input1=int(input1)
            if input1>23:
                print ("Hour entry exceeding max. Enter an integer 0-23.")
                continue
            elif input1<0:
                print ("Hour entry less than 0. Enter an integer 0-23.")
                continue
            else:break
        except ValueError:
            print ("Invalid input. Please input integer only")
            continue
        
    now=datetime.time(input1, 0, 0)
    today=datetime.datetime.now().date()
    date_time = datetime.datetime.combine(today, now)
    print ("Current datetime is: ", date_time )
    input2=input("Enter the hours to wait for alarm. Integers only please.") 
    new_time = date_time + datetime.timedelta(hours=int(input2))
    print ("Alarm will go of at: ",new_time)

if __name__ == "__main__": alarm_time()

