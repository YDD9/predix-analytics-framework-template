import os
import sys

# print  os.getcwd()
sys.path.insert(0, os.path.join(os.getcwd(), "analytic"))
# print '\n'.join(sys.path)
from AnalyticsDemo import AnalyticsDemo


if __name__ == "__main__":
    currentPath = os.getcwd()
    print currentPath

    model = AnalyticsDemo()

    # test with single int
    result = None
    dataList = 1
    signalNameList = 'A'
    timestampList = [1499287754000]
    constantsDict = {'apple': 500, 'orange':600}
    result = model.inputJsonGen(dataList, signalNameList, timestampList, constantsDict)

    print result
    assert result == {'data': {'time_series': {'A': [1], 'time_stamp': [1499287754000]}, 'constants': {'orange': 600, 'apple': 500}}}


    # test with single int
    result = None
    dataList = [1]
    signalNameList = ['A']
    timestampList = 1499287754000
    constantsDict = {'apple': 500, 'orange':600}
    result = model.inputJsonGen(dataList, signalNameList, timestampList, constantsDict)

    print result
    assert result == {'data': {'time_series': {'A': [1], 'time_stamp': [1499287754000]}, 'constants': {'orange': 600, 'apple': 500}}}


    # test with single int
    result = None
    dataList = 1
    signalNameList = list('A')
    timestampList = 1499287754000
    constantsDict = {'apple': 500, 'orange':600}
    result = model.inputJsonGen(dataList, signalNameList, timestampList, constantsDict)

    print result
    assert result == {'data': {'time_series': {'A': [1], 'time_stamp': [1499287754000]}, 'constants': {'orange': 600, 'apple': 500}}}


    # test with single int
    result = None
    dataList = [1]
    signalNameList = 'A'
    timestampList = [1499287754000]
    constantsDict = {'apple': 500, 'orange':600}
    result = model.inputJsonGen(dataList, signalNameList, timestampList, constantsDict)

    print result
    assert result == {'data': {'time_series': {'A': [1], 'time_stamp': [1499287754000]}, 'constants': {'orange': 600, 'apple': 500}}}


    # test with single int
    result = None
    dataList = [1,2,3,4]
    signalNameList = 'A'
    timestampList = [1499287754000, 1499287764000, 1499287774000, 1499287784000]
    constantsDict = {'apple': 500, 'orange':600}
    result = model.inputJsonGen(dataList, signalNameList, timestampList, constantsDict)

    print result
    assert result == {"data":{"time_series":{"A":[1,2,3,4],"time_stamp":[1499287754000,1499287764000,1499287774000,1499287784000]},"constants":{"orange":600,"apple":500}}}


    # test with list and omit constantsDict
    result = None
    dataList = [1,2,3,4]
    signalNameList = list('ABCD')
    timestampList = 1499287754000
    result = model.inputJsonGen(dataList, signalNameList, timestampList)

    print result
    assert result == {'data': {'time_series': {'A': [1], 'time_stamp': [1499287754000], 'C': [3], 'B': [2], 'D': [4]}, 'constants': {}}}


    # test with list and omit constantsDict
    result = None
    dataList = [[1,1],[2,2],[3,3],[4,4]]
    signalNameList = list('ABCD')
    timestampList = [1499287754000, 1499287764000]
    result = model.inputJsonGen(dataList, signalNameList, timestampList)

    print result
    assert result == {'data': {'time_series': {'A': [1, 1], 'time_stamp': [1499287754000, 1499287764000], 'C': [3, 3], 'B': [2, 2], 'D': [4, 4]}, 'constants': {}}}
