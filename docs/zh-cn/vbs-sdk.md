# VBS SDK

HuaWei OpenStack `Volume Backup` 服务SDK
- 服务入口: `conn.volume_backup`
- 服务类型: `volume-backup`


## API接口文档

请查阅 [官方接口文档](https://docs.otc.t-systems.com/en-us/api/vbs/en-us_topic_0061309333.html)


## 云硬盘备份

### 创建备份
```python
# 要备份的卷ID
volume_id = "xxxxxx"
backup = {
    "volume_id": volume_id,
    "name": "volume-backup-xxxx",
    "description": "created by openstacksdk"
}
job = conn.volume_backup.create_backup(**backup)
```

### 从备份恢复磁盘
```python
volume_backup_id = "xxxxxxx"
# 要恢复到的卷ID
volume_id = "xxxxxx"
job = conn.volume_backup.restore_backup(volume_backup_id, volume_id)
```

### 创建备份（原生）
```python
volume_id = "c68ae7fb-0aa5-4a97-ab01-ed02c5b7e768"
snapshot_id = "2bb856e1-b3d8-4432-a858-09e4ce939389"
data = {
    "volume_id": volume_id,
    "snapshot_id": snapshot_id,
    "name": "native-volume-backup-1",
    "description": "created by openstacksdk"
}
backup = conn.volume_backup.create_native_backup(**data)
```

### 查询备份概要信息列表（原生）
```python
query = {
    "name": "some-backup",
    "status": "available",
    "volume_id": "0781095c-b8ab-4ce5-99f3-4c5f6ff75319",
    "marker": "some-backup-id",
    "limit": 10
}
backups = listconn.volume_backup.backups(**query))
```

### 查询备份详细信息列表（原生）
```python
query = {
    "name": "some-backup",
    "status": "available",
    "volume_id": "0781095c-b8ab-4ce5-99f3-4c5f6ff75319",
    "marker": "some-backup-id",
    "limit": 10
}
backups = listconn.volume_backup.backups(details=True, **query))
```

### 查询单个备份详情（原生）
```python
volume_backup_id = "xx"
volume_backup = conn.volume_backup.get_backup(volume_backup_id)
```

### 删除备份（原生）
```python
conn.volume_backup.delete_backup("volume_backup_id")
```


### 查询job的状态
```python
# 这个API比较特殊，因为他的版本跟其他的API都不一样。
# 还在跟VBS的同事确认，能否在v2版本也放一个API
conn.volume_backup.get_job("job_id")
```


## 备份策略
### 创建备份策略
```python
data = {
    "remain_first_backup_of_curMonth": True,
    "rentention_num": 10,
    "frequency": 1,
    "start_time": "12:00",
    "status": "ON"
}
volume_backup_name = "SDK-backup-test-1"
policy = conn.volume_backup.create_backup_policy(volume_backup_name, **data)
```

### 查询备份策略列表
```python
policies = list(conn.volume_backup.backup_policies())
```

### 修改备份策略
```python
updated = {
    "scheduled_policy": {
        "frequency": 5,
        "start_time": "01:00"
    }
}
policy = BackupPolicy(id="policy-id")
conn.volume_backup.update_backup_policy(policy, **updated)
```

### 删除备份策略
```python
policy = BackupPolicy(id="policy-id")
conn.volume_backup.delete_backup_policy(policy)
```

### 绑定资源到备份策略
```python
policy = BackupPolicy(id="policy-id")
volumes = ["volume-id-1", "volume-id-2",]
conn.volume_backup.link_resources_to_policy(policy, volumes)
```

### 从备份策略解绑资源
```python
policy = BackupPolicy(id="policy-id")
volumes = ["volume-id-1", "volume-id-2",]
conn.volume_backup.unlink_resources_of_policy(policy, volumes)
```

### 立即执行备份策略
```python
policy = BackupPolicy(id="policy-id")
conn.volume_backup.execute_policy(policy)
```

### 启用备份策略
```python
policy = BackupPolicy(id="policy-id")
conn.volume_backup.enable_policy(policy)
```


### 停用备份策略
```python
policy = BackupPolicy(id="policy-id")
conn.volume_backup.disable_policy(policy)
```

### 查询策略下的备份任务
```python
query = {
    "id": "0781095c-b8ab-4ce5-99f3-4c5f6ff75319", # job_id 也是一样效果
    "sort_dir": "asc",
    "sort_key": "created_at",
    "status": "RUNNING",
    "limit": 10,
    "offset": 10
}
backup_policy_id = "policy-id"
tasks = list(conn.volume_backup.tasks(backup_policy_id, **query))
```


