
from sql_db_operation import *

sever_name = "serverhostname" # "local" if local is used then it take quite a long time to process connection to db

database = "nameofDB"
username = 'username'
password = 'userpassword'

#connect_db(sever_name, database, username, password)

query1 = 'select * from tblGender'
query2 = 'select * from tblPerson'

query = [query1, query2]

for q in query:
    print(run_select_query(sever_name, database, username, password, q))

print('success')

