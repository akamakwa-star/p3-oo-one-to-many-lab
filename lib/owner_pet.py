# lib/owner_pet.py

class Pet:
    # Allowed types of pets
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    # Class variable to store all Pet instances
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = None
        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("owner must be an instance of Owner")
            self.owner = owner
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    # Return all pets that belong to this owner
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    # Add a pet to this owner
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("add_pet expects a Pet instance")
        pet.owner = self

    # Return pets sorted by name
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
