import json 

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def to_json(self):
        return json.dumps(self.__dict__)
    
    @classmethod
    def from_json(cls, json_str):
        data=json.loads(json_str)
        return cls(**data)
    
person=Person("bonnie", 30)
serialized_person = person.to_json()
print(serialized_person)
deserialized_person = Person.from_json(serialized_person)
print(f"Name: {deserialized_person.name}, Age: {deserialized_person.age}")