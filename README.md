# 50K-requests-in-30-min

This repo contains python code that makes it able to request large no of urls in a high speed.

#Using threading and session 

File reads a txt file 'net_domains.txt' containing 15million rows with with 1 column each having urls. Then hits requests for each of them. 

At last , the status code and errors are counted and placed in a pandas series.
