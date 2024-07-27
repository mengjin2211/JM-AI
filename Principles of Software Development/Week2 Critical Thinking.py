"""Meng Model Implementation with Python Classes
Week2 Critical Thinking Assignment"""
class Requirements:
    def __init__ (self):
        pass
    def gather_requirements(self):
        print("Gathering requirements...")

    def analyze_requirements(self):
        print("Analyzing requirements...")

    def refine_requirements(self):
        print("Refining requirements...")

    def planning(self):
        print("Planning...")

    def get_feedback(self):
        print("Getting feedback...")
    
    def execute_all(self):
        print("\n--> Requirements <--")
        self.gather_requirements()
        self.analyze_requirements()
        self.refine_requirements()
        self.planning()
        self.get_feedback()

class Modeling (Requirements):
    def __init__ (self):
        super().__init__()
         
    def analysis(self):
        
        print("Performing analysis...")

    def design(self):
        print("Designing the system...")

    def prototype(self):
        print("Creating a prototype...")

    def get_feedback(self):
        print("Getting feedback ...")
        
    def execute_all(self):
        super().execute_all()  # Calls Requirements.execute_all()
        print("\n--> Modeling <--")
        self.analysis()
        self.design()
        self.prototype()
        self.get_feedback()

class Construction (Modeling):
    def __init__ (self):
        super().__init__()
    def code(self):
        print("Coding the system...")

    def test(self):
        print("Testing the system...")

    def iterate(self, num=3): 
        print("Iterating coding and testing...")       
        for i in range(0, num):
            print (f'##iteration loop {i+1}##')
            self.code()
            self.test()      

    def risk_analysis(self):
        print("Performing risk analysis...")

    def get_feedback(self):
        print("Getting feedback ...")
    def execute_all(self):
        super().execute_all()  # Calls Modeling.execute_all()
        print("\n--> Construction <--")
        self.risk_analysis()
        self.iterate()
        
        self.get_feedback()

class Deployment (Construction):
    def __init__ (self):
        super().__init__()
    def deploy(self):
        print("Deploying the system...")

    def support(self):
        print("Providing support for the system...")

    def gather_feedback(self):
        print("Gathering feedback...")

    def execute_all(self):
        super().execute_all()  # Calls Construction.execute_all()
        print("\n--> Deployment <--")
        self.deploy()
        self.support()
        self.gather_feedback() 

def Meng_Model(): 
    print("#"*3, 'Modified Waterfall Model', "#"*3)
    Deployment().execute_all()
    print("-" * 50)
    print ("Meng Model enhances Waterfall process by enabling iteration and feedback loops.")
    print("""Meng Model Visualization \n
    \u25CF \u2192 Requirement   
    --> Modeling \u2191(feedback) 
    --> Construction (with iterations)\u21bb \u2191(feedback)
    --> Deployment \u2191(feedback) \n""")
if __name__=='__main__': 
    Meng_Model()

 
