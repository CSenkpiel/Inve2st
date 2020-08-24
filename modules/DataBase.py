#import psycopg2
class DataBase():
    """Base class for Postgresql Database"""
    def __init__(self, dbname, host, user, password):
        """
        Database constructor method

        Parameters
        ----------
        dbname: str
            Database Name
        host: str
            Host
        user: str
            Username
        password: str
            Password
        """

        # Connect to an existing database
        self._conn = psycopg2.connect(dbname=dbname, host=host, user=user, password=password, port=5432)
        # Open a cursor to perform database operations
        self._cur = self._conn.cursor()
        self.cur = self._conn.cursor()

    def execute_query(self, query):
        """
        Method for executing Postgresql query.
        
        Parameters
        ----------
        query: str
            SQL Query
        Returns
        -------
        r: str
            SQL Query Result

        """

        # Execute a command: this creates a new table
        self._cur.execute(query)

        # Query the database and obtain data as Python objects
        r = self._cur.fetchall()

        # Make the changes to the database persistent
        self._conn.commit()

        # Close communication with the database
        # self._conn.close()
        return r

