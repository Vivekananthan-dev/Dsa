def convert(num):
    if num == 0:
        return "zero"
    
    ones = ["","one","two","three","four","five","six","seven","eight","nine"]
    
    teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens = ["","","wenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    thousands = ["","thousand","million","billion","trillion"]
    
    def convert_hundred(n):
        result = ""
        
        if n>=100:
            result +=ones[n//100]+ "hundred"
            n %= 100
            if n:
                result += " "
        if 10 <= n <=19:
            result += teens[n-10]
        else:
            if n >= 20:
                result += tens[n//10]
                if n%10:
                    result += " "+ones[n%10]
            else:
                result +=ones[n]
        return result
    result = ""
    i = 0
    
    while num >0:
        cut = num %1000
        
        if cut != 0:
            words = convert_hundred(cut)
            if thousands[i]:
                words += " "+thousands[i]
            result = words+ " "+result
        num //=1000
        i+=1
    return result.strip()
print(convert(1000000000001))
print(convert(1012))
print(convert(1234567))
            