import json

import instaloader


def getProfile():
    namelists = ["kuohsingchun_official", "mitou_yu", "luxiaojunbarbell"]
    for item in namelists:
        L = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context, item)
        print(profile.username)
        print(profile.full_name)
        print(profile.business_category_name)
        print(profile.biography)



testObj = [
    {"key": "Product Specifications", "value": ""},
    {"key": "Bar type", "value": "Men's Training bar"},
    {"key": "Bar use", "value": "Weightlifting & Cross-training"},
    {"key": "Weight", "value": "20 KG"},
    {"key": "Diameter", "value": "28 MM"},
    {"key": "Length", "value": "220 CM"},
    {"key": "Knurl", "value": "Double"},
    {"key": "Center Knurl", "value": "Non"},
    {"key": "Shaft Coating", "value": "Hard Chrome/Black Chrome"},
    {"key": "Sleeve Coating", "value": "Sleeve Coating"},
    {"key": "Loading Capacity", "value": "680 kg/1500 LBS"},
    {"key": "Loadable sleeve length", "value": "415 MM"},
    {"key": "Bushing/Bearing", "value": "8 Bearings"},
    {"key": "Tensile Strength", "value": "200000 PSI"},
    {"key": "Warranty", "value": "2 Years"},
]

testJson = json.dumps(testObj)
print(testJson)
