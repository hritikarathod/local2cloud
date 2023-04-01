# local2cloud
Upload files to cloud

# Steps to test the project-

1. Run the following command to take clone, (open terminal and go to the folder where you want to take a clone then run this command)
    
    `git clone https://github.com/hritikarathod/local2cloud.git`

2. create a virtual env

    `cd local2cloud/`
    
    `pip install virtualenv`
    
    `virtualenv venv`

3. Activate virtualenv
    
    `source venv/bin/activate`

4. Run the command to go inside the directory in the terminal

    `cd local2cloud/`

5. Run following command to install module
    
    `pip install --upgrade setuptools`
    
    `pip install .`

6. Run the commands to open your Python terminal

    `cd ..`

    `python3`


7. Import module-
    
    `from local2cloud.scripts import transfer`

8. Get a list of files(images,media,documents)
    
    > transfer.get_files(DIR_PATH)

    DIR_PATH is the path of the directory where your files(images,media,documents) are located.
    
    This function will return a json in the following format-

    ```
    {
        "images": [ LIST_OF_IMAGES ],
        "media": [ LIST_OF_MEDIA ],
        "documents": [ LIST_OF_DOCUMENTS ]
    }
    ```

9. Upload files to AWS S3
    
    > transfer.aws_upload(FILELIST, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME)

    FILELIST is the list of the files which you want to upload to AWS S3.

10. Upload files to Google Cloud Storage
    
    > transfer.gcloud_upload(FILELIST, CREDS_FILE, BUCKET_NAME)

    FILELIST is the list of hte files which you want to upload to Google Cloud Storage.
    
    CREDS_FILE is a json file of google credentials.
    
    BUCKET_NAME is the name of the bucket created inside the project on google cloud storage.

    
# Steps to check Pytest Coverage

1. Open Terminal, go to local2cloud path and activate virtualenv, then go to next local2cloud/scrips directory path

    `cd local2cloud/`

    `source venv/bin/activate`

    `cd local2cloud/scripts/`

2. Open "local2cloud/local2cloud/scripts/tests/static/creds/" folder, and update google cloud storage credentials for the follwoing keys in the "creds.json" file.

    * project_id
    * private_key_id
    * private_key
    * client_email
    * client_id
    * client_x509_cert_url

3. Open "local2cloud/local2cloud/scripts/tests/" folder, and update AWS and google cloud storage credentials for the follwoing variables in the "test_transfer.py" file.

    * AWS_ACCESS_KEY_ID
    * AWS_SECRET_ACCESS_KEY
    * BUCKET_NAME
    * GOOGLE_BUCKET_NAME


4. Run the test cases

    `python -m pytest tests`

5. Check coverage

    `python -m pytest --cov --cov-report=html:coverage_re`

    After executing this command, you will be able to see a folder "coverage_re" inside "local2cloud/local2cloud/scripts". Just go to the folder "coverage_re" and run the index.html file on browser.


