from concert import Concert
from venue import Venue
from band import Band

chainsmokers = Band(9, "chainsmokers", "LA")
print(chainsmokers)

sofi_stadium = Venue(6, "Sofi Stadium", "LA")
print(sofi_stadium)

chainsmokers_concert = Concert(9, 9, 6, '2024-10-20')

chainsmokers_venues = chainsmokers.venues()
print(f"chainsmokers Venues: {chainsmokers_venues}")  

# Test 'play_in_venue' method
chainsmokers.play_in_venue("Sofi Stadium", "2024-10-20")
print(f"Concerts for chainsmokers: {chainsmokers.concerts()}")  

# Test 'all_introductions' method
chainsmokers_introductions = chainsmokers.all_introductions()
print(f"chainsmokers Introductions: {chainsmokers_introductions}")  

# Test 'most_performances' method
most_performances_band = Band.most_performances()
print(f"Band with most performances: {most_performances_band}")


# Test 'concert_on' method
concert_on_date = sofi_stadium.concert_on("2024-10-20")
print(f"Concert at olympic stadium on 2024-10-20: {concert_on_date}")  

# Test 'most_frequent_band' method
most_frequent_band_sofi_stadium = sofi_stadium.most_frequent_band()
print(f"Most frequent band at sofi stadium: {most_frequent_band_sofi_stadium}")  

# Test 'introduction' method
introduction = chainsmokers_concert.introduction()
print(f"Concert Introduction: {introduction}")


# Test 'hometown_show' method
is_hometown_show = chainsmokers_concert.hometown_show()
print(f"Is it a hometown show? {is_hometown_show}") 

