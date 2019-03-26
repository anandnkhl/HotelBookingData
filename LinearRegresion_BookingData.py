'''
Created on 27-Jun-2018

@author: Nikhil Anand
'''
import pymongo
from pymongo import MongoClient
import numpy as np
from statistics import mean
import matplotlib.pyplot as plt

client = MongoClient("mongodb+srv://anandnkhl:anandnkhl@bookingwebsite-uhoaf.mongodb.net/test?retryWrites=true")
db = client["BookingWebsite"]
collection = db["BookingData"]

class Slope():
    def best_fit(self, xs, ys):
        m = ((mean(xs) * mean(ys)) - mean(xs * ys)) / ((mean(xs)**2) - mean(xs**2))
        C = mean(ys) - m*mean(xs)
        return m,C
    
class Age():
    age = [20,30,40,50,60]
    age = np.array(age, dtype = np.float64)
    yesnum = []
    nonum = []
    predicted_yesnum = []
    predicted_nonum = []
    for low in age:
        counter1 = counter2 = 0
        query1 = { "Age": { "$gte": low, "$lte": low+9 }, "$and": [ { "Booked": "YES" } ] }
        ageyes = collection.find(query1,{"Age" : 1, "Booked" : 1, "_id" : 0})
        query2 = { "Age": { "$gte": low, "$lte": low+9 }, "$and": [ { "Booked": "NO" } ] }
        ageno = collection.find(query2,{"Age" : 1, "Booked" : 1, "_id" : 0})
        for fields1 in ageyes :
            counter1 += 1
        for fields2 in ageno :
            counter2 += 1
        yesnum.append(counter1)
        nonum.append (counter2)
    print(yesnum, nonum)
    yesnum = np.array(yesnum, dtype = np.float64)
    nonum = np.array(nonum, dtype = np.float64)
    
    obj = Slope()
    
    m1,C1 = obj.best_fit(age, yesnum)
    m2,C2 = obj.best_fit(age, nonum)
    
    for i in range(len(age)) :
        predicted_yesnum.append ((m1*age[i]) + C1)
    predicted_yesnum = np.array(predicted_yesnum, dtype = np.float64)
    for i in range(len(age)) :
        predicted_nonum.append ((m2*age[i]) + C2)
    predicted_nonum = np.array(predicted_nonum, dtype = np.float64)
    
    f1 = plt.figure(1)
    plt.xlabel('Age')
    plt.ylabel('Booked {Red-> No ; Green -> Yes}')
    plt.scatter(age, yesnum , s=50, color = "green")
    plt.plot(age, predicted_yesnum , color = "green")
    plt.scatter(age, nonum , s=50, color = "red")
    plt.plot(age, predicted_nonum , color = "red")
#     plt.show()
    
class HotelStar():
    hotelstar = [2,3,4,5]
    hotelstar = np.array(hotelstar, dtype = np.float64)
    yesnum = []
    nonum = []
    predicted_yesnum = []
    predicted_nonum = []
    
    for star in hotelstar:
        counter1 = counter2 = 0
        query1 = { "HotelStar": star, "$and": [ { "Booked": "YES" } ] }
        staryes = collection.find(query1,{"HotelStar" : 1, "Booked" : 1, "_id" : 0})
        query2 = { "HotelStar": star, "$and": [ { "Booked": "NO" } ] }
        starno = collection.find(query2,{"HotelStar" : 1, "Booked" : 1, "_id" : 0})
        for fields1 in staryes :
            counter1 += 1
        for fields2 in starno :
            counter2 += 1
        yesnum.append(counter1)
        nonum.append (counter2)
    print(yesnum, nonum)
    yesnum = np.array(yesnum, dtype = np.float64)
    nonum = np.array(nonum, dtype = np.float64)
    
    obj = Slope()
    
    m1,C1 = obj.best_fit(hotelstar, yesnum)
    m2,C2 = obj.best_fit(hotelstar, nonum)
    
    for i in range(len(hotelstar)) :
        predicted_yesnum.append ((m1*hotelstar[i]) + C1)
    predicted_yesnum = np.array(predicted_yesnum, dtype = np.float64)
    for i in range(len(hotelstar)) :
        predicted_nonum.append ((m2*hotelstar[i]) + C2)
    predicted_nonum = np.array(predicted_nonum, dtype = np.float64)
    
    f2 = plt.figure(2)
    plt.xlabel('Hotel Star')
    plt.ylabel('Booked {Red-> No ; Green -> Yes}')
    plt.scatter(hotelstar, yesnum , s=50, color = "green")
    plt.plot(hotelstar, predicted_yesnum , color = "green")
    plt.scatter(hotelstar, nonum , s=50, color = "red")
    plt.plot(hotelstar, predicted_nonum , color = "red")
