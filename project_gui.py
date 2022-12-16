from tkinter import *
import project

#functions
def predict():
    #Land Area Value
    landAreaValue = landAreaInput.get()
    landAreaValue = float(landAreaValue)

    #Floor Area Value
    floorAreaValue = floorAreaInput.get()
    floorAreaValue = float(floorAreaValue)

    #Bedrooms Count
    bedroomsMenuValue = valueInsideBedrooms.get()
    bedroomsMenuValue = int(bedroomsMenuValue)

    #Bathrooms Count
    bathroomsMenuValue = valueInsideBathrooms.get()
    bathroomsMenuValue = int(bathroomsMenuValue)

    #Garage Count
    garageMenuValue = valueInsideGarage.get()
    garageMenuValue = int(garageMenuValue)

    #Build Year
    buildYearMenuValue = valueInsideBuildYear.get()
    buildYearMenuValue = int(buildYearMenuValue)

    predictedValue = project.model(landAreaValue, floorAreaValue, bedroomsMenuValue, bathroomsMenuValue, garageMenuValue, buildYearMenuValue)

    predictedValue = float(predictedValue)

    predictionBoxVar.set(predictedValue)
    print(predictedValue)

#Window 
root = Tk()
root.geometry("600x750")
root.title("Foretell.AI")

#Variables, Lists
bedroomsCountList = ["Select",1,2,3,4,5,6,7,8,9,10]
bathroomsCountList = ["Select",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

garageCountList = []
for i in range(1,101):
    garageCountList.append(i)
garageCountList.insert(0, "Select")

buildYearCountList = []
for i in range(1868, 2021):
    buildYearCountList.append(i)
buildYearCountList.insert(0, "Select")

predictionBoxVar = StringVar()

#Main Heading
mainHeading = Label(root, text="Perth House Price Prediction", font=("Arial", 25), pady=20).pack()

#Land Area
landAreaLabel = Label(root, text="Land Area in Sq ft", font=("Arial", 15), pady=20).pack()
landAreaInput = Entry(root, font=('calibre',12))
landAreaInput.pack()

#Floor Area
floorAreaLabel = Label(root, text="Floor Area in Sq ft", font=("Arial", 15), pady=20).pack()
floorAreaInput = Entry(root, font=('calibre',12))
floorAreaInput.pack()

#Bedrooms
bedroomsLabel = Label(root, text="Bedrooms", font=("Arial", 15), pady=20).pack()
valueInsideBedrooms = StringVar(root)
valueInsideBedrooms.set("Select")
bedroomsMenu = OptionMenu(root, valueInsideBedrooms, *bedroomsCountList)
bedroomsMenu.pack()

#Bathrooms
bathroomsLabel = Label(root, text="Bathrooms", font=("Arial", 15), pady=20).pack()
valueInsideBathrooms = StringVar(root)
valueInsideBathrooms.set("Select")
bathroomsMenu = OptionMenu(root, valueInsideBathrooms, *bathroomsCountList)
bathroomsMenu.pack()

#Garage
garageLabel = Label(root, text="Garage", font=("Arial", 15), pady=20).pack()
valueInsideGarage = StringVar(root)
valueInsideGarage.set("Select")
garageMenu = OptionMenu(root, valueInsideGarage, *garageCountList)
garageMenu.pack()

#Build Year
buildYearLabel = Label(root, text="Build Year", font=("Arial", 15), pady=20).pack()
valueInsideBuildYear = StringVar(root)
valueInsideBuildYear.set("Select")
buildYearMenu = OptionMenu(root, valueInsideBuildYear, *buildYearCountList)
buildYearMenu.pack()

#Prediction
Label(root, pady=5).pack()
predictButton = Button(root, text='Predict', bd='5', command=predict).pack()

predictionBox = Entry(root, textvariable=predictionBoxVar, font=('calibre',12))
predictionBox.pack(pady=20)

#Main Loop
root.mainloop()