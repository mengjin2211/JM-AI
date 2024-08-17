class Actor:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class UseCase:
    def __init__(self, name, description):
        self.name = name
        self.description = description

actors = [
    Actor("Citizen", "Users who report potholes and damages"),
    Actor("Employee", "Public Works Employee managing pothole reports and work orders"),
    Actor("Crew", "Workers repairing the potholes and updating status")
]

use_cases = [
    UseCase("Report Pothole", "Citizen reports a pothole"),
    UseCase("Report Damage ", "Citizen reports damage as optional part of the Pothole Report"),
    UseCase("Damage File", "Viewed by Employee"),
    UseCase("Generate Work Order", "Employee creates work order"),
    UseCase("Assign Work Order ", "Crew works on the assigned order"),
    UseCase("Update Pothole Status", "Crew updates pothole status"),
    UseCase("View Pothole Status ", "Citizen and Employee view status")
]

flow=["Citizen reports pothole and includes damage if applicable."
      ,"The report trigger the creation of a work order."
      ,"Employee reviews pothole report and damage report to determine priority and assignment."
      ,"Employee generates a work order"
      ,"The work order is assigned to a crew."
      ,"Crew repairs the pothole and updates the pothole status."
      ,"Citizen and Employee view the pothole status."
      ]

def print_diagram_description():
    print("\nPHTRS Use Case Diagram Description\n","*"*20)
    print("\nActors:")
    for actor in actors:
        print(f"- {actor.name}: {actor.description}")
    
    print("\nUse Cases:")
    for use_case in use_cases:
        print(f"- {use_case.name}: {use_case.description}")
    
    print("\nDescription of the flow:")
    for i, j in enumerate(flow, start=1):
        print (f'Step {i} {j}')

if __name__=="__main__":

    print_diagram_description()
    print('\n',"*"*20) 