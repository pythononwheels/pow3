
from sqlalchemy import Column, Integer, String
from pow3.db import engine, get_session

class BaseModel():
    
    def get_session(self):
        return self.session
        
    def schema(self):
        print(50*"-")
        print("Schema for: " + str(self.__class__))
        print("{0:30s} {1:20s}".format("Column", "Type"))
        print(50*"-")
        for col in self.__table__._columns:
            print("{0:30s} {1:20s}".format(str(col), str(col.type)))
            #print(dir(col))

    def values(self):
        print(50*"-")
        print("Schema for: " + str(self.__class__))
        print("{0:30s} {1:20s}".format("Column", "Type"))
        print(50*"-")
        for col in self.__table__._columns:
            pass
            
            
    def create_table(self):
        """
            created the physical table in the DB
        """
        self.__table__.create(bind=engine)

    def drop_table(self):
        """
            created the physical table in the DB
        """
        self.__table__.drop(bind=engine)


    def find(self, filter_condition = [('name', 'eq', 'klaas')]):
        dynamic_filtered_query_class = DynamicFilter(query=None, model_class=self,
                                  filter_condition=filter_condition)
        dynamic_filtered_query = dynamic_filtered_query_class.return_query()
        return dynamic_filtered_query

class DynamicFilter():
    def __init__(self, query=None, model_class=None, filter_condition=None):
        #super().__init__(*args, **kwargs)
        self.query = query
        self.model_class = model_class.__class__
        self.filter_condition = filter_condition
        self.session = get_session()


    def get_query(self):
        '''
        Returns query with all the objects
        :return:
        '''
        if not self.query:
            self.query = self.session.query(self.model_class)
        return self.query


    def filter_query(self, query, filter_condition):
        '''
        Return filtered queryset based on condition.
        :param query: takes query
        :param filter_condition: Its a list, ie: [(key,operator,value)]
        operator list:
            eq for ==
            lt for <
            ge for >=
            in for in_
            like for like
            value could be list or a string
        :return: queryset

        '''

        if query is None:
            query = self.get_query()
        #model_class = self.get_model_class()  # returns the query's Model
        model_class = self.model_class
        for raw in filter_condition:
            try:
                key, op, value = raw
            except ValueError:
                raise Exception('Invalid filter: %s' % raw)
            column = getattr(model_class, key, None)
            if not column:
                raise Exception('Invalid filter column: %s' % key)
            if op == 'in':
                if isinstance(value, list):
                    filt = column.in_(value)
                else:
                    filt = column.in_(value.split(','))
            else:
                try:
                    attr = list(filter(
                        lambda e: hasattr(column, e % op),
                        ['%s', '%s_', '__%s__']
                    ))[0] % op
                except IndexError:
                    raise Exception('Invalid filter operator: %s' % op)
                if value == 'null':
                    value = None
                filt = getattr(column, attr)(value)
            query = query.filter(filt)
        return query


    def return_query(self):
        return self.filter_query(self.get_query(), self.filter_condition)