'''
Use for Database SQL operations.
'''

__author__ = 'Birender'

import pyodbc

def connect_db(server_name, database, username, password):
    """
    Creates database connection.

    :param sever_name: str type. Database server ip or server hostname.
    :param database: str type. Database name.
    :param username: str type. Database username.
    :param password: str type. Database password
    :return: cursor. db connection & cursor.
    """

    server = server_name
    database = database
    username = username
    password = password

    #connectin to the database
    try:
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server
                              + ';DATABASE='+ database
                              + ';UID='+ username
                              + ';PWD='+ password)
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        return e
    finally:
        pass

def run_select_query(server_name, database, username, password, query):
    """
    Executes SQL SELECT Query and returns query result.

    :param server_name:
    :param database:
    :param username:
    :param password:
    :param query:
    :return: return code, list containing result. result code 1 if success and 0 if error ocurred.
    """

    #Create db conncetion
    conn, cursor = connect_db(server_name, database, username, password)
    try:
        #executing query
        query_result = cursor.execute(query)

        #Getting result into list variable.
        result = []
        for row in query_result:
            result.append(row)
        flag = 1
    except Exception as e:
        flag = 0
        errorMessage = e
    finally:
        cursor.close()
        conn.close()

        #Checking for any exception occured
        if flag == 0:
            return flag, errorMessage
        else:
            return 1, result



def run_insert_query(server_name, database, username, password, queries):
    """
    SQL Insert queries and return success code.

    :param server_name:
    :param database:
    :param username:
    :param password:
    :param queries:
    :return: return code, errorMessage if exception ocurred. result code 1 if success and 0 if error ocurred.
    """

    #create DB connection
    conn, cursor = connect_db(server_name, database, username, password)

    #Executing query
    try:
        for query in queries:
            cursor.execute(query)
        conn.commit()
        flag = 1
    except Exception as e:
        flag = 0
        errorMessage = e
    finally:
        cursor.close()
        conn.close()

        if flag == 0:
            return flag, errorMessage
        else:
            return 1

def run_update_query(server_name, database, username, password, query):
    """
    Execute SQL UPDATE query

    :param server_name:
    :param database:
    :param username:
    :param password:
    :param query:
    :return:  return code, errorMessage if exception ocurred. result code 1 if success and 0 if error ocurred.
    """
    # create DB connection
    conn, cursor = connect_db(server_name, database, username, password)

    # Executing query
    try:
        query_result = cursor.execute(query)
        conn.commit()
        flag = 1
    except Exception as e:
        flag = 0
        errorMessage = e
    finally:
        cursor.close()
        conn.close()
        if flag == 0:
            return flag, errorMessage
        else:
            return 1

def run_delete_query(server_name, database, username, password, query):
    """
    Execute SQL DELETE query and return success code.
    :param server_name:
    :param database:
    :param username:
    :param password:
    :param query:
    :return:
    """
    # create DB connection
    conn, cursor = connect_db(server_name, database, username, password)

    # Executing query
    try:
        cursor.execute(query)
        conn.commit()
        flag = 1
    except Exception as e:
        flag = 0
        errorMessage = e
    finally:
        cursor.close()
        conn.close()
        if flag == 0 :
            return flag, errorMessage
        else:
            return 1
