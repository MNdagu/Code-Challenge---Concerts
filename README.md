<h1>CODE CHALLENGE - CONCERTS</h1>

<h2>Object Relationship Methods</h2>


<h3>Concert</h3>
<ul>
<li>Concert.band(): should return the Band instance for this concert.</li>
<li>Concert.venue(): should return the Venue instance for this concert.</li>
</ul>

<h3>Venue</h3>
<ul>
<li>Venue.concerts(): returns a collection of all concerts for the venue.</li>
<li>Venue.bands(): returns a collection of all bands who performed at the venue.</li>
</ul>

<h3>Band</h3>
<ul>
<li>Band.concerts(): should return a collection of all concerts the band has played.</li>
<li>Band.venues(): should return a collection of all venues the band has performed at.</li>
</ul>


<h2>Aggregate and Relationship Methods</h2>

<h3>Concert</h3>
<ul>
<li>Concert.hometown_show(): returns true if the concert is in the band's hometown, false if it is not.</li>
<li>Concert.introduction(): returns a string with the band's introduction for this concert:
"Hello {venue city}!!!!! We are {band name} and we're from {band hometown}"</li>
</ul>

<h3>Band</h3>
<ul>
<li>Band.play_in_venue(venue, date): takes a venue (venue title) and date (as a string) as arguments, and creates a new concert for the band at that venue on that date.</li>
<li>Band.all_introductions(): returns an array of strings representing all the introductions for this band.</li>
<li>Each introduction is in the form: "Hello {venue city}!!!!! We are {band name} and we're from {band hometown}"</li>
<li>Band.most_performances(): returns the Band that has played the most concerts.</li>
</ul>

<h3>Venue</h3>
<ul>
<li>Venue.concert_on(date): takes a date (string) as an argument and finds the first concert on that date at the venue.</li>
<li>Venue.most_frequent_band(): returns the band that has performed the most at the venue.</li>
</ul>