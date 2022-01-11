# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def func1():


    if list(Drink) == []:
            print("Out of Stock now, please wait for restock")

    else:
     print(
        "Please select service \nPress (1) Buying Drinks \nPress (2) Refill Stock & Add New Stock \nPress (3) Remove Brand\nPress (4) Edit The Price\nPress (5) Exit ")
     num = int(input())

     (switch(num))
def End():
    return
def Price():

    print(ShowPrice)
    print("Choose to edit Price for the Brand")
    Str = input("Enter Brand to edit :")

    print("Now Price of the", Str,ShowPrice[Str])
    print("Please input Price for new Brand")
    NewPrice = float(input())
    ShowPrice[Str] ="RM" "{:.2f}".format(NewPrice)
    Price[Str] = NewPrice
    print(ShowPrice)
    func1()

    return
def Buying():
    print(ShowPrice)



    print("Please insert the money ?")
    coin = float(input())
    print("Now you have RM",coin)
    Pick = input("Which Drink you choose to buy ?")

    while Pick not in Drink:
            Pick = input("Drink out of stock or Invalid Input please pick another drink ?")


    else:
         print("take your drink")
    Drink[Pick] = Drink[Pick] - 1
    Out = float(Price[Pick])
    if Drink[Pick] == 0:
            del Drink[Pick]
            del Price[Pick]
            del ShowPrice[Pick]

    change =float( coin - Out)
    fivesen= int(change/0.5)
    twentysen=int((change - (fivesen * 0.5) )/0.2)
    tensen=(change %2)
    print("get coin RM0.50 x",int(fivesen),"RM0.20 x",int(twentysen),"RM0.10 x",int(tensen))



    func1()
    return
def Delete():
    print(Drink)
    Str = input("Enter Brand to Delete :")

    del Drink[Str]
    del Price[Str]
    del ShowPrice[Str]
    print(Drink)
    func1()
    return


def Restock(current=None):
    print(Drink)
    if (len(Drink)) == 10:
        print("Full of Brand space, cant not add more brand until it have empty space")
        func1()

    Str = input("Enter Brand of refill stock :")
    print(Str)
    print("Enter Stock of refill stock for", Str)

    quantiti = int(input())
    try:
        if Drink[Str] != None:
            Drink[Str] = quantiti + Drink[Str]
        else:

           Drink[Str] = quantiti
    except KeyError:

        Drink[Str] = quantiti


    print(Drink)


    try:
        if Price[Str] == None:
           func1()
        else:
            print("Restock done")

    except KeyError:

        print("Please input Price for new Brand")
        NewPrice = float(input())
        ShowPrice[Str] = "RM" "{:.2f}".format(NewPrice)
        Price[Str] =(NewPrice)
    func1()
    return




def default():
    print ("Incorrect input,please try again")

    num = int(input())
    (switch(num))
    return


switcher = {
    1: Buying,
    2: Restock,
    3: Delete,
    4: Price,
    5: End



}


def switch(service):
    return switcher.get(service, default)()
ShowPrice = {'100plus':"RM" "{:.2f}".format(2.00), 'cola':"RM" "{:.2f}".format(2.50)}
Drink = {'100plus': 2, 'cola': 1}
Price = {'100plus':2.00, 'cola':2.50}
func1()
