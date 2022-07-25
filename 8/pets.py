def describe_pet(animal_type, pet_name):
    """Display info about the pet"""
    
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('cat', 'bean')
describe_pet('guinea pig', 'arnold')