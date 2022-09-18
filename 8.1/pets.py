def describe_pet(anuimal_type, pet_name):
    """Display information about the pet."""
    print(f"\nI have a {anuimal_type}.")
    print(f"My {anuimal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'pico')