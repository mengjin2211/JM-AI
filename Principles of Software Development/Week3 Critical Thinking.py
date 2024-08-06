"""prototype for a mobile shopping app.
preliminary architectural design
key screens for a paper prototype  
Use Python to write a script that will print out the names and number of pages in your prototype and the sequence 
or flow of the pages. 
********** 
Basic functionality: Users can create, edit, and view shopping lists.
Platform: Mobile (iOS or Android)
Data storage: Local device  
Tool: Lucidchart, ppt, paper schetches
https://lucid.app/lucidchart/9573b0aa-7ee5-4846-af4b-2edc3fc9cb35/edit?viewport_loc=669%2C-517%2C2886%2C1416%2C0_0&invitationId=inv_2926ed7a-6005-4429-a484-0e8f8aff2c7e
"""

prototype_pages = [
    "Main Screen",
    "Shopping List Screen",
    "Create List Screen",
    "View List Screen",
    "Edit List Screen", 
    "Add Item Screen",
    "Edit Item Screen",
    "Delete Item Screen"]


page_flow = [ 
    ("Main Screen", "Shopping List Screen"),
    ("Shopping List Screen", "Create List Screen"),
    ("Shopping List Screen", "Edit List Screen"), 
    ("Shopping List Screen", "View List Screen"),
    ("Edit List Screen", "Edit Item Screen"),
    ("Edit List Screen", "Add Item Screen"),
    ("Edit List Screen", "Delete Item Screen"),
]
def colorFormat():
        """Define font color as a private and static method independant of instances."""
        colorCode = {
        'red': "\033[31m",
        'green': "\033[32m",
        'magenta': "\033[35m",
        'cyan': "\033[36m",
        'blue': "\033[34m",
        'reset': "\033[0m"}
        return colorCode

def print_prototype_info(pages, flow):
    print("\nMobile App Prototype Pages:\n",'*'*10)
    maxlength= max(len(page) for page in prototype_pages)
    #for page, number in pages.items():
    for number, page in enumerate(prototype_pages):
        print(f"{page:<{maxlength}}: Page {number+1}")

    print("\nPage Flow:\n",'*'*10)
    maxlength2= max(len(page[0]) for page in page_flow)
    color= colorFormat() 
    for i in flow:
        if i[0]=='Main Screen':
            print(f"{color['blue']} {i[0]:<{maxlength2}} --> {i[1]} {colorFormat()['reset']}")
        elif i[0]=='Shopping List Screen':
            print(f"{color['green']} {i[0]:<{maxlength2}} --> {i[1]} {colorFormat()['reset']}")
        elif i[0]=='Edit List Screen':
            print(f"{color['magenta']} {i[0]:<{maxlength2}} --> {i[1]} {colorFormat()['reset']}")
        else:
            print(f" {i[0]:<{maxlength2}} --> {i[1]} {colorFormat()['reset']}")
    print("\nBack to Main\n",'*'*10)
print_prototype_info(prototype_pages, page_flow)

 