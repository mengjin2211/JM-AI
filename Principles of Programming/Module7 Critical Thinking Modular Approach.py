
class course_DB:
    """Define course information dictionaries."""
    def __init__(self):
        self.room={'CSC101': 3004, 'CSC102': 4501, 'CSC103': 6755, 
                'NET110': 1244, 'COM241': 1411}
        self.instructor={'CSC101': 'Haynes', 'CSC102': 'Alvarado', 'CSC103': 'Rich', 
                'NET110': 'Burke', 'COM241': 'Lee'}
        self.course_time={'CSC101': '8:00 a.m.', 'CSC102': '9:00 a.m.', 'CSC103': '10:00 a.m.', 
                'NET110': '11:00 a.m.', 'COM241': '1:00 p.m.'}

    def courseInfo (self, course_num):
        """Get user input with error handling. Print the course info with colors."""   

        if (course_num in self.room) or (course_num in self.instructor) or (course_num in self.course_time):
            return  self.room[course_num], self.instructor[course_num], self.course_time[course_num]
        else: 
            return None, None, None

def colorFormat():
    """Define font color dictionary."""
    colorCode = {
    'red': "\033[31m",
    'green': "\033[32m",
    'bold': "\033[1m",
    'blue': "\033[34m",
    'reset': "\033[0m"}
    return colorCode

def course_input():
    """Manage input of the course number."""
    is_valid = False 
    while not is_valid:
        try:
            print('Welcome to CSU Global Course Information Database.')
            course_num=input('Please enter a course number (in the format CSC111): ').upper()
            is_valid = True
            if len(course_num)!=6:
                print('Please enter exactly 6 characters: 3 letters of course name followed by 3 digit course number without space.')
                is_valid = False
            if not course_num[:3].isalpha():
                print('The first three characters should be alphabetic.')
                is_valid = False
            if not course_num[-3:].isdigit():
                print('The last three characters should be numerical.')
                is_valid = False
                continue
        except ValueError:
            print('ValueError. Please enter course number in the exact format as example CSC111.')
            is_valid = False
            continue
    return course_num

def print_course_info(room, instructor, course_time, course_num,color):
    
    if room or instructor or course_time:   # If a course exists in any dict(room or instructor or time), display the course.
        
        print(f"Course information for {color['bold']}{course_num}{color['reset']}\n"
            f"{color['red']}Room Number: {room}{color['reset']}\n"
            f"{color['green']}Instructor: {instructor}{color['reset']}\n"
            f"{color['blue']}Course Time: {course_time}{color['reset']}")       
    else: 
        print(f"Course {color['red']}{course_num}{color['reset']} not found in the curriculum or is not offered in the current term.\n")


def main():
    color=colorFormat()
    courses= course_DB() #create instance of the course database class
    keep_searching=True 
    while keep_searching:
        course_num=course_input() #obtain course number from user       
        room, instructor, course_time=courses.courseInfo(course_num) #calling the method of the course database instance to unpack course info.
        print_course_info(room, instructor, course_time, course_num,color)  # print function using all above variables as input.
        keep_searching=input('Do you want to search for another course? (Y/N) ').strip().upper()
        if keep_searching!='Y':
            keep_searching=False
            print('Exiting course search. Thank you for using CSU Global Course Database.\n')
            break


if __name__ == "__main__": main ()