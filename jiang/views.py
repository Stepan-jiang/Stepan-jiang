#coding:utf-8
import os
import requests,json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.

def hello_test(request):
    return HttpResponse("hello")
def index(request):
    return render(request, 'index.html')
def post(request):
    """post请求页面方法"""
    if request.method == 'POST':
        url = request.POST.get("url")#获取前台输入url
        header=request.POST.get('header')#获取前台输入header
        body=request.POST.get('body')#获取前台输入body
        type_data = request.POST['type_data']#获取前台选择的参数类型
        print(type_data)
        try:
            data = eval(body)
        except:
            data = body
        #print(url)
        print(body)
        if header == "":
            if type_data == "json":
                if body =="":
                    try:
                        r = requests.post(url=url,json=data,verify=False)
                        print(r.json())
                        return render(request, 'post_type2.html', {"url": url, "header": "未输入", "body": "未输入",
                                                                   "respnse":json.dumps(r.json(),ensure_ascii=False)})
                    except:
                        return render(request, 'post_type2.html',
                                      {"url": url, "header": "未输入", "body": "未输入", "respnse": "请求url、header、body存在参数错误"})
                elif body!="":
                    try:
                        r = requests.post(url=url, json=data, verify=False)
                        print(r.json())
                        return render(request, 'post_type2.html', {"url": url, "header": "未输入", "body": body,
                                                                   "respnse":json.dumps(r.json(),ensure_ascii=False)})
                    except:
                        return render(request, 'post_type2.html',
                                      {"url": url, "header": "未输入", "body": body, "respnse": "请求url、header、body存在参数错误"})
            elif type_data == "params":
                if body == "":
                    try:
                        r = requests.post(url=url, params=data, verify=False)
                        print(r.json())
                        return render(request, 'post_type2.html', {"url": url, "header": "未输入", "body": "未输入",
                                                                   "respnse": json.dumps(r.json(), ensure_ascii=False)})
                    except:
                        return render(request, 'post_type2.html',
                                      {"url": url, "header": "未输入", "body": "未输入", "respnse": "请求url、header、body存在参数错误"})
                elif body != "":
                    try:
                        r = requests.post(url=url, params=data, verify=False)
                        print(r.json())
                        return render(request, 'post_type2.html', {"url": url, "header": "未输入", "body": body,
                                                                   "respnse": json.dumps(r.json(), ensure_ascii=False)})
                    except:
                        return render(request, 'post_type2.html',
                                      {"url": url, "header": "未输入", "body": body, "respnse": "请求url、header、body存在参数错误"})
            elif type_data == "data":
                if body == "":
                    try:
                        r = requests.post(url=url, data=data, verify=False)
                        print(r.json())
                        return render(request, 'post_type2.html', {"url": url, "header": "未输入", "body": "未输入",
                                                                   "respnse": json.dumps(r.json(), ensure_ascii=False)})
                    except:
                        return render(request, 'post_type2.html',
                                      {"url": url, "header": "未输入", "body": "未输入", "respnse": "请求url、header、body存在参数错误"})
                elif body != "":
                    try:
                        r = requests.post(url=url, data=data, verify=False)
                        print(r.json())
                        return render(request, 'post_type2.html', {"url": url, "header": "未输入", "body": body,
                                                                   "respnse": json.dumps(r.json(), ensure_ascii=False)})
                    except:
                        return render(request, 'post_type2.html',
                                      {"url": url, "header": "未输入", "body": body, "respnse": "请求url、header、body存在参数错误"})
        elif header != "":
            if type_data == "json":
                if body =="":
                    try:
                        r = requests.post(url=url, headers=header, json=data, verify=False)
                        print(r.json())
                        return render(request, 'post_type2.html', {"url":url, "header":header, "body":"未输入",
                                                                   "respnse":json.dumps(r.json(),ensure_ascii=False)})
                    except:
                        return render(request, 'post_type2.html',
                                      {"url":url, "header":header, "body":"未输入", "respnse": "请求url、header、body存在参数错误"})
                elif body !="":
                    try:
                        r = requests.post(url=url, headers=header, json=data, verify=False)
                        print(r.json())
                        return render(request, 'post_type2.html', {"url": url, "header": header, "body": body,
                                                                   "respnse": json.dumps(r.json(), ensure_ascii=False)})
                    except:
                        return render(request, 'post_type2.html',
                                      {"url": url, "header": header, "body": body, "respnse": "请求url、header、body存在参数错误"})
            elif type_data == "params":
                if body =="":
                    try:
                        r = requests.post(url=url, headers=header, params=data, verify=False)
                        print(r.json())
                        return render(request, 'post_type2.html', {"url":url, "header":header, "body":"未输入",
                                                                   "respnse":json.dumps(r.json(),ensure_ascii=False)})
                    except:
                        return render(request, 'post_type2.html',
                                      {"url":url, "header":header, "body":"未输入", "respnse": "请求url、header、body存在参数错误"})
                elif body !="":
                    try:
                        r = requests.post(url=url, headers=header, params=data, verify=False)
                        print(r.json())
                        return render(request, 'post_type2.html', {"url": url, "header": header, "body": body,
                                                                   "respnse": json.dumps(r.json(), ensure_ascii=False)})
                    except:
                        return render(request, 'post_type2.html',
                                      {"url": url, "header": header, "body": body, "respnse": "请求url、header、body存在参数错误"})
            elif type_data == "data":
                if body == "":
                    try:
                        r = requests.post(url=url, headers=header, data=data, verify=False)
                        print(r.json())
                        return render(request, 'post_type2.html', {"url": url, "header": header, "body": "未输入",
                                                                   "respnse": json.dumps(r.json(), ensure_ascii=False)})
                    except:
                        return render(request, 'post_type2.html',
                                      {"url": url, "header": header, "body": "未输入", "respnse": "请求url、header、body存在参数错误"})
                elif body != "":
                    try:
                        r = requests.post(url=url, headers=header, data=data, verify=False)
                        print(r.json())
                        return render(request, 'post_type2.html', {"url": url, "header": header, "body": body,
                                                                   "respnse": json.dumps(r.json(), ensure_ascii=False)})
                    except:
                        return render(request, 'post_type2.html',
                                      {"url": url, "header": header, "body": body, "respnse": "请求url、header、body存在参数错误"})
    else:
        return render(request, 'post_type.html')
