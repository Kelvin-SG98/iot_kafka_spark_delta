from kafka import KafkaAdminClient

admin = KafkaAdminClient(bootstrap_servers='localhost:29092')
print(admin.list_topics())