# Automatic Blind SQL Injection
Automate Blind SQL Injection with Python. 

This tool programmed in Python exploits a Blind SQL Injection via the response time with the SQL command called sleep, it also checks the correct character with the command called substr.

**Modules:**

**1. Actual DataBase**

![image](https://user-images.githubusercontent.com/79543461/185760280-b604ac00-e7cf-42aa-bfee-7a3d55fda582.png)

Actual DataBase Module is the first module. This module dumps the name of the database in which you are via the SQL command called database(), once we have this thanks to a double for loop we can test all the letters of the alphabet in each of the positions, and when the letter is correct the sleep() command puts the web to sleep and that is when the character is discovered

**2. All DataBases**

The second module it's called All Databases, with same way of working than module one, this module do the same but changing the payload. The new payload is like this:

SELECT schema_name FROM information_schema.schemata- --

And every time it finishes discovering all the characters in a database it adds a comma ", " and starts with the following, like this:

![image](https://user-images.githubusercontent.com/79543461/185761325-4bc5ebac-9df1-4e0d-b646-5fe2283b52ca.png)

**3. Tables**

The third module catch the results from all database module, and dump every tables from every databases founded in module 2. It is a module that takes a long time to finish but it works correctly.

![image](https://user-images.githubusercontent.com/79543461/185761459-4f0da3f8-bf4d-40b8-a77c-318174ced0dc.png)

**4. Columns Discover**

The fourth module is the one used to discover columns, in this case, since the execution of the previous module was already quite long, now it allows you to only discover the columns of the table that interests you, like this:

![image](https://user-images.githubusercontent.com/79543461/185762110-25554cf7-ebf1-4fb7-8755-4f992b239cdd.png)

**5. Columns Dumper**

The fifth module is used to dump the columns that interest you from the table and the database that you choose, you have to manually write the (database/table/column) and if you want to dump two columns it would be like this (database/table/column1:column2)

![image](https://user-images.githubusercontent.com/79543461/185762712-398edb55-a2cc-48d9-9e0b-f3253b661301.png)


**Basic Usage**

python3 sqli_blind.py -u target_url -d "'username':'anything','password':'sadasdsa'"

![image](https://user-images.githubusercontent.com/79543461/185762185-1cf1e554-f500-43c8-9de5-7662bde011a2.png)

And with -time flag you can add time of responses to avoid false positives. 

![image](https://user-images.githubusercontent.com/79543461/185762259-8f7e0977-6766-4854-bd87-d741dcffe61d.png)

Author: S12

Youtube Channel: https://www.youtube.com/channel/UCKILJTZISRLxQmiUgwg94Hw

Contact: s12deff@gmail.com
