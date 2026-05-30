#Question : Write a python program using function to convert fahrenheit to Celsius. 

def f_to_c(f):
    return 5*(f-32)/9


f = int(input("Enter temperature in F : "))
c = f_to_c(f)
print(round(c,2),"°C")