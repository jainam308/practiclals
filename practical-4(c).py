#BMI calculater

w=float(input("Enter your weight in kgs"))
h=float(input("Enter your hright in cm:"))

BMI=w/((h/100)*(h/100))

if(19>BMI and  BMI<25):
    print("The person is healthy")
elif(BMI<19):
    print("The person is underweight")
elif(BMI>25):
    print("The person is overweight")
    