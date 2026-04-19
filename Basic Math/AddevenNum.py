# Add only even numbers in a list
def addEvenNumber(val):
    return sum(n for n in val if n%2==0)

print(addEvenNumber([1,2,3,4,5,6,7,8,9,10]))