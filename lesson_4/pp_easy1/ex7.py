import random

class Oracle:
    def predict_the_future(self):
        return f'You will {random.choice(self.choices())}.'

    def choices(self):
        return [
            'eat a nice lunch',
            'take a nap soon',
            'stay at work late',
            'adopt a cat',
        ]

class RoadTrip(Oracle):
    def choices(self):
        return [
            'visit Vegas',
            'fly to Fiji',
            'romp in Rome',
            'go on a Scrabble cruise',
            'get hopelessly lost',
        ]
    
trip = RoadTrip()
print(trip.predict_the_future())

# In this case RoadTrip will call the inherited predict_the_future method which will
# intern call its own choices method when self.choices() is reached. If no such method
# exists in RoadTrip, then it would fall back to Oracles choices method.