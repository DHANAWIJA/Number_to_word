#NUMBER TO WORD CONVERTOR

words_upto_19=["","One","Two","Three","four","Five","Six","Seven","Eight","Nine",
              "Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
words_for_tens=['','',"Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","ninty"]
words_for_hundreds=['',"One hundred","Two hundred","Three hundred","Four hundred","Five hundred","Six hundred",
                    "Seven hundred","Eight hundred","Nine hundred"]
words_for_thousands=['','One thousand','Two thousand','Three thousand','Four thousand','Five thousand','Six thousand',
                    'Seven thousand','Eight thousand','Nine thousand',]
n=int(input("enter a number from 0 to 10000:"))

num=''
if n==0:
    num='Zero'
elif n==100:
    num='hundred'
elif n==1000:
    num='one thousand'
elif n==10000:
    num='Ten thousand'
elif n<=19:
    num=words_upto_19[n]
elif n<=99:
    num=words_for_tens[n//10]+' '+words_upto_19[n%10]
elif n<=999:
    num=words_for_hundreds[n//100]+' '+words_for_tens[(n%100)//10]+' '+words_upto_19[n%10]
elif n<=9999:
    num=words_for_thousands[n//1000]+' '+words_for_hundreds[(n%1000)//100]\
        +' and '+words_for_tens[(n%100)//10]+' '+words_upto_19[n%10]
else:
    num='please enter a number from 0 to 100000'
print(num)










