class animal(object):
    def __init__(self, weight, mood):
        self.weight = weight  # 定義共用屬性
        self.mood = mood

    def dogswalk(self, times):
        self.weight = self.weight-0.2*times
        self.mood = self.mood+times*2

    def dogsfeed(self, times):
        self.weight = self.weight+0.2*times
        self.mood = self.mood+times

    def dogsbath(self, times):
        self.mood = self.mood-2*times


class Dogs(animal):
    def __init__(self, weight, mood):
        super().__init__(weight, mood)


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


class Shiba(animal):
    def __init__(self, weight, mood):
        super().__init__(weight, mood)

    def shifeed(self, times):
        self.weight = self.weight+times*0.3
        self.mood = self.mood+5*times

    def shimood(self):  # self mean inher the class attribute
        if (self.mood > 90):
            print("mood最高只能為90")
            self.mood=90
            print("所以柴犬的心情 ",str(self.mood))
    def shimood2(self):
        if(self.mood<300):
            print("mood最高只能為300")
        
shiba=Shiba(5,70)
shiba.dogswalk(12)
shiba.shifeed(20)
shiba.dogsbath(3)
print("柴犬現在的體重= "+str(shiba.weight)+"kg, 心情 "+str(shiba.mood))
shiba.shimood()
