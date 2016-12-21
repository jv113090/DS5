# Justin Vena's Homework


1.

Justins-MacBook-Air:DataScienceGA JVena$ cd ClassRepo
Justins-MacBook-Air:ClassRepo JVena$ cd ds-sea-05
Justins-MacBook-Air:ds-sea-05 JVena$ cd ls
-bash: cd: ls: No such file or directory
Justins-MacBook-Air:ds-sea-05 JVena$ ls
README.md	data		images		other		slides
code		homework	notebooks	project
Justins-MacBook-Air:ds-sea-05 JVena$ cd data
Justins-MacBook-Air:data JVena$ ls
Airline_on_time_west_coast.csv	pronto_cycle_share
NBA_players_2015.csv		rossmann.csv
Pronto_trip_duration.png	rt_critics.csv
Shawshank.html			sms.tsv
airlines.csv			stores.csv
bank-additional.csv		syria.csv
beer.txt			test.png
beer_histogram.png		time_series_train.csv
beer_histogram1.png		time_series_train.csv.zip
bikeshare.csv			titanic.csv
chipotle.tsv			u.data
citibike_feb2014.csv		u.item
drinks.csv			u.user
drones.csv			u.user_original
example.html			ufo.csv
features.csv.zip		untitled0.py
hitters.csv			untitled1.py
icecream.csv			vehicles_test.csv
imdb_1000.csv			vehicles_train.csv
imdb_ids.txt			yelp.csv
mtcars.csv			yelp.json
ozone.csv

Justins-MacBook-Air:data JVena$ open chipotle.tsv

Justins-MacBook-Air:data JVena$ head chipotle.tsv

Justins-MacBook-Air:data JVena$ tail chipotle.tsv

The columns show each part recorded about type of item in an order. The rows show each item.

2.There are 1834 orders

3.

Justins-MacBook-Air:data JVena$ wc chipotle.tsv

There are 4623 lines

4.

grep "Chicken Burrito" chipotle.tsv
grep “Steak Burrito" chipotle.tsv

More Steak

5. 

grep "Chicken Burrito" "Pinto Beans" chipotle.tsv
grep "Chicken Burrito" “Black Beans" chipotle.tsv

More Black Beans

6. 

Justins-MacBook-Air:ds-sea-05 JVena$ find . -name *csv
Justins-MacBook-Air:ds-sea-05 JVena$ find . -name *tsv

7.

Justins-MacBook-Air:ds-sea-05 JVena$ grep -r  "dictionary" .







