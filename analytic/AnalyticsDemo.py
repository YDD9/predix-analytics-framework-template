from __future__ import division
import numpy as np
import json
from datetime import datetime

class AnalyticsDemo():
    def __init__(self):
        ## output
        self.time_stamp = 0

    def inputJsonGen(self, dataList, signalNameList, timestampList, constantsDict={}):
        """
        Generate Analytics input format json with args of
        dataList, signalNameList, timestampList millisecond, [constantsDict]
        The number of data points for each signal should be the same and it
        should be equal to the number of timestamps
        """
        result = {
                    "data": {
                        "time_series": {
                            "time_stamp": []
                        },
                        "constants": constantsDict
                    }
                    }
        # if isinstance(dataList, (int, float)):
        #     pass
        dataList = np.asarray(dataList)
        signalNameList = np.asarray(signalNameList)

        if isinstance(timestampList, list):
            result['data']['time_series']['time_stamp'] = timestampList
        elif isinstance(timestampList, long):
            result['data']['time_series']['time_stamp'] = [timestampList]
        else:
            raise ValueError ('{} is not epochtime[ms] nor a list of epochtime[ms]'.format(timestampList)) 

        # multi signals
        if signalNameList.size is not 1:
            for i in range(signalNameList.size):
                # value as a single number
                if dataList.shape[0] == dataList.size:
                    if len(result['data']['time_series']['time_stamp']) is not 1:
                        raise Exception ('number of data points for each signal and number of timestamps are not identical')
                    result['data']['time_series'][signalNameList.item(i)] = [dataList.item(i)]
                # value as a list
                else:
                    if len(result['data']['time_series']['time_stamp']) != dataList.shape[1]:
                        raise Exception ('number of data points for each signal and number of timestamps are not identical')
                    result['data']['time_series'][signalNameList.item(i)] = dataList[i].tolist()
        # single signal
        else:
            # values as a list
            if dataList.size is not 1:
                if len(result['data']['time_series']['time_stamp']) != dataList.size:
                    raise Exception ('number of data points for each signal and number of timestamps are not identical')
                result['data']['time_series'][signalNameList.item(0)] = dataList.tolist()
            # value as a single number
            else:
                if len(result['data']['time_series']['time_stamp']) is not 1:
                    raise Exception ('number of data points for each signal and number of timestamps are not identical')
                result['data']['time_series'][signalNameList.item(0)] = [dataList.item(0)]

        return result


    def formatOutput(self, signallist, valuelist):
        """
        Convert output to Predix Analytics output json format
        """
        output = json.loads('{"data":{"time_series":{} } }')
        output['data']['time_series']['time_stamp'] = self.time_stamp
        N = len(signallist)
        assert  N == len(valuelist)
        for i in range(N):
            output['data']['time_series'][signallist[i]] = valuelist[i]

        return output

    def AnalyticsDemoCalc(self, jsondataInput):
        """
        AnalyticsDemo calculate Revenue:
        Input has data of previous hour and current hour !!!
        Input json can not contain null !!!
        """

        # ***********************************************************************
        # *                                                                     *
        # *---------------------------------------------------------------------*
        # *                                                                     *
        # *  Input Constants                                                    *
        # *  ----------------                                                   *
        # *  ABC:   model constant one  2.8[m]                                  *
        # *  XYZ:   model constant two  [1, 2, 3][s]                            *
        # *                                                                     *
        # *                                                                     *
        # *  Input Timeseries                                                   *
        # *                                                                     *
        # *  Signal_ONE:    Power comsuption    [kW]                            *
        # *  Signal_TWO:    Power generation    [kW]                            *
        # *  Signal_THREE:  Power price         [kW h/ Dollar]                            *
        # *                                                                     *
        # *---------------------------------------------------------------------*
        # *                                                                     *
        # *  Output parameter                                                   *
        # *  ----------------                                                   *
        # *  Output_A:  Efficiency raw  [-]                                     *
        # *  Output_B:  Revenue         [Dollar]                                *
        # *                                                                     *
        # *---------------------------------------------------------------------*
        # *                                                                     *
        # *  Reference                                                          *
        # *  ---------                                                          *
        # *                                                                     *
        # *                                                                     *
        # *---------------------------------------------------------------------*
        # *                                                                     *
        # *  General                                                            *
        # *  ----------------                                                   *
        # *  programming language :  Python                                     *
        # *  created by           :  YDD9                                       *
        # *  date of creation     :  01.01.2017                                 *
        # *                                                                     *
        # *  modified by          :  YDD9                                       *
        # *  date of modification :  29.06.2017                                 *
        # *                                                                     *
        # *  date       modification                                            *
        # *  ----       ------------                                            *
        # *                                                                     *
        # *                                                                     *
        # *                                                                     *
        # ***********************************************************************

        # input timestamp
        self.time_stamp = jsondataInput['data']['time_series']['time_stamp']

        # inputs constants
        ABC = jsondataInput['data']['constants']['ABC']
        XYZ = jsondataInput['data']['constants']['XYZ']

        # inputs timeseries list of 2
        Signal_ONE = jsondataInput['data']['time_series']['Signal_ONE']
        Signal_TWO = filter(None, jsondataInput['data']['time_series']['Signal_TWO'])
        Signal_THREE = jsondataInput['data']['time_series']["Signal_THREE"]


        # calculations
        Output_A = np.divide(Signal_ONE, Signal_TWO).tolist()
        Output_B = np.multiply(np.add(Signal_ONE, Signal_TWO), Signal_THREE).tolist()

        # output names and values
        output_signallist = ["Output_A", "Output_B"]
        output_valuelist = [Output_A, Output_B]

        return self.formatOutput(output_signallist, output_valuelist)

    def runAll(self, jsondataInput):
        print 'start run all:'
        data_json = json.loads(jsondataInput)
        result = self.AnalyticsDemoCalc(data_json)
        print 'AnalyticsDemo Analysis finishes!'

        return result
