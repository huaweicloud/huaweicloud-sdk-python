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


# get a single volume attachment on a server
def get_server_volume_attachment(vol_id, ser_id):
    attachment = conn.compute.get_volume_attachment(vol_id, ser_id)
    print (attachment)
    print ("volume_id is :", attachment.volume_id)
    print ("server_id is :", attachment.server_id)


# get server volume attachments information.
def volume_attachments(server_id):
    attachments = conn.compute.volume_attachments(server_id)
    print("volume attachments information is:")
    for attachment in attachments:
        print ("volume_id is :", attachment.volume_id)


# attach a volume to a server
def create_volume_attachment(server_id, volume_id):
    attrs = {
        "volumeId": volume_id,
        "device": "/dev/sdc"
    }
    response = conn.compute.create_volume_attachment(server_id, **attrs)
    print (response)
    print ("volume id: ", response.id)


# detach a volume from a server
def delete_volume_attachment(server_id, volume_id):
    conn.compute.delete_volume_attachment(volume_id, server_id)


if __name__ == "__main__":
    volume_id = "volume_id"
    server_id = "server_id"
    get_server_volume_attachment(volume_id, server_id)
    volume_attachments(server_id)
    delete_volume_attachment(server_id, volume_id)
    create_volume_attachment(server_id, volume_id)
