# -*-coding:utf-8 -*-

from openstack import connection

# create connection
username = "xxxxxx"
password = "xxxxxx"
projectId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # tenant ID
userDomainId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # user account ID
auth_url = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # endpoint url
conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             project_id=projectId,
                             username=username,
                             password=password)


# get list of image
def list_images():
    images = conn.compute.images()
    for image in images:
        print(image)


# show image detail
def get_image(image_id):
    image = conn.compute.get_image(image_id)
    print(image)


# find image
def find_image(image_id):
    image = conn.compute.find_image(image_id)
    print(image)


# get image metadata
def get_image_metadata(image_id):
    image_metadata = conn.compute.get_image_metadata(image_id)
    print(image_metadata)


# delete image
def delete_image(image_id):
    conn.compute.delete_image(image_id)


if __name__ == "__main__":
    image_id = "6422e642-e81f-4f85-a4a4-74bc36e8c7d9"
    list_images()
    get_image(image_id)
    find_image(image_id)
    get_image_metadata(image_id)
    delete_image(image_id)
