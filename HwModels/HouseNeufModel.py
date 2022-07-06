from HwModels.DbModel import DbModel

class HouseNeufModel(DbModel):

    def __init__(self):
        self.TableName = "hw_neuf_house_model"

        pass


    def attributes(self):
        return [
            {"name":"id","type":"int"},
            {"name":"surface_string","type":"string"},
            {"name":"etage","type":"int"},
            {"name":"prix_string","type":"string"},
            {"name":"utime","type":"string"},
            {"name":"ctime","type":"string"}

        ]