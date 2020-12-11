from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import string, random


# Create your views here.
@csrf_exempt
def home_page(request):
    # print(request.GET.get('passlen'))
    if request.method == 'POST':
        optionValue = request.POST.get('passlen')
        if 7 > int(optionValue) or int(optionValue) > 22:
            optionValue = 22
        is_uppercase = request.POST.get('uppercase')
        is_lowercase = request.POST.get('lowercase')
        is_number = request.POST.get('number')
        is_specialchar = request.POST.get('specialchar')
        contains = [x for x in [is_uppercase, is_lowercase, is_number, is_specialchar] if x != None]

        
        a = [x for x in string.ascii_uppercase]
        b = [x for x in string.ascii_lowercase]
        c = [x for x in string.digits]
        d = [x for x in string.punctuation]

        allStrings = list()

        for x in contains:
            if x == 'a':
                allStrings.append(a)           
            elif x == 'b':
                allStrings.append(b)           
            elif x == 'c':
                allStrings.append(c)              
            else:
                allStrings.append(d)
            
        if allStrings == list():
            allStrings.append(a+b+c+d)
            optionValue = random.randint(8, 22)
        elif len(contains) == 1 and contains[0] == 'c':
            allStrings.append(c+c+c)
        
        def MakeOneList(x):
            FinalList = list()
            for i in x:
                if type(i) == list:
                    for j in i:
                        FinalList.append(j)
                else:
                    return x
            return FinalList

        def passgen(x, data, psd=set()):
            FinalList = MakeOneList(data)
            if len(contains) == 1 and contains[0] == 'c':
                psd = list()
            while True:
                random.shuffle(FinalList)
                num = random.choice(FinalList)
                if type(psd) != list:
                    psd.add(num)
                else:
                    psd.append(num)
                if len(psd) == x:
                    break
            return "".join(psd)
        password = passgen(int(optionValue), allStrings)
        
    else:
        return render(request, 'index.html', {'pass': "-Not Generated Yet-"})
    return render(request, 'index.html', {'pass': password})