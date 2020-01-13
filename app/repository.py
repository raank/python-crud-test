
class Repository(object):
    def __init__(self, connection, table):
        self.connection = connection
        self.table = table
        
    def apply(self, sql):
        self.connection.cursor().execute(sql)
        self.connection.commit()
    
    def findAll(self):
        data = self.connection.cursor().execute('SELECT * FROM %s' % self.table)
        return data.fetchall()
    
    def find(self, id, otherTable=None):
        if otherTable is None:
            currentTable = self.table
        else:
            currentTable = otherTable
            
        item = self.connection.cursor().execute('SELECT * FROM %s WHERE id = %s' % (currentTable, id))

        return item.fetchone()
    
    def last(self):
        item = self.connection.cursor().execute('SELECT * FROM %s ORDER BY id DESC LIMIT 1' % self.table)
        return item.fetchone()
    
    def insert(self, data):
        make = self.make(data)
        columns = make.get('columns')
        insert = make.get('insert')
        sql = 'INSERT INTO %s (%s) VALUES (%s)' % (self.table, columns, insert)
        
        self.apply(sql)
        
        return self
    
    def update(self, id, data):
        make = self.make(data)
        sets = make.get('update')
        sql = 'UPDATE %s SET %s WHERE id = %s' % (self.table, make.get('update'), id)
        
        self.apply(sql)

        return self
    
    def delete(self, id):
        sql = 'DELETE FROM %s WHERE id = %s' % (self.table, id)
        
        self.apply(sql)
        
        return self
    
    def make(self, data):
        columns = []
        insert = []
        update = []
        
        for row in data:
            values = list(row.values())
            keys = list(row.keys())
            
            for key in row.keys():
                columns.append('`%s`' % key)
            for value in values:
                insert.append("'%s'" % value)
                if value:
                    update.append("`%s` = '%s'" % (keys[values.index(value)], value))
                
        return {
            'columns': ', '.join(columns),
            'insert': ', '.join(insert),
            'update': ', '.join(update),
        }