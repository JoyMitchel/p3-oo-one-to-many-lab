class Pet:
    # List of allowed pet types
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    # Class variable to store all Pet instances
    all = []

    def __init__(self, name, pet_type, owner=None):
        # Validate pet_type is allowed
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        # Set the pet's name
        self.name = name
        # Set the pet's type
        self.pet_type = pet_type
        # Initialize owner to None
        self.owner = None
        # If an owner is provided, check type and assign
        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an Owner instance")
            self.owner = owner
        # Add this pet instance to the class variable all
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        
        self.name = name

    def pets(self):
      
        return [pet for pet in Pet.all if pet.owner is self]

    def add_pet(self, pet):
        
        if not isinstance(pet, Pet):
            raise Exception("Can only add Pet instances")
        
        pet.owner = self

    def get_sorted_pets(self):
       
        return sorted(self.pets(), key=lambda pet: pet.name)