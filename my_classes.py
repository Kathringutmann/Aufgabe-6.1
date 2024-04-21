import json

class Person:
    def __init__(self, first_name, last_name, sex, age, phone_number=None, max_hr=None):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.phone_number = phone_number
        self.max_hr = max_hr
        self.__dict__ = vars(self)  #das dict Attribut enthält automatisch alle Atribute eines Objekts als dictionary

    def estimate_max_hr(self):    #Methode
        """
        See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/ for different formulas
        """
        if self.gender == "male":
            max_hr_bpm = 223 - 0.9 * self.age
        elif self.gender == "female":
            max_hr_bpm = 226 - 1.0 * self.age
        else:
            # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = int(input("Enter maximum heart rate:"))
        return int(max_hr_bpm)

    def save(self, filename): #die Methode Save ermöglicht, die Attribute der Objekte als JSON in eine datei zu speichern
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)
            
            
class Experiment: 
    def __init__(self,experiment_name ,experiment_number , date, supervisor, subject):
        self.experiment_name =  experiment_name   #Attribute
        self.experiment_number = experiment_number
        self.date = date
        self.supervisor = supervisor
        self.subject = subject
        self.__dict__ = vars(self)
        
    def to_dict(self):   #das Objekt in ein Dictionary konvertiert, indem sie das __dict__-Attribut zurückgibt
        return self.__dict__
        
    def save(self, filename):   #Methode
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)
            

# Erstellen Sie ein Objekt der Experiment-Klasse
experiment = Experiment("Experiment 1", 1, "2023-04-21", "Supervisor 1", Person("John", "Doe", "male", 30))

# Rufen Sie die to_dict()-Methode auf dem Objekt auf
print(experiment.to_dict())
