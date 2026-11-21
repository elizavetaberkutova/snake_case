import numpy as np

#ціни товарів
prices = np.array([120,250,500,750,1000])
#кількість проданих товарів
quatities = np.array([5, 3, 8, 2, 4 ])
#відсотки
discounts = np.array ([10, 15, 0, 20, 5])

print(prices)
print(quatities)
print(discounts)

def show_info(arr):
    print(arr)
    print(type(arr))
    print(arr.dtype)
    print(arr.shape)
    print(arr.size)
    print(arr.size)

show_info(prices)
show_info(quatities)
show_info(discounts)

#ціна товара
prices = prices*quatities
print(prices)
#відсотки +3%
discounts = discounts+3
print(discounts)

#скідка
prices_discounts = prices * (1 - discounts/100)
print(prices_discounts)

#більше 500
print(prices[prices>500])

#від 200 до 800
print(prices[(prices>=200) & (prices<=800)])

# 500 рівно
print(prices[prices==500])

#<300 | >800
num1 = prices[(prices<300)|(prices>800)]
print(num1)

# 500 ~
num2 = prices[~(prices > 500)]
print(num2)

# >200 та 3 товара
num3 = prices[(prices >200)&(quatities > 3)]
print(num3)

#скидка 20%
discounts_20 = prices * 20/100
print(discounts_20)

#індувід. скидка
individual_discounts = prices * discounts/100
print(individual_discounts)

#ціна після знижки
prices = prices  - individual_discounts
print(prices)

#індексація
print(prices[0])
print(prices[-1])

print(prices[0])
print(prices[-1])
print(prices[-2])

prices[1]=300
print(prices)

print(prices[::-1])

#Зміна масивів
prices = np.append(prices, 1500)
print(prices)

prices = np.insert(prices, 2, 400)
print(prices)

prices = np.delete(prices, 3)
print(prices)
