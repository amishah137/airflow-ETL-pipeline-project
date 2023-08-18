# airflow-ETL-pipeline-project
This project extracts user information using Twitter API, uses python to transform data, deploy the code on Airflow/EC2 and save the final result on Amazon S3.

## Prerequisites
1. Twitter APIs - To avail the Twitter APIs (Tweepy package), setup an tweeter account and get api credentials.
2. AWS Account - To use EC2 and S3 instance.

## Steps to follow:
1. Create an EC2 instace with:
  - name: airflow-test
  - OS: Ubuntu
  - Instance type: t2.micro
  - key-pair(name, type, file format): airflow-ec2-key, RSA, ".pem" (default)
  - Network settings: check "Allow HTTPS traffic from Internet" and "Allow HTTP traffic from Internet".
  - Now, Launch the EC2 instance
2. Login into the instance using SSH client and update the instance as follow:
    ```
    sudo apt-get update
    sudo apt install python3-pip
    sudo pip install apache-airflow
    sudo pip install pandas 
    sudo pip install s3fs
    sudo pip install tweepy
    ```
    Now, Check the airflow is working
    ```
    airflow
    ```
    ```
    airflow standalone
    ```
    note down the username and password
3. Create AWS S3 bucket with name 'ami-airflow-etl-test' with EC2.
4. Create IAM role with name 'ec2_s3_airflow_role'. (note: use underscore instead of hyphens)
5. Associate it to our EC2 instance.
6. Open a new terminal of EC2 instance.
    ```
    cd airflow
    ```
    ```
    mkdir tweeter && cd tweeter
    ```
    Copy two files here the folder tweeter.
7. Go to first terminal and restart the airflow.

Go to Dashboard :