#     plt.show()

class Season():
    season = [1,2,3]
    season = np.array(season, dtype = np.float64)
    yesnum = []
    nonum = []
    predicted_yesnum = []
    predicted_nonum = []
    
    for seasons in {"LOW","MEDIUM","HIGH"}:
        counter1 = counter2 = 0
        query1 = { "Season": seasons, "$and": [ { "Booked": "YES" } ] }
        seasonyes = collection.find(query1,{"HotelStar" : 1, "Booked" : 1, "_id" : 0})
        query2 = { "Season": seasons, "$and": [ { "Booked": "NO" } ] }
        seasonno = collection.find(query2,{"HotelStar" : 1, "Booked" : 1, "_id" : 0})
        for fields1 in seasonyes :
            counter1 += 1
        for fields2 in seasonno :
            counter2 += 1
        yesnum.append(counter1)
        nonum.append (counter2)
    print(yesnum, nonum)
    yesnum = np.array(yesnum, dtype = np.float64)
    nonum = np.array(nonum, dtype = np.float64)
    
    obj = Slope()
    
    m1,C1 = obj.best_fit(season, yesnum)
    m2,C2 = obj.best_fit(season, nonum)
    
    for i in range(len(season)) :
        predicted_yesnum.append ((m1*season[i]) + C1)
    predicted_yesnum = np.array(predicted_yesnum, dtype = np.float64)
    for i in range(len(season)) :
        predicted_nonum.append ((m2*season[i]) + C2)
    predicted_nonum = np.array(predicted_nonum, dtype = np.float64)
    
    f2 = plt.figure(3)
    plt.xlabel('Season { 1->Low; 2->Medium; 3->High }' )
    plt.ylabel('Booked {Red-> No ; Green -> Yes}')
    plt.scatter(season, yesnum , s=50, color = "green")
    plt.plot(season, predicted_yesnum , color = "green")
    plt.scatter(season, nonum , s=50, color = "red")
    plt.plot(season, predicted_nonum , color = "red")
#     plt.show()

class Price():
    price = [2000, 3000, 4000, 5000, 6000]
    price = np.array(price, dtype = np.float64)
    yesnum = []
    nonum = []
    predicted_yesnum = []
    predicted_nonum = []
    for low in price:
        counter1 = counter2 = 0
        query1 = { "Price": { "$gte": low, "$lte": low+999 }, "$and": [ { "Booked": "YES" } ] }
        priceyes = collection.find(query1,{"Age" : 1, "Booked" : 1, "_id" : 0})
        query2 = { "Price": { "$gte": low, "$lte": low+999 }, "$and": [ { "Booked": "NO" } ] }
        priceno = collection.find(query2,{"Price" : 1, "Booked" : 1, "_id" : 0})
        for fields1 in priceyes :
            counter1 += 1
        for fields2 in priceno :
            counter2 += 1
        yesnum.append(counter1)
        nonum.append (counter2)
    print(yesnum, nonum)
    yesnum = np.array(yesnum, dtype = np.float64)
    nonum = np.array(nonum, dtype = np.float64)
    
    obj = Slope()
    
    m1,C1 = obj.best_fit(price, yesnum)
    m2,C2 = obj.best_fit(price, nonum)
    
    for i in range(len(price)) :
        predicted_yesnum.append ((m1*price[i]) + C1)
    predicted_yesnum = np.array(predicted_yesnum, dtype = np.float64)
    for i in range(len(price)) :
        predicted_nonum.append ((m2*price[i]) + C2)
    predicted_nonum = np.array(predicted_nonum, dtype = np.float64)
    
    f1 = plt.figure(4)
    plt.xlabel('Price {Amounts in INR}')
    plt.ylabel('Booked {Red-> No ; Green -> Yes}')
    plt.scatter(price, yesnum , s=50, color = "green")
    plt.plot(price, predicted_yesnum , color = "green")
    plt.scatter(price, nonum , s=50, color = "red")
    plt.plot(price, predicted_nonum , color = "red")
    plt.show()
    