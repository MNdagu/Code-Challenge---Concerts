from __init__ import CONN, CURSOR
from band import Band

class Venue:
    def __init__(self,id, title, city) -> None:
        self.id = id
        self.title = title
        self.city = city
        
    def __repr__(self):
        return f"<Venue(id={self.id}, title='{self.title}', city='{self.city}')>"

        
    @classmethod   
    def create(cls, title, city):
        sql = """
        INSERT INTO venues (title, city)
        VALUES (?, ?)
        """
        
        CURSOR.execute(sql, (title, city))
        CONN.commit()
        return cls(CURSOR.lastrowid, title, city)
        
    
    def concerts(self):
        #Returns a collection of all concerts for the venue
        sql = """
        SELECT * FROM concerts
        WHERE venue_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        return CURSOR.fetchall()

    def bands(self):
        #Returns a collection of all bands who performed at the venue
        sql = """
        SELECT DISTINCT bands.*
        FROM concerts 
        JOIN bands ON concerts.band_id = bands.id
        WHERE concerts.venue_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        return CURSOR.fetchall()
    
    def concert_on(self, date):
        #Find the first concert on this date at the venue
        query = """
        SELECT * FROM concerts
        WHERE venue_id = ? AND date = ?
        LIMIT 1
        """
        CURSOR.execute(query, (self.id, date))
        return CURSOR.fetchone()

    def most_frequent_band(self):
        #Return the band that has performed the most at the venue
        query = """
        SELECT bands.id, bands.name, bands.hometown, COUNT(concerts.id) AS concert_count
        FROM concerts 
        JOIN bands ON concerts.band_id = bands.id
        WHERE concerts.venue_id = ?
        GROUP BY bands.id
        ORDER BY concert_count DESC
        LIMIT 1
        """
        CURSOR.execute(query, (self.id,))
        result = CURSOR.fetchone()
        
        if result:  # Check if a result was found
            return Band(result[0], result[1], result[2])
        else:
            return None