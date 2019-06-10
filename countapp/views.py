from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def count(request):
    full_text = request.GET['fulltext']
    #총단어수세기
    word_list = full_text.split()
    #각단어별 수
    word_dic = {}
    for word in word_list:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    return render(request, 'index.html', {'full_text' : full_text, 'total':len(word_list), 'dic':word_dic.items()})