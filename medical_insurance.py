# Add your code here
medical_costs={}
medical_costs["Marina"]=6607.0
medical_costs["Vinay"]=3225.0

medical_costs.update({"Connie": 8886.0, "Isaac":16444.0, "Valentina":6420.})
print(medical_costs)

#Vinay's Update
medical_costs["Vinay"]=3325.0
print(medical_costs)

#calculating total Cost
total_cost=0
for u in medical_costs.values():
  total_cost+=u

#Average Cost
average_cost=total_cost/len(medical_costs)
print("Average Insurance Cost: {}".format(str(average_cost)))

#second Dictionary
names=["Marina","Vinay","Connie","Isaac","Valentina"]
ages=[27,24,43,35,52]
zipped_ages=zip(names,ages)
names_to_ages={key:value for key,value in zipped_ages}
print(names_to_ages)

#Marina's Age
marina_age=names_to_ages.get("Marina")
print("Marina's age is {}".format(str(marina_age)))

#Using a Dictionary to create a medical database
medical_records={}
medical_records["Marina"]={"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records["Vinay"]={"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records["Connie"]={"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Isaac"]={"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"]={"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}
print(medical_records)

print("Connie's insurance cost is "+str(medical_records.get("Connie").get("Insurance_cost"))+" dollars.")
medical_records.pop("Vinay")
print(medical_records)

#displaying all records
for name,values in medical_records.items():
  print("{} is a {} year old {} {} with a BMI of{} and insurance cost of {}".format(name,str(values.get("Age")),values.get("Sex"),values.get("Smoker"),str(values.get("BMI")),str(values.get("Insurance_cost"))))

#Extra
def update_medical_records(name,age,sex,bmi,children,smoker,insurance_cost):
  medical_records[name]={"Age":age,"Sex":sex,"BMI":bmi,"Children":children,"Smoker":smoker,"Insurance_cost":insurance_cost}
  return medical_records
update_medical_records("Mykell",26,"Male",25.3,0,"Non-Smoker",25638.5)

print(medical_records)


  

