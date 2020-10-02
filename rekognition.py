import boto3
import json
import csv

#upload SS photo of celebrity/
photo= 'profession.jpeg'

client=boto3.client('rekognition',
	aws_access_key_id='ASIAQUQRSLPB6DHBB57V',
	aws_secret_access_key='wlKtDZNFZ52Mtbiw+UhYSl/kGOVNTkYfZBIBSX5S',
	aws_session_token='FwoGZXIvYXdzEHEaDCvTAYZv36/sgfjC9SLbARUqCyk+ce3+Jl9KSuMApb4AC/XFwZcqKBqdlDaptk7CT5SXopxa2fKnUfzy3M7CjS+yAli4qKUK0Ujb0sD4JHMThcw/ErfTHt8o0huASQtS4OfWleZC/AaIQG+lUoN2L8Hb3iMOz/rt2DB2kajgPYt5J/BCHuYM0K54BRpLha5+kx/EtR9xFYojXSFgiC8oilGF1HrE+jjbeJfBTprm3EamLijz/WnOXC56bmIEUURBqvgzQXLshvl21P93JuuB/tO7J6qzhuZS/nx4fGTiA+Nx+6KcwnBEwksuLSjPstv7BTIttpLfQdXfpksCHUcPZ8szVUc9mb5bbbBPpjCTGtkQFNJnLh5VuSbYuy1fagNH')

#read the photo with detect_faces
with open(photo,'rb') as image:
	response=client.detect_faces(Image={'Bytes':image.read()},Attributes=['ALL'])

#get response in string format and convert it to dict format
response_string=json.dumps(response)
obj= json.loads(response_string)

#Print output in csv format
emp = obj['FaceDetails'][0]
print(type(emp))
print(emp)
data_file = open('data_file.csv', 'w')
csv_writer=csv.writer(data_file)

#get the key of output
header = emp.keys()

csv_writer.writerow(header)

# Writing data of CSV file
csv_writer.writerow(emp.values())

data_file.close()
