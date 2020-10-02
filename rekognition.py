import boto3
import json
import csv

#upload SS photo of celebrity/
photo= 'profession.jpeg'

client=boto3.client('rekognition',
	aws_access_key_id='ASIAQUQRSLPB7KLUBHWE',
	aws_secret_access_key='7K7V8Hl55B0saBjbb41E49kUE/tlyB2dVs0nPHqL',
	aws_session_token='FwoGZXIvYXdzEHIaDFvFvFXx+U1gML1aySLbAewREid6L34KIPpYSguFdEydJ71a\
		5FL4i3oJdrTD3n4I7Tc/J8Obx1QuFKR1i52J1MVcit2gN+W1tBHXEth/evAJzRQRp5xIniE8AGu4OsEifPbdiU4\
		gbJzBLYl/ZURyTc4ANCUDWxTfpf8AdoC9qk1rgFUmep2slmXaQBIUb1XwrTRt9u+fvE9bfnAgv6pO34U+JYCphV\
		18G7+il0ess8Y3SfmJRvpFjVELzUD0Sev7RySJM8MBSJkrdq/LUcYZgVXAFpkXxz5YVk8ZRvcKchxF5KlF1tlrK\
		btnbSi20tv7BTItzgVNV0R++1fQfXI470cddBE8+OayylGji9CEJw7LoJ6LeeZStQq5faUV5UIU'
)
#read the photo with dete_faces
with open(photo,'rb') as image:
	response=client.detect_faces(Image={'Bytes':image.read()},Attributes=['ALL'])

#get response in string format and convert it to dict format
response_string=json.dumps(response)
obj= json.loads(response_string)

#Print output in csv format
emp = obj['FaceDetails'][0]

with open('data_file.csv', 'w') as data_file:
	csv_writer=csv.writer(data_file)
	#get the key of output
	header = emp.keys()

	csv_writer.writerow(header)

	# Writing data of CSV file
	csv_writer.writerow(emp.values())

