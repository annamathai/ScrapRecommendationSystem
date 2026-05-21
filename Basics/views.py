from django.shortcuts import render
def Sum(request):
    if request.method=="POST":
        num1=int(request.POST.get("txt_num1"))
        num2=int(request.POST.get("txt_num2"))
        result=num1+num2
        return render(request,'Basics/Sum.html',{'Sum':result})
    else:
        return render(request,'Basics/Sum.html')
def Calculator(request):  
    if request.method=="POST":
        num1=int(request.POST.get("txt_num1"))
        num2=int(request.POST.get("txt_num2"))
        btn=request.POST.get("calc")
        if btn=="Add":
           result=num1+num2
        elif btn=="Subtract":
            result=num1-num2
        elif btn=="Division":
            result=num1/num2
        elif btn=="Multiplication" :
            result=num1*num2
        return render(request,'Basics/Calculator.html',{'result':result})
    else:
        return render(request,'Basics/Calculator.html')
def LargestSmallest(request):
    if request.method=="POST":
        num1=int(request.POST.get("txt_num1"))
        num2=int(request.POST.get("txt_num2"))
        num3=int(request.POST.get("txt_num3"))
        smallest=min(num1,num2,num3)
        largest=max(num1,num2,num3)
        return  render(request,'Basics/LargestSmallest.html',{'small':smallest,'large':largest})
    else:
        return render(request,'Basics/LargestSmallest.html')
    return render(request,'Basics/LargestSmallest.html')
