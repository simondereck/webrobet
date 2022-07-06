from HwModels.DbModel import DbModel


class estimateModel(DbModel):


    id_mutation = "" #2020-1
    date_mutation = "" #2020-01-07
    numero_disposition = 0 #somthing not know
    nature_mutation = "" #vente 买卖类型
    valeur_fonciere = 0.01 #80000 价格
    adresse_numero = 0 # 11 RUE
    adresse_suffixe = "" # 5A 3B RUE
    adresse_nom_voie = "" #RUE NOM

    adresse_code_voie = "" #NOT SO IMPORT B112
    code_postal = "" #75001 OR SIZE<5 ADD 0 BEFORE
    code_commune = "" #75101 FOR SOMTHIG BUT DIDN'T USEFURL
    nom_commune = "" #city nom

    code_departement = "" #unkonw colum

    ancien_code_commune = "" #unkonw colum
    ancien_nom_commune = "" #unknow colum

    id_parcelle = "" #unknow colum
    ancien_id_parcelle = "" #unknow colum

    numero_volume = ""

    lot1_numero = ""
    lot1_surface_carrez = 0.01

    lot2_numero = ""
    lot2_surface_carrez = 0.01


    lot3_numero = ""
    lot3_surface_carrez = 0.01

    lot4_numero = ""
    lot4_surface_carrez = 0.01


    lot5_numero = ""
    lot5_surface_carrez = 0.01

    nombre_lots = 0

    code_type_local = 1 # 1 masion 2 appartement 3 dependacnce

    type_local = "" # masion appartement

    surface_reelle_bati = 0.01 #面积

    nombre_pieces_principales = 0 #几间房

    code_nature_culture = "" #类型

    nature_culture = ""

    code_nature_culture_speciale = "" #unknow colum

    nature_culture_speciale = ""


    surface_terrain = 0.01 #占用面积

    longitude = ""

    latitude = ""

    def attributes(self):
        # return ["id_mutation","date_mutation","numero_disposition",
        #         "nature_mutation","valeur_fonciere","adresse_numero",
        #         "adresse_suffixe","adresse_nom_voie","adresse_code_voie",
        #         "code_postal","code_commune","nom_commune","code_departement",
        #         "ancien_code_commune","ancien_nom_commune","id_parcelle",
        #         "ancien_id_parcelle","numero_volume",
        #         "lot1_numero","lot1_surface_carrez",
        #         "lot2_numero","lot2_surface_carrez",
        #         "lot3_numero","lot3_surface_carrez",
        #         "lot4_numero","lot4_surface_carrez",
        #         "lot5_numero","lot5_surface_carrez",
        #         "nombre_lots","code_type_local","type_local",
        #         "surface_reelle_bati","nombre_pieces_principales",
        #         "code_nature_culture","nature_culture","code_nature_culture_speciale",
        #         "nature_culture_speciale","surface_terrain","longitude","latitude"]

        # return ["date_mutation","numero_disposition",
        #             "nature_mutation","valeur_fonciere","adresse_numero",
        #             "adresse_suffixe","adresse_nom_voie","adresse_code_voie",
        #             "code_postal","code_commune","nom_commune","code_departement",
        #             "ancien_code_commune","ancien_nom_commune",
        #             "nombre_lots","code_type_local",
        #             "surface_reelle_bati","nombre_pieces_principales",
        #             "code_nature_culture","nature_culture"
        #             ,"surface_terrain","longitude","latitude"]

        return [{"name":"date_mutation","type":"string"},
                {"name":"numero_disposition","type":"int"},
                {"name":"nature_mutation","type":"string"},
                {"name":"valeur_fonciere","type":"string"},
                {"name":"adresse_numero","type":"string"},
                {"name":"adresse_suffixe","type":"string"},
                {"name": "adresse_nom_voie", "type": "string"},
                {"name": "adresse_code_voie", "type": "string"},
                {"name": "code_postal", "type": "string"},
                {"name": "nom_commune", "type": "string"},
                {"name": "code_departement", "type": "int"},
                {"name": "nombre_lots", "type": "int"},
                {"name": "code_type_local", "type": "int"},
                {"name": "surface_reelle_bati", "type": "int"},
                {"name": "nombre_pieces_principales", "type": "int"},
                {"name": "nature_culture", "type": "string"},
                {"name": "surface_terrain", "type": "int"},
                {"name": "longitude", "type": "double"},
                {"name": "latitude", "type": "double"}]


    def __init__(self):
        self.TableName = "hw_estimate_model_2"
        super().__init__()

    # def setValues(self,row):
    #     self.row = row
