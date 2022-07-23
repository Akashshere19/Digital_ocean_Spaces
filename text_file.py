import boto3
def space_connect(region_name):
    try:
        session = boto3.session.Session()
        client = session.client('s3',
                            region_name=str(region_name),
                            endpoint_url='https://' + str(region_name) + '.digitaloceanspaces.com',
                                aws_access_key_id='********',  # write your  Access_id
                                aws_secret_access_key='*****')  # write your  Access_Key
        print('Successfully connection with spaces..')
    except Exception:
        print('Error in Connection with Spaces')
    #client.create_bucket(Bucket='unverified')
    #--------- showing Buckects -------------------
    try:
       response = client.list_buckets()
       print('\nBuckects are :')

       for space in response['Buckets']:

             print(space['Name'])
    except Exception:
        print('Error in showing buckect')
    #------------- data insert ------------
    try:
           client.put_object(Bucket='verified123',
                      Key='New.ext',
                      Body=r'D:\akash\test.JPG',
                      ACL='private',
                      Metadata={
                          'x-amz-meta-my-key': 'your-value'
                      }
                      )
           print('\nSuccessfully Data Inserted ...')
    except Exception as e:
            print('Error in Data Inserting')
    # ----------  showing Data from Buckects----------
    try:
            response = client.list_objects(Bucket='verified123')
            print('\nData objects: ')
            for obj in response['Contents']:
                print(obj['Key'])
    except Exception:
            print('Error in Data showing from Buckect')

   # -------------Download File from --------------------
    try:
             client.download_file('verified123',
                         'New.ext',
                         r'D:\akash\New.jpg')
             print(r"successfully download at D:\akash\verified")

    except Exception:
             print('Error in Downloading')

    except Exception as e:
              print('some error')

    finally:
            return client
s =space_connect('sgp1')
print('\nsuccess connection with...',s)