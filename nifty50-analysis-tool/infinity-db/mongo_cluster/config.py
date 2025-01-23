# MongoDB Sharded Cluster Configuration

MONGO_CLUSTER_SETTINGS = {
    'shards': [
        {'host': 'shard1.mongodb.net', 'port': 27017},
        {'host': 'shard2.mongodb.net', 'port': 27017},
        {'host': 'shard3.mongodb.net', 'port': 27017}
    ],
    'replica_set': 'rs0',
    'auth_source': 'admin',
    'username': 'clusterAdmin',
    'password': 'securePassword123',
    'ssl': True
}

def get_mongo_uri():
    shards = MONGO_CLUSTER_SETTINGS['shards']
    shard_hosts = ','.join([f"{shard['host']}:{shard['port']}" for shard in shards])
    return f"mongodb://{MONGO_CLUSTER_SETTINGS['username']}:{MONGO_CLUSTER_SETTINGS['password']}@{shard_hosts}/?replicaSet={MONGO_CLUSTER_SETTINGS['replica_set']}&authSource={MONGO_CLUSTER_SETTINGS['auth_source']}&ssl={str(MONGO_CLUSTER_SETTINGS['ssl']).lower()}"
