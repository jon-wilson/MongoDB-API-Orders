

class FairfieldUDW: 
    def __init__(self, data, db):   # Fetchs the MongoDB, by making use of Request Body   
        self.collection = db[data.pop('collection')]
        self.data = data

    def insert_data(self, data): 
        new_document = data['document']
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Successfully Inserted', 'Document_ID': str(response.inserted_id)}
        return output

    def read(self): 
        documents = self.collection.find(self.data)
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def update_data(self):
        filter = self.data['filter']
        updated_data = {"$set": self.data['dataToBeUpdated']}
        response = self.collection.update_one(filter, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete_data(self, data):
        filter = data['filter']
        response = self.collection.delete_one(filter)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output