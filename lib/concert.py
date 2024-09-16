from __init__ import CONN, CURSOR

class Concert:
    def __init__(self, id, band_id, venue_id, date) -> None:
        self.id = id
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date
        
    
        
    @classmethod
    def create(cls, band_id, venue_id, date):
        query = """
        INSERT INTO concerts (band_id, venue_id, date)
        VALUES (?, ?, ?)
        """
        CURSOR.execute(query, (band_id, venue_id, date))
        CONN.commit()
        return cls(CURSOR.lastrowid, band_id, venue_id, date)

    def band(self):
        query = """
        SELECT * FROM bands
        WHERE id = ?
        """
        CURSOR.execute(query, (self.band_id,))
        return CURSOR.fetchone()

    def venue(self):
        query = """
        SELECT * FROM venues
        WHERE id = ?
        """
        CURSOR.execute(query, (self.venue_id,))
        return CURSOR.fetchone()

    def hometown_show(self):
        query = """
        SELECT venues.city, bands.hometown
        FROM concerts
        JOIN venues ON concerts.venue_id = venues.id
        JOIN bands ON concerts.band_id = bands.id
        WHERE concerts.band_id = ? AND concerts.venue_id = ?
        """
        CURSOR.execute(query, (self.band_id, self.venue_id))
        result = CURSOR.fetchone()
        
        if result:  # Ensure there's a result before unpacking
            city, hometown = result
            return city == hometown
        else:
            return False  # Return False if no result found

    def introduction(self):
        query = """
        SELECT bands.name, bands.hometown, venues.city
        FROM bands 
        JOIN venues ON venues.id = ?
        WHERE bands.id = ?
        """
        CURSOR.execute(query, (self.venue_id, self.band_id))
        band_name, band_hometown, venue_city = CURSOR.fetchone()
        return f"Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}"
