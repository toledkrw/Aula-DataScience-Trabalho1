from pandas import DataFrame
from sqlalchemy import create_engine, Connection, text

def checkSchema(dbConnection:Connection ,schema:str) -> bool:
    query = text(
        f"""
        SELECT 
            SCHEMA_NAME 
        FROM 
            INFORMATION_SCHEMA.SCHEMATA 
        WHERE 
            SCHEMA_NAME = '{schema}';"""
        )

    result = dbConnection.execute(query)
    
    row = result.fetchone()

    if row is not None and row[0] == schema:
        return True
    else:
        return False

def createDatabase(dbConnection:Connection, db_name:str) -> None:
    query = text(
        f"""
        CREATE SCHEMA 
            {db_name} 
        DEFAULT CHARACTER SET 
            utf8 
        COLLATE 
            utf8_general_ci;
        """
    )

    dbConnection.execute(query)
    
def genConnection(schema='') -> Connection:
    if schema == '':
        return create_engine(f'mysql+pymysql://root:batata@localhost:3306')
    else:
        return create_engine(f'mysql+pymysql://root:batata@localhost:3306/{schema}')
    
def switch_database(connection, new_schema):
    connection.execute(text(f"USE {new_schema};"))

    
def handleSaveTable(df:DataFrame, table:str) -> None:
    dbConnection = genConnection()
    
    with dbConnection.connect() as dbConnection:
        try:
            db_schema = "dbo"
            
            if(not checkSchema(dbConnection,db_schema)):
                createDatabase(dbConnection,db_schema)

            switch_database(dbConnection, db_schema)
            
            df.to_sql(table, dbConnection, if_exists='append', schema=db_schema, method='multi')
            dbConnection.commit()
        except Exception as e:
            raise(e)
        finally:
            dbConnection.close()
