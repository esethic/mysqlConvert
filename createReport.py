import connect
import csv

connection = connect.dbConnection

#accepts sql query as string variable and returns query result as a list of dicts
def getQuery(sql):
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
                            
#accepts result of getQuery(sql) and writes result to csv with a blank first column to be compatible with sql server bulk insert
def prepareCSV(queryResult, reportName, saveLocation):
    query = list(queryResult)
    processed = []
    for x in range(len(query)):
        currentRow = query[x]
        addBlank = list(currentRow.values())
        addBlank.insert(0,'')
        processed.append(addBlank)
        
    with open(f'{saveLocation}\{reportName}.csv','w') as f:
        write=csv.writer(f, delimiter='|')
        write.writerows(processed)
