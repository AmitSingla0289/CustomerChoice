import json
class Response():
    def __init__(self,buisnessType):
        self.Service_Name = None
        self.URL = None
        self.Category = None
        self.Sub_Category = None
        self.Image = None
        self.serviceRecord = []
        self.buisnessType = buisnessType

    @property
    def Service_Name(self):
        return self._Service_Name

    @Service_Name.setter
    def Service_Name(self, value):
        self._Service_Name = value
    @property
    def URL(self):
        return self._URL

    @URL.setter
    def URL(self, value):
        self._URL = value
    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, value):
        self._Category = value

    @property
    def Sub_Category(self):
        return self._Sub_Category

    @Sub_Category.setter
    def Sub_Category(self, value):
        self._Sub_Category = value

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, value):
        self._Image = value

    @property
    def buisnessType(self):
        return self._buisnessType

    @buisnessType.setter
    def buisnessType(self, value):
        self._buisnessType = value


    def addRecord(self,serviceRecordd):
        self.serviceRecord.append(serviceRecordd)

    def dump(self):
        store_data_dict = {}
        string1 = []
        for item in self.serviceRecord:
            string1.append(item.str11())
            #str(item)
        return {
            "url": self._URL,
            "category": self._Category,
            "sub_category": self._Sub_Category,
            "image_src": self._Image,
            "reviews": string1}

        #Sreturn json.dumps(store_data_dict).replace("/", "\\/")

    def __repr__(self):
        store_data_dict = {}
        string1 = ""
        for item in self.serviceRecord:
            string1 = string1 + item.str()
            #str(item)
        store_data_dict[self.Service_Name] = {"business_item_data": {
            "business_type":self.business_type,
            "absolute_url": self._URL,
            "category": self._Category,
            "name":self.Service_Name,
            "sub_category": self._Sub_Category,
            "picture_urls": self._Image},
            "reviews": string1}
        return json.dumps(store_data_dict)



