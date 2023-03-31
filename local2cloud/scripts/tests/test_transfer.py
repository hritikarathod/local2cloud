import pytest
import transfer

#AWS Credentials
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
BUCKET_NAME = ''
FILE_LOCATION = './tests/static/'

#Gcloud Credentials
CREDS_FILE = './tests/static/creds/cred.json'
GOOGLE_BUCKET_NAME = ''

def test_get_files():
    # test get_files with wrong path
    output = transfer.get_files('./test/')
    # Verify the output of `get_files` function
    assert len(output) == 0
    # test get_files with correct path
    output = transfer.get_files(FILE_LOCATION)
    # Verify the output of `get_files` function
    assert len(output) == 3
    assert len(output["images"]) == 1
    assert len(output["media"]) == 1
    assert len(output["documents"]) == 1

def test_aws_img_upload():
    output = transfer.get_files(FILE_LOCATION)
    # test aws_upload with wrong credetials
    transfer.aws_upload(output["images"], 'AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'BUCKET_NAME')
    # test aws_upload with empty imagelist
    transfer.aws_upload([], AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME)
    # test aws_upload with imagelist
    transfer.aws_upload(output["images"], AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME)
    # test aws_upload with wrong imagelist
    transfer.aws_upload(["test.png"], AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME)

def test_aws_media_upload():
    output = transfer.get_files(FILE_LOCATION)
    # test aws_upload with empty filelist
    transfer.aws_upload([], AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME)
    # test aws_upload with filelist
    transfer.aws_upload(output["media"], AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME)
    # test aws_upload with wrong filelist
    transfer.aws_upload(["test.mp3"], AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME)
    

def test_gcloud_upload():
    output = transfer.get_files(FILE_LOCATION)
    # test gcloud_upload with wrong credetials
    transfer.gcloud_upload(output["documents"], 'CREDS_FILE', 'GOOGLE_BUCKET_NAME')
    # test gcloud_upload with empty doclist
    transfer.gcloud_upload([], CREDS_FILE, GOOGLE_BUCKET_NAME)
    # test gcloud_upload with doclist
    transfer.gcloud_upload(output["documents"], CREDS_FILE, GOOGLE_BUCKET_NAME)
    # test gcloud_upload with wrong doclist
    transfer.gcloud_upload("testing.doc", CREDS_FILE, GOOGLE_BUCKET_NAME)


    