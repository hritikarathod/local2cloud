import os
import boto3
import botocore
import logging


# Set up our logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def get_files(dir_path):
	#we shall store all the file names in this list
	imglist = []
	filelist = []
	doclist = []

	images_suffix = ("jpg", "png", "svg", "webp", "jpeg")
	media_suffix = ("mp3", "mp4", "mpeg4", "wmv", "3gp", "webm")
	docs_suffix = ("doc", "docx", "csv", "pdf")
	count = 0
	
	if not os.path.isdir(dir_path):
		logger.info('Path does not exists')
		return []

	for root, dirs, files in os.walk(dir_path):
		for f1 in files:
			file_path = os.path.join(root,f1)
			if (f1.endswith(images_suffix)):
				imglist.append(file_path) #append the file name to the image list
			elif (f1.endswith(media_suffix)):
				filelist.append(file_path) #append the file name to the media list
			elif(f1.endswith(docs_suffix)):
				doclist.append(file_path)  #append the file name to the document list
			else:
				count+=1			

	if count>0:
		print(count, "non relavent file(s) found")
	
	response = {
		"images":imglist,
		"media":filelist,
		"documents":doclist
	}
	return response

def aws_upload(filelist, aws_access_key_id, aws_secret_access_key, bucket_name):
	if len(filelist)>0:
		s3 = boto3.client(
			's3',
			aws_access_key_id=aws_access_key_id,
			aws_secret_access_key=aws_secret_access_key,
		)
		
		try:
			logger.info('Calling S3 API')
			for index, name in enumerate(filelist):
				print(index+1, "/", len(filelist), " uploading...")
				key_name = name.split("/")[-1]
				s3.upload_file(
					Filename=name,
					Bucket=bucket_name,
					Key=key_name
				)	
			logger.info('Successfully uploaded all the files')		
		except botocore.exceptions.ClientError as error:
			if error.response['Error']['Code'] == 'AccessDenied':
				logger.warn('Do not have the required permissions')
			else:
				print("Unexpected error: %s" % error)
		except boto3.exceptions.S3UploadFailedError as error:
			print("Unexpected error: %s" % error)
		except Exception as error:
			print("Unexpected error: %s" % error)	
	else:
		logger.info('File not found')

def gcloud_upload(doclist, creds_file, bucket_name ):
	if len(doclist)>0:
		from google.cloud import storage
		from oauth2client.service_account import ServiceAccountCredentials

		try:
			logger.info('Calling Google Cloud API')
			
			storage_client = storage.Client.from_service_account_json(creds_file)

			bucket = storage_client.get_bucket(bucket_name)
			
			for index, name in enumerate(doclist):
				print(index+1, "/", len(doclist), " uploading...")				
				blob = bucket.blob(name)
				blob.upload_from_filename(name)
			logger.info('Successfully uploaded all the files')
		except Exception as error:
			print("Unexpected error: %s" % error)		
	else:
		logger.info('File not found')