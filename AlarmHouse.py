# -*- coding: utf8 -*-
from HwModels.AnnonceModel import AnnonceModel
from HwModels.AlarmModel import AlarmModel
from HwHelper.HwTool import HwTool
if __name__ == '__main__':
    annonceModel = AnnonceModel()
    data = annonceModel.getAllCountsByStatus()
    print(data)

    tool = HwTool()
    # print(tool.getDay())
    alarmModel = AlarmModel()
    alarm = alarmModel.findAlarmByDate(tool.getDay())
    print(alarmModel.toArray(alarm))
    if alarm:
        # upadte
        pass
    else:
        # insert one
        pass


    pass