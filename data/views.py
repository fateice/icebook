# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context
from django.template.context import RequestContext
from data.models import *
import datetime
from django.template.context import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import get_template
from models import*
import MySQLdb
from django.db import connection,transaction  
from django.shortcuts import render_to_response

def index(request):
    ISBN=0
    ISBN=1
    ISBN=0
    return render_to_response('index.html')

def add(request):
    if 'ISBN' in request.GET and request.GET['ISBN'] and 'Title' in request.GET and request.GET['Title']: 
        already=0
        ISBN = request.GET['ISBN']
        Title = request.GET['Title']
        AuthorID = request.GET['AuthorID']
        Publisher = request.GET['Publisher']
        PublishDate = request.GET['PublishDate']
        Price = request.GET['Price']
        cursor=connection.cursor()
        sql = 'SELECT * from data1_book where ISBN= \''+ISBN+'\''
        if not(cursor.execute(sql)):
            sql = 'SELECT * from data1_author where AuthorID= \''+AuthorID+'\''
            if(cursor.execute(sql)):
                sql = 'insert into data1_book (ISBN,Title,AuthorID,Publisher,PublishDate,Price) value (\''+ISBN+'\',\''+Title+'\',\''+AuthorID+'\',\''+Publisher+'\',\''+PublishDate+'\',\''+Price+'\')'
                cursor.execute(sql)  
                transaction.commit_unless_managed()  
                cursor.close() 
                #return render_to_response('index.html')
                return render_to_response("success.html")
            else:
                sql = 'insert into data1_book (ISBN,Title,AuthorID,Publisher,PublishDate,Price) value (\''+ISBN+'\',\''+Title+'\',\''+AuthorID+'\',\''+Publisher+'\',\''+PublishDate+'\',\''+Price+'\')'
                cursor.execute(sql)  
                transaction.commit_unless_managed()  
                cursor.close() 
                idd = AuthorID
                iddd = 1
                return render_to_response('add_author.html',{'idd':idd,'iddd':iddd})
        else:
            already=1
            transaction.commit_unless_managed()  
            cursor.close() 
            return render_to_response('add.html',{'already':already})
    else:
        return render_to_response('add.html')
    #return render_to_response('add.html')



def add_author(request):
    iddd=0
    if 'AuthorID' in request.GET and request.GET['AuthorID'] and 'Name' in request.GET and request.GET['Name']: 
        AuthorID = request.GET['AuthorID']
        Name = request.GET['Name']
        Age = request.GET['Age']
        Country = request.GET['Country']
        cursor=connection.cursor()

        sql = 'SELECT * from data1_author where AuthorID= \''+AuthorID+'\''
        
        if not(cursor.execute(sql)):
            sql = 'insert into data1_author (AuthorID,Name,Age,Country) value (\''+AuthorID+'\',\''+Name+'\',\''+Age+'\',\''+Country+'\')'
            cursor.execute(sql)  
            transaction.commit_unless_managed()  
            cursor.close() 
            #return render_to_response('index.html')
            return render_to_response("success.html")
        else:
            transaction.commit_unless_managed()  
            cursor.close()
            return render_to_response('add_author.html') 
    else:
        return render_to_response('add_author.html')

def searchbook(request):
    if 'TitleIN' in request.GET:
        ex=0
        TitleIN = request.GET['TitleIN']
        cursor=connection.cursor()
        sql = 'SELECT * from data1_book where Title= \''+TitleIN+'\''
        cursor.execute(sql)
        all = cursor.fetchall()
        if (cursor.execute(sql)):
            ex=0
            str = TitleIN
            str2 = all
            transaction.commit_unless_managed()  
            cursor.close()
        else:
            ex=1
            str = ''
            str2 = ''
            transaction.commit_unless_managed()  
            cursor.close()
        #return HttpResponse(html)
    #return render_to_response('searchbook.html',{'str':str})
    return render_to_response('searchbook.html',{'str':str,'str2':str2,'ex':ex,'all':all})

def searchauthor(request):
    if 'authorIN' in request.GET:
        cursor=connection.cursor()
        authorIN = request.GET['authorIN']
        sql = 'SELECT * from data1_author where Name= \''+authorIN+'\''
        cursor.execute(sql)
        all = cursor.fetchall()
        autid = str(all[0][0])
        sql = 'SELECT * from data1_book where AuthorID = \''+autid+'\''
        cursor.execute(sql)
        autbook = cursor.fetchall()
        aut = authorIN
        transaction.commit_unless_managed()  
        cursor.close() 
    return render_to_response('searchauthor.html',{'aut':aut,'all':all,'autbook':autbook,'autid':autid})

def allbook(request):
    cursor=connection.cursor()
    sql = 'SELECT * from data1_book '
    cursor.execute(sql)
    all = cursor.fetchall()
    allbook = all
    transaction.commit_unless_managed()  
    cursor.close() 
    return render_to_response('allbook.html',{'allbook':allbook})

def update(request):
    up = request.GET['ISBN']
    cursor=connection.cursor()
    sql = 'SELECT * from data1_book where ISBN= \''+up+'\''
    cursor.execute(sql)
    all = cursor.fetchall()
    transaction.commit_unless_managed()  
    cursor.close()
    if 'ISBN' in request.GET and request.GET['ISBN'] and 'Title' in request.GET and request.GET['Title']: 
        Title = request.GET['Title']
        AuthorID = request.GET['AuthorID']
        Publisher = request.GET['Publisher']
        PublishDate = request.GET['PublishDate']
        Price = request.GET['Price']
        cursor=connection.cursor()
        sql = 'UPDATE data1_book SET Title = \''+Title+'\', AuthorID =\''+AuthorID+'\',Publisher=\''+Publisher+'\',PublishDate=\''+PublishDate+'\',Price=\''+Price+'\' where ISBN = \''+up+'\'  '
        cursor.execute(sql)  
        transaction.commit_unless_managed()  
        cursor.close()
        up = request.GET['ISBN']
    cursor=connection.cursor()
    sql = 'SELECT * from data1_book where ISBN= \''+up+'\''
    cursor.execute(sql)
    all = cursor.fetchall()
    transaction.commit_unless_managed()  
    cursor.close()
    return render_to_response('update.html',{'up':up,'all':all})

def delete(request):
    de = request.GET['ISBN']
    cursor=connection.cursor()
    sql = 'DELETE from data1_book where ISBN= \''+de+'\''
    cursor.execute(sql)
    all = cursor.fetchall()
    transaction.commit_unless_managed()  
    cursor.close()
    return render_to_response('delete.html')

def detail(request):
    det = request.GET['AuthorID']
    cursor=connection.cursor()
    sql = 'SELECT * from data1_author where AuthorID= \''+det+'\''
    cursor.execute(sql)
    all = cursor.fetchall()
    transaction.commit_unless_managed()  
    cursor.close()
    return render_to_response('detail.html',{'all':all})

def add_success(request):
    return render_to_response('success.html')
