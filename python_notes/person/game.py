from character import Superhero

superhero1 = Superhero("Bruce Wayne", "Batman")
superhero1.set_power("Rich")

print(f"{superhero1.real} is actually the superhero {superhero1.alias} and his super power is being {superhero1.powers}")

superhero1.get_power()
