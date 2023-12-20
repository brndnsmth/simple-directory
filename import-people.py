# If not using included db:
# Add entries to the database.
# Execute the script or enter python shell:
# python manage.py shell
# Copy and execute the following into the shell.

from directory.models import Person

people_data = [
    ("Alex", "White", "Can mimic animal sounds better than a wildlife documentary."),
    ("Sophia", "Taylor", "Has an encyclopedic knowledge of obscure 80s movie quotes."),
    ("Ethan", "Davis", "Once tried to teach a goldfish to play chess."),
    ("Olivia", "Martinez", "Master of creating puns that make people both laugh and cringe."),
    ("Aiden", "Brown", "Collects more comic books than a superhero museum."),
    ("Ava", "Smith", "Can turn a quiet bookstore into a karaoke party."),
    ("Logan", "Johnson", "Approaches cooking like a mad scientist conducting delicious experiments."),
    ("Emma", "Miller", "Expresses emotions through a series of perfectly-timed GIFs."),
    ("Noah", "Garcia", "Attempts at DIY projects result in abstract home decor."),
    ("Isabella", "Robinson", "Predicts rain with a more accurate knee than a barometer.")
]

for first_name, last_name, biography in people_data:
    person = Person.objects.create(first_name=first_name, last_name=last_name, biography=biography)
    print('Person Created', f"{person.first_name} {person.last_name}")
