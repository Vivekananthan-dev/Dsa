def SecondLargest(l1):

    first = second = float('-inf')
    for num in l1:
        if num>first:
            second,first = first,num
        elif first > num >second:
            second = num
    return second if second !=float('-inf') else None

print(SecondLargest([10, 20, 4, 45, 99]))