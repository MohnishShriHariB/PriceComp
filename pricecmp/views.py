from django.shortcuts import render
from .models import product
import requests,random
from bs4 import BeautifulSoup



def home(request):
    items=product.objects.all()
    l=[]
    l2=[]
    b={}

    for i in items:
        l.append(i.type)
    l=list(set(l))
    l.sort()
    for j in l:
        a=product.objects.filter(type=j)
        b1=[]
        b[str(j)]=[]
        for k in a:
            print(k.brand)
            b1.append(k.brand)
        b1=list(set(b1))
        b1.sort()
        for e in b1:
            b[str(j)].append(str(e))
    products = random.sample(list(items),24)
    return render(request,"pricecmp/home.html",{"items":items,"type":l,"brand":b,"pro":products})


def display(request,pro_pk):
    pro=product.objects.get(id=pro_pk)
    aurl=str(pro.amazon_url)
    furl=str(pro.flipkart_url)
    headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
    page1=requests.get(aurl,headers=headers)
    page2=requests.post(furl)
    soup1=BeautifulSoup(page1.text,'html.parser')
    soup2=BeautifulSoup(page2.text,'html.parser')
    price1=soup1.select(".a-price-whole")
    price2=soup2.select("._30jeq3._16Jk6d")
    amazon_price=""
    amazon_error=""
    flipkart_price=""
    flipkart_error=""
    for i in price1:
        amazon_price=str(i.get_text())
        break
    for i in price2:
        flipkart_price=str(i.get_text())
    if amazon_price != "":
        pro.amazon_price=amazon_price
    else:
        amazon_error="UNAVAILABLE"
    if flipkart_price != "":
        pro.flipkart_price=flipkart_price[1:]
    else:
        flipkart_error="UNAVAILABLE"
    pro.save()
    return render(request,"pricecmp/display.html",{"pro":pro,"ae":amazon_error,"fe":flipkart_error})
