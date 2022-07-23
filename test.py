import boto3
def space_connect(region_name):

    session = boto3.session.Session()
    client = session.client('s3',
                            region_name=str(region_name),
                            endpoint_url='https://' + str(region_name) + '.digitaloceanspaces.com',
                            aws_access_key_id='********',# write your  Access_id
                            aws_secret_access_key='*****')# write your  Access_Key

    #client.create_bucket(Bucket='unverified')
    #--------- showing Buckects -------------------

    response = client.list_buckets()
    print('Buckects are :')
    for space in response['Buckets']:

         print(space['Name'])

    #------------- data insert ------------
    client.put_object(Bucket='epod-documents',
                      Key='photo.JPG',
                      #Body=b'hello world',
                      ACL='private',
                      Metadata={
                          'x-amz-meta-my-key': 'your-value'
                      }
                      )
    # ----------  showing Data from Buckects----------

    response = client.list_objects(Bucket='epod-documents')
    print('\nData objects: ')
    for obj in response['Contents']:
        print(obj['Key'])

   # -------------Download File from --------------------
    client.download_file('epod-documents',
                         'photo.JPG',
                         r'D:\akash\unverified\photo.jpg')
    print(r'download successfully at D:\akash\unverified')


    return client

s =space_connect('sgp1')
print('\nsuccess connection with...',s)