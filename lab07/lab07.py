class animal(object):
    def __init__(self, weight, mood):
        self.weight = weight  # 定義共用屬性
        self.mood = mood
 
 
class Dogs(animal):
    def __init__(self, weight, mood):
        super().__init__(weight, mood)
 
    def dogswalk(self, times):
        self.weight = self.weight-0.2*times
        self.mood = self.mood+times*2
 
    def dogsfeed(self, times):
        self.weight = self.weight+0.2*times
        self.mood = self.mood+times
 
    def dogsbath(self, times):
        self.mood = self.mood-2*times
 
 
class Cats(animal):
    def __init__(self, weight, mood):
        super().__init__(weight, mood)
 
    def catswalk(self, times):
        self.weight = self.weight-0.1*times
        self.mood = self.mood-times
 
    def catsfeed(self, times):
        self.weight = self.weight+0.1*times
        self.mood = self.mood+times
 
    def catsbath(self, times):
        self.mood = self.mood-2*times
 
 
dog=Dogs(4.8,65)
dog.dogswalk(10)
dog.dogsbath(4)
dog.dogsfeed(18)
print("狗狗現在體重= "+str(dog.weight)+"kg, 心情 "+str(dog.mood))
cat=Cats(8.2,60)
cat.catswalk(7)
cat.catsfeed(40)
cat.catsbath(1)
print("貓貓現在體重= "+str(cat.weight)+"kg, 心情 "+str(cat.mood))