def get(request):
    """get请求页面方法"""
    if request.method == 'POST':
        url = request.POST.get("get_url")  # 获取前台输入url
        header = request.POST.get('get_header')  # 获取前台输入header
        body = request.POST.get('params')  # 获取前台输入body
        try:
            data = eval(body)
        except:
            data = body
        print(url)
        print(body)
        print(header)
        if header == "":
            if body =="":
                try:
                    r = requests.get(url=url, verify=False)
                    print(r.json())
                    return render(request, 'get_type2.html', {"url": url, "header": "未输入", "body": "未输入", "respnse": json.dumps(r.json(),ensure_ascii=False)})
                except:
                    return render(request, 'get_type2.html', {"url": url, "header": "未输入", "body": "未输入", "respnse": "URL错误"})
            elif body !="":
                try:
                    r = requests.get(url=url, params=data, verify=False)
                    print(r.json())
                    return render(request, 'get_type2.html', {"url": url, "header": "未输入", "body": body, "respnse": json.dumps(r.json(),ensure_ascii=False)})
                except:
                    return render(request, 'get_type2.html', {"url": url, "header": "未输入", "body": body, "respnse": "URL或参数错误"})

        elif header != "":
            if body =="":
                try:
                    r = requests.get(url=url, headers=header, verify=False)
                    print(r.json())
                    return render(request, 'get_type2.html', {"url": url, "header": header, "body": "未输入", "respnse": json.dumps(r.json(),ensure_ascii=False)})
                except:
                    return render(request, 'get_type2.html', {"url": url, "header": header, "body": "未输入", "respnse": "请求url、请求头、存在错误"})
            elif body !="":
                try:
                    r = requests.get(url=url, headers=header, params=data, verify=False)
                    print(r.json())
                    return render(request, 'get_type2.html', {"url": url, "header": header, "body": body, "respnse": json.dumps(r.json(),ensure_ascii=False)})
                except:
                    return render(request, 'get_type2.html', {"url": url, "header": header, "body": body, "respnse": "请求url、请求头、参数存在错误"})
    else:
        return render(request, 'get_type.html')