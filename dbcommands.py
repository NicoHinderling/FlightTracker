from cassandra.cluster import Cluster

def createKeySpace(session, title, class_type='SimpleStrategy', replication_factor='3'):
    session.execute("""
    CREATE KEYSPACE {}
    WITH REPLICATION = { 'class' : '{}', 'replication_factor' : {} };
    """.format(title, class_type, replication_factor))