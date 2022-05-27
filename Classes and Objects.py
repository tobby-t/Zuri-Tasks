class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
    def show(self):
        print( 'The student name is',self.name,',', 'he is',self.age,',', 'his tracks are: ',self.tracks, 'and he got',self.score, 'in his last test.')
    def change_name(self, new_name):
        self.name = str(new_name)
    def change_age(self, new_age):
        self.age = int(new_age)
    def add_track(self, new_tracks):
        self.tracks.append(new_tracks)
    def get_score(self):
        return self.score
        
        
        

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

Bob.show()

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

Bob.show()
 
