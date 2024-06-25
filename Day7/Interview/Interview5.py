class AnimalShelter:
    def __init__(self):
        self.dog_queue = [] 
        self.cat_queue = []
        # thời gian đến của động vật
        self.timestamp = 0 

    #Khi thêm động vật mới
    def enqueue(self, animal_type):
        # tăng thời gian thêm 1
        self.timestamp += 1
        if animal_type == "dog":
            self.dog_queue.append((animal_type, self.timestamp))
        elif animal_type == "cat":
            self.cat_queue.append((animal_type, self.timestamp))

    def dequeueAny(self):
        if not self.dog_queue and not self.cat_queue:
            return None
        elif not self.dog_queue:
            return self.cat_queue.pop(0)
        elif not self.cat_queue:
            return self.dog_queue.pop(0)
        else:
            dog, cat = self.dog_queue[0], self.cat_queue[0]
            return dog if dog[1] < cat[1] else cat

    def dequeueDog(self):
        if not self.dog_queue:
            return None
        return self.dog_queue.pop(0)

    def dequeueCat(self):
        if not self.cat_queue:
            return None
        return self.cat_queue.pop(0)

shelter = AnimalShelter()
shelter.enqueue("dog")
shelter.enqueue("cat")
shelter.enqueue("dog")
print(shelter.dequeueAny()) 
print(shelter.dequeueCat())
