from __init__ import CONN, CURSOR


class Band:
    def __init__(self,id, name, hometown) -> None:
        self.id = id
        self.name = name
        self.hometown = hometown
        
    def __repr__(self):
        return f"<Band(id={self.id}, name='{self.name}', hometown='{self.hometown}')>"

        
    @classmethod
    def create(cls, name, hometown):
        query = """
        INSERT INTO bands (name, hometown)
        VALUES (?, ?)
        """
        CURSOR.execute(query, (name, hometown))
        CONN.commit()
        return cls(CURSOR.lastrowid, name, hometown)

    def concerts(self):
        #Return a collection of all concerts the band has played
        query = """
        SELECT * FROM concerts
        WHERE band_id = ?
        """
        CURSOR.execute(query, (self.id,))
        return CURSOR.fetchall()

    def venues(self):
        #Return a collection of all venues the band has performed at
        query = """
        SELECT DISTINCT venues.*
        FROM concerts 
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.band_id = ?
        """
        CURSOR.execute(query, (self.id,))
        return CURSOR.fetchall()
    
    def play_in_venue(self, venue, date):
        # Insert a new concert for this band at the given venue on the given date
        query = """
        INSERT INTO concerts (band_id, venue_id, date)
        SELECT ?, venues.id, ?
        FROM venues
        WHERE venues.title = ?
        """
        CURSOR.execute(query, (self.id, date, venue))
        CONN.commit()

    def all_introductions(self):
        # Return an array of all introductions for this band
        query = """
        SELECT venues.city, bands.name, bands.hometown
        FROM concerts 
        JOIN venues ON concerts.venue_id = venues.id
        JOIN bands ON concerts.band_id = bands.id
        WHERE bands.id = ?
        """
        CURSOR.execute(query, (self.id,))
        results = CURSOR.fetchall()
        introductions = [f"Hello {city}!!!!! We are {name} and we're from {hometown}" for city, name, hometown in results]
        return introductions

    @classmethod
    def most_performances(cls):
        # Return the band that has played the most concerts
        query = """
        SELECT bands.id, bands.name, bands.hometown, COUNT(concerts.id) AS concert_count
        FROM bands 
        JOIN concerts ON bands.id = concerts.band_id
        GROUP BY bands.id, bands.hometown  -- Group by both id and hometown
        ORDER BY concert_count DESC
        LIMIT 1
        """
        CURSOR.execute(query)
        result = CURSOR.fetchone()

        if result:  # Check if a result was found
            return cls(result[0], result[1], result[2]) 
        else:
            return None  # Return None if no result found