from pymongo import MongoClient

class MongoDB:
    def __init__(self, collection):
        self.client = MongoClient("mongodb://localhost:27017/")  
      
        cursor = self.client["apiCards"]
        self.collection = cursor[collection]

    def read_all(self):
        output = []
        for obj in self.collection.find():
            output.append(obj)
        return output

    def read_by_id(self, id):
        output = self.collection.find_one(id)
            
        return output

    def read_with_filter(self,filter):
        output = []
        for obj in self.collection.find():
            if str(filter) in str(obj['tags']):
                output.append(obj)
        return output

    def find_by_name(self,name):
        output = self.collection.find_one(name)
        return output

    def insert(self, data):
        response = self.collection.insert_one(data)
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id),
                  "ID": data['id']}
        return output

    def bulk_insert(self, data):
        response = self.collection.insert_many(data)
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_ids),
                  "ID": data['id']}
        return output

    def update(self, data):
        filt = {}
        filt['id'] = data['id']
        updated_data = {"$set": data['newData']}
        response = self.collection.update_one(filt, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete(self, data):
        filt = data
        response = self.collection.delete_one(filt)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output