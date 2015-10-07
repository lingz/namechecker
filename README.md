Instructions
============

MAKE SURE YOU PASS IN THE FILES IN THE RIGHT ORDER

pip install fuzzywuzzy
python checker.py <ALLOWED_FILENAME> <TOCHECK_FILENAME>

It accepts a plaintext file with one name per line

Also included a csv -> plaintext converter in case
you need to create the data from an excel sheet. You can use it like so:
Note the arrow

Usage: python csv_transform.py <CSV> > <OUTPUT_FILENAME>

You can get facebook data the following way

Go To:

https://developers.facebook.com/tools/explorer

Get an access token, making sure to tick user_managed_groups

Then go to (replacing access token):

https://graph.facebook.com/me/groups?access_token=PUT_ACCESS_TOKEN_HERE

Get the right group Id and then go to (replacing group id and access token):

https://graph.facebook.com/GROUP_ID_HERE/members?access_token=ACCESS_TOKEN_HERE

Finally copy and paste it into a file, and then run the following converter:

Usage: python json_transform.py <FACEBOOK_JSON> > <OUTPUT_FILENAMe>


Originally written by Lingliang Zhang (lingliang.zhang@nyu.edu)

