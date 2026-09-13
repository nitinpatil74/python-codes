#Calculate Simple Interest in Python
#Simple Interest is calculated using the following formula:

#SI = (P × R × T) / 100

#Where:

#P = Principal amount of money.
#R = Rate of Interest (e.g. 7%).
#T = Time period.
#The principal is the sum of money that remains constant every year in the case of simple interest.

#Here is a Python program to figure out the simple interest:

def simple_interest(p, t, r):
    """
    p = principal amount
    t = time interval
    r = rate of interest
    
    si = simple interest given p, t, r
    """
      
    si = (p * t * r)/100
      
    print("The Simple Interest is", si)
    return si
    
simple_interest(1200, 10, 7)


# out put 
# The Simple Interest is 840.0