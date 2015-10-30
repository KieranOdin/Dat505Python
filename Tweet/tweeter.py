import twitter, datetime, sqlite3, sys


#Opens twitter credentials and saves to a string array

user = 42858262
file = open("TwitterCredentials.txt")
creds = file.readline().strip().split(',')
api = twitter.Api(creds[0],creds[1],creds[2],creds[3])
statuses = api.GetUserTimeline(user)
print (statuses[0].text)


#

#f = open('C:\Users\Kieran\AppData\Local\Google\Chrome\User Data\Default\History', 'rb')
f = open('/Users/kodinius/Library/Application Support/Google/Chrome/Default/History', 'rb')
data = f.read()
f.close()
f = open('DATA', 'w')
f.write(repr(data))
f.close()

#con = sqlite3.connect('data.db')
#cur = con.cursor()
#rows = cur.fetchall()
conn = sqlite3.connect('/Users/kodinius/Library/Application Support/Google/Chrome/Default/History/data.db')

f = open('SEARCH.txt', 'r')
search = f.readline()
search = search.split(',', search.count(','))
data = data.split(',', data.count(','))
print search

timestamp = datetime.datetime.utcnow()
response = api.PostUpdate("Kieran has been looking at: " + str(timestamp))
print("Status updated to: " + response.text)



#for x in range(0,len(row)):
    #if row[x] in search:
        #timestamp = datetime.datetime.utcnow()
        #response = api.PostUpdate("Kieran has been looking at: " + search + ' at ' + str(timestamp))
        #print("Status updated to: " + response.text)
        #print search
    

#for x in range(0,len(data)):
	#if data[x] in search:
		#timestamp = datetime.datetime.utcnow()
        #response = api.PostUpdate("Kieran has been looking at: " + search + ' at ' + str(timestamp))
        #print("Status updated to: " + response.text)
        #print search

    