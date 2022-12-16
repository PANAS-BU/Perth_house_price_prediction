from tkinter import *

#Window 
root = Tk()
root.geometry("600x700")
root.title("Perth House Price Prediction")

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

#Main Heading
mainHeading = Label(root, text="Perth House Price Prediction", font=("Arial", 25), pady=20).pack()

#Land Area
landAreaLabel = Label(root, text="Land Area in Sq ft", font=("Arial", 15), pady=20).pack()
landAreaInput = Entry(root, font=('calibre',12)).pack()

#Floor Area
floorAreaLabel = Label(root, text="Floor Area in Sq ft", font=("Arial", 15), pady=20).pack()
floorAreaInput = Entry(root, font=('calibre',12)).pack()

#Bedrooms
bedroomsLabel = Label(root, text="Bedrooms", font=("Arial", 15), pady=20).pack()
valueInsideBedrooms = StringVar(root)
valueInsideBedrooms.set("Select")
bedroomsMenu = OptionMenu(root, valueInsideBedrooms, *bedroomsCountList).pack()

#Bathrooms
bathroomsLabel = Label(root, text="Bathrooms", font=("Arial", 15), pady=20).pack()
valueInsideBathrooms = StringVar(root)
valueInsideBathrooms.set("Select")
bedroomsMenu = OptionMenu(root, valueInsideBathrooms, *bathroomsCountList).pack()

#Garage
garageLabel = Label(root, text="Garage", font=("Arial", 15), pady=20).pack()
valueInsideGarage = StringVar(root)
valueInsideGarage.set("Select")
bedroomsMenu = OptionMenu(root, valueInsideGarage, *garageCountList).pack()

#Build Year
buildYearLabel = Label(root, text="Build Year", font=("Arial", 15), pady=20).pack()
valueInsideBuildYear = StringVar(root)
valueInsideBuildYear.set("Select")
bedroomsMenu = OptionMenu(root, valueInsideBuildYear, *buildYearCountList).pack()

#Prediction
Label(root, pady= 10).pack()
predictButton = Button(root, text='Predict', bd='5', command = root.destroy).pack()
predictionBox = Entry(root, font=('calibre',12)).pack()

#Main Loop
root.mainloop()