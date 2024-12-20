from django.shortcuts import render

# Create your views here.

def main(request):
    context = {
        'title': 'Home_work_2',
        'name': "Домашняя задания 2",
        'description': "Выполнено домашняя задание",
        'img': 'https://thumbs.dreamstime.com/z/%D0%B7%D0%BD%D0%B0%D1%87%D0%BE%D0%BA-%D0%B4%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D0%B5%D0%B3%D0%BE-%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BF%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B9-%D1%80%D0%B5%D0%B4%D0%B0%D0%BA%D1%82%D0%B8%D1%80%D1%83%D0%B5%D0%BC%D1%8B%D0%B9-%D0%B2%D0%B5%D0%BA%D1%82%D0%BE%D1%80%D0%BD%D1%8B%D0%B9-%D0%B4%D0%B8%D0%B7%D0%B0%D0%B9%D0%BD-223879537.jpg'
    }
    return render(request, 'index.html', context=context)

