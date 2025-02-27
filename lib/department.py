from __init__ import CURSOR, CONN  # Import CURSOR and CONN from __init__.py

class Department:
    @classmethod
    def create_table(cls):
        """Creates the departments table if it doesn't exist"""
        sql = """
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drops the departments table if it exists"""
        sql = "DROP TABLE IF EXISTS departments"
        CURSOR.execute(sql)
        CONN.commit()
    
    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def save(self):
        """Saves a department instance to the database and assigns an ID"""
        sql = "INSERT INTO departments (name, location) VALUES (?, ?)"
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()
        self.id = CURSOR.lastrowid  # Assign the auto-generated ID

    @classmethod
    def create(cls, name, location):
        """Creates a new department record and returns a Department instance"""
        department = cls(name, location)
        department.save()
        return department

    def update(self):
        """Updates the department's row in the database"""
        if self.id is None:
            raise ValueError("Cannot update a department that has not been saved to the database.")
        
        sql = "UPDATE departments SET name = ?, location = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        """Deletes the department's row from the database"""
        if self.id is None:
            raise ValueError("Cannot delete a department that has not been saved to the database.")
        
        sql = "DELETE FROM departments WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
