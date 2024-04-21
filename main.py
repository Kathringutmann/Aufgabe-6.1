import json

from my_classes import Person, Experiment

def main():
    subject = Person(first_name="John", last_name="Doe", sex="male", age=30, phone_number=123456789, max_hr=180)
    experiment = Experiment(experiment_name="Leistung", experiment_number=2, date="12.24.2342", supervisor="Bob", subject=subject)

    filename = "experiment.json"

    with open(filename, 'w') as outfile:
        json.dump(experiment.to_dict(), outfile, default=lambda o: o.__dict__)

    print(f"Die Experiment- und Versuchsteilnehmerdaten wurden in der Datei '{filename}' gespeichert.")

if __name__ == "__main__":
    main()