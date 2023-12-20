'''
6. WAP, using function, to convert temparature from C to K and K to C
'''
def c_to_k(c):
    return c+273.15
def k_to_c(k):
    return k-273.15
c=float(input("Enter temparature in celcius:-"))
k=c_to_k(c)
print("Temparature in kelvin:-",k)
k=float(input("Enter temparature in kelvin:-"))
c=k_to_c(k)
print("Temparature in celcius:-",c)