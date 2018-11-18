class Dineout:
    class Discount:
        def __init__(self, nbrFoods, price):
            self.nbrFoods = nbrFoods
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.foods = {}


    def addDiscount(self, food, nbrOfFoods, price):
        discount = self.Discount(nbrOfFoods, price)
        self.discounts[food] = discount


    def addFoodPrice(self, food, price):
        self.prices[food] = price

    def addFood(self, food):
        if food not in self.prices:
            raise Exception("Bad Food")

        if food in self.foods:
            self.foods[food] += 1
        else:
            self.foods[food] = 1

    def calculateTotal(self):
        total = 0
        for food, cnt in self.foods.items():
            total += self.calculateFoodTotal(food, cnt)
        return total

    def calculateFoodTotal(self, food, cnt):
        total = 0
        if food in self.discounts:
            discount = self.discounts[food]
            if cnt >= discount.nbrFoods:
                total += self.calculateFoodDiscountedTotal(food, cnt, discount)
            else:
                total += self.prices[food] * cnt
        else:
            total += self.prices[food] * cnt

        return total

    def calculateFoodDiscountedTotal(self, food, cnt, discount):
        total = 0
        nbrOfDiscounts = cnt / discount.nbrFoods
        total += nbrOfDiscounts * discount.price
        remaining = cnt % discount.nbrFoods
        total += remaining * self.prices[food]
        return total
