# Movie Finder

#### Movie finder scraper crwal **[YTS.AG](yts.ag)** movie torrent site. Output a list of movie according to movie quality, genre, rating and order by.

## Installation

    pip install scrapy

## Usage
    scrapy crawl finder -o output.csv


##### After crawling data will save in **output.csv** file.

##### You can save data others formats also like json, xml etc. Just change file type in crawler command.


##### Here i crawl Biography movie that has 8+ rating. To crawl others category go [yts.ag](https://yts.ag/browse-movies) and select all category that you want and search. Then copy the url from urlbar and paste it into **[finder.py]()** file in **start_urls** line [16]().


## Output

* Movie name
*Release year
* Likes
* Rotten
* Tomatoes Critics
* Rotten Tomatoes Audience
* IMDB
* Download links
    * 3D
    * 720P
    * 1080P

##### This data will be in csv file. See a demo output file [here](gist.github.com)


###### This data will be in output file.


>N.B: This is an educational purpose project. Commercial use of the [YTS.AG](yts.ag)  data may require permission from the authority.
