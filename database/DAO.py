from database.DB_connect import DBConnect
from model.country import Country


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getConfiniAnno(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select state1no, state2no, conttype from contiguity c 
                where year <= %s"""
        cursor.execute(query, (anno,))

        for row in cursor:
            result.append((row["state1no"], row["state2no"], row["conttype"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getStati():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * from country"""
        cursor.execute(query)

        for row in cursor:
            result.append(Country(**row))
        cursor.close()
        conn.close()
        return result
