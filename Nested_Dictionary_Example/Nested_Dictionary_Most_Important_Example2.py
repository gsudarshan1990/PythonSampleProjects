"""
Find the value of duration from the below dictionary

"""


response={"users": [
{	"type": "postData",
	"data": {
		"postId":"443328e9497740b456154c636349",
		"postTimestamp": "1521543600",
		"pageType": "/home.php:topnews",
		"viewTime": 1521545993647,
		"gender": 3,
		"likes": "8",
		"comments_shares_viewes": ["1"],
		"posters": [{"type": "page",
			"id": "695e45affa1e07529ac917f6d573a"} ],
		"postImg": 1,
		"postDesc": [253],
		"origLink": 0,
        "duration": 0,
		"timestamp": 1521545993647},
	    "back_time": 1521545993693},
			{"type": "saveLooked",
			"data": {
				"duration": 18,
				"timestamp": 1521545993656,
				"sessionId": 639,
				"gender": 2},
				"back_time": 1521546011657}
]}

print(type(response))
import json
#print(json.dumps(response,indent=2))
response1=response['users']
#print(type(response1))
for response2 in response1:
    #print(type(response2))
    #print(response2.keys())
    response3=response2['data']
    #print(type(response3))
    #print(response3.keys())
    print(response3['duration'])
