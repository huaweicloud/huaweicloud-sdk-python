# -*- coding:utf-8 -*-
from openstack import connection


# Query Alarm List
def list_alarms(connection):
    query = {
        "limit": 1,
        "start": "al1569570560505mk5veYL9g",
        "order": "desc"
    }

    alarmIDs = []
    for alarm in connection.cloud_eye.alarms(**query):
        alarmIDs.append(alarm.id)
    return alarmIDs[0]


# Query Alarm By AlarmID
def get_alarm(connection, alarm_id):
    alarm = connection.cloud_eye.get_alarm(alarm_id)
    print("Alarm name: ", alarm.name)
    print("Alarm description: ", alarm.description)
    print("Alarm metric: ", alarm.metric)


# Delete Alarm By AlarmID
def delete_alarm(connection, alarm_id):
    connection.cloud_eye.delete_alarm(alarm_id)


# Enable Alarm By AlarmID
def enable_alarm(connection, alarm_id):
    connection.cloud_eye.enable_alarm(alarm_id)


# Disable Alarm By AlarmID
def disable_alarm(connection, alarm_id):
    connection.cloud_eye.disable_alarm(alarm_id)


if __name__ == "__main__":
    # create connection
    username = "xxxxxxxxxxxxxx"
    password = "xxxxxxxxxxxx"
    projectId = "xxxxxxxxxxxxxxxxxxxxxx"  # tenant ID
    userDomainId = "xxxxxxxxxxxxxxx"  # user account ID
    auth_url = "xxxxxxxxxxxxxxxxxxxxxx"  # endpoint url

    conn = connection.Connection(auth_url=auth_url,
                                 user_domain_id=userDomainId,
                                 project_id=projectId,
                                 username=username,
                                 password=password)

    alarmID = list_alarms(conn)
    get_alarm(conn, alarmID)
    enable_alarm(conn, alarmID)
    disable_alarm(conn, alarmID)
    delete_alarm(conn, alarmID)

