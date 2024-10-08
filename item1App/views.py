from django.shortcuts import render

# Create your views here.
def index(request):
    data = {'titulo_index': 'Index'}
    return render(request, 'index.html', data)

def dic_num(request):
    data = {
        'dic_titulo': 'Diccionario Númerico',
    }
    dic = {}
    num = 1
    for i in range(1, 13):
        if i % 2 != 0:
            if num == 1:
                dic[i] = num
                num = -1
            elif num == -1:
                dic[i] = num
                num = 1
        else:
            dic[i] = 0
    info = {'data': data, 'dic': dic}
    return render(request, 'algoritmos.html', info)

def dic_log(request):
    data = {'dic_titulo': 'Diccionario Lógico'}
    dic = {}
    var1 = True
    var2 = None
    for i in range(1, 13):
        if var1 == True:
            if var2 == None:
                dic[f'{var1} {i}'] = var2
                var1 = False
                var2 = True
            elif var2 == True:
                dic[f'{var1} {i}'] = var2
                var1 = False
                var2 = False
            elif var2 == False:
                dic[f'{var1} {i}'] = var2
                var1 = False
                var2 = None
        elif var1 == False:
            if var2 == None:
                dic[f'{var1} {i}'] = var2
                var1 = True
                var2 = True
            elif var2 == True:
                dic[f'{var1} {i}'] = var2
                var1 = True
                var2 = False
            elif var2 == False:
                dic[f'{var1} {i}'] = var2
                var1 = True
                var2 = None
    info = {'data': data, 'dic': dic}
    return render(request, 'algoritmos.html', info)

def dic_hib(request):
    data = {'dic_titulo': 'Diccionario Híbrido'}
    dic = {}
    caracter = 40
    var = 1
    for i in range(1, 13):
        dic[chr(caracter)] = var
        caracter += 5
        var += i
    info = {'dic': dic, 'data': data}
    return render(request, 'algoritmos.html', info)