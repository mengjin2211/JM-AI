
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

