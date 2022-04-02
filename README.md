# OverbondChallenge


# Design choice
Given file XICE_Bond_Close2.tip. I examined lines and found out that for each record keeps information in specific line numbers.
First, issurance date was located in the 6th line of each record and other three informations were located in the last line of record.
Although, each record always had the issurance date, CleanBid, CleanAsk and LastPrice were not always presented in the record.

In order to keep track of each information for each issurance date. I created dictionary containing a date as a key and a list of dictionary containing the other three information. The reason why I chose to make a value a list of dictionary was that the file contained duplicate dates. I decided to keep track of all the records even if it had a duplicate date.


# Trade-offs and additional thoughts
This was my first time dealing with "Bond" data and was not really sure if I had to keep the information of duplicate dates. If I had additional time and supervisor, I would've asked him/her about how to handle duplicate dates. Also, I would like to spend more time on plotting information with detailed axis as given in the graph "pey.md"

# Result
![result](https://user-images.githubusercontent.com/56323360/161400403-b831017d-811a-4708-9ada-9df679174b6a.jpg)

