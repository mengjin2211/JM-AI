 
from abc import ABCMeta, abstractmethod

class TraitBuilder(metaclass=ABCMeta):
    "The Abstract Builder Interface for good traits in software engineers"
    @abstractmethod
    def team_work():
        """Works well with others helping team members."""

    @abstractmethod
    def attention_to_detail():
        """Carefully reviewing code and specifications to ensure accuracy and identify issues."""

    @abstractmethod
    def resilience_under_pressure():
        """Manages pressure so that his performance does not suffer."""
 
class DeveloperTraitBuilder(TraitBuilder):
    "The Concrete Builder for Traits." 
    def __init__(self):
        self.trait = SoftwareEngineerTrait()

    def team_work(self):
        message=TraitBuilder.team_work.__doc__
        self.trait.traits['Team Work']=message
        return self

    def attention_to_detail(self):
        message=TraitBuilder.attention_to_detail.__doc__
        self.trait.traits['Attention To Detail']=message
        return self

    def resilience_under_pressure(self):
        message=TraitBuilder.resilience_under_pressure.__doc__
        self.trait.traits['Resilience']=message
        return self

    def get_result(self):
        return self.trait

class SoftwareEngineerTrait():
    "The Product"
    def __init__(self):
        self.traits = {}

class TraitDirector:
    "The Director for constructing the object using builder."
    @staticmethod
    def construct():
        return DeveloperTraitBuilder()\
            .team_work()\
            .attention_to_detail()\
            .resilience_under_pressure()\
            .get_result()

def main():
    # The Client
    Trait = TraitDirector.construct()
    print("\nExcellent Developer Traits:")
    for PersonalTrait, Description in Trait.traits.items():
        print(f'{PersonalTrait:<20}: {Description}')
    # Descriptions of important steps
    print("\nImportant Steps in the Program:")
    steps = [
        "Create a TraitBuilder class as Builder Interface.",
        "Implement a DeveloperTraitBuilder class as Concrete Builder, inheriting from the Builder Interface.",
        "Implement a SoftwareEngineerTrait class as Product, which represents the object.",
        "Implement a TraitDirector class as Director, which constructs the object with the builder.",
        "Create a Software Developer Trait instance in the main function.",
        "Print the traits of the SoftwareDeveloper instance."
    ]
    for num, step in enumerate(steps, start=1):
        print(f'{num}. {step}')

if __name__=="__main__":
    main()