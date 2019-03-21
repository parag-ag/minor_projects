Once on youtube, I found a video "See who stalks you on facebook!". It showed that after logging in to Facebook if we view the source code and search Initialchatfriendslist, the numbers in that list shows who has viewed your profile the most.
You just have to copy that no. and type "https://www.facebook.com/<-number->" in your browser search bar and that person's profile will appear.
But there were a lot of numbers (approx 500) and I wanted to see them all. But copying and pasting numbers in search bar was a boring process. So, I made a python script to do the same for me.

NOTE: Later I get to know that Initialchatfriendslist is not about the people who viewed my profile but its about overall activities of that person related to me ( chatting, post likes and comments, profile view, shares etc.)

How it works :
1. Login to your Facebook account in your browser.
2. View source code
3. Search for 'InitialChatFriendslist' and copy the whole list of nos. (Sometimes it also includes some group details so to take look of only people search for  list:["  and copy the complete list.)
4. Run this python script and paste the list there.

It will start showing you the name of peoples who according to Facebook are your good friends (in "best friend first" order)