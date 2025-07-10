import  person_pb2

person=person_pb2.Person()
person.name="Charlie"
person.age=25

serialized=person.SerializeToString()
print(f"Serialized data:{serialized}")

deserialized=person_pb2.Person()
deserialized.ParseFromString(serialized)
print(f"Name: {deserialized.name}, Age: {deserialized.age}")