import setuptools

LONG_DESCRIPTION = 'local2cloud package reads a directory and its subdirectory, uploads all the images(jpg, png, svg, and webp) and media(mp3, mp4, mpeg4, wmv, 3gp, and webm) files to AWS S3 and all the documents (doc, docx, csv, and pdf) files to Google Cloud Storage.'
setuptools.setup(
    name = "local2cloud",
    version = "0.0.1",
    author = "Hritu Rathod",
    author_email = "hriturathod1708@gmail.com",
    description = "Upload local files to cloud",
    long_description = LONG_DESCRIPTION,
    long_description_content_type = "text/markdown",
    url = "https://github.com/hritikarathod/local2cloud.git",
    project_urls = {
        "Bug Tracker": "package issues URL",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
                      'boto3',
                      'google-cloud-storage' ,
                      'oauth2client',
                      'pytest',
                      'pytest-cov'                
                      ],
    package_dir = {"": "scripts"},
    packages = setuptools.find_packages(where="scripts"),
    python_requires = ">=3.6"
)