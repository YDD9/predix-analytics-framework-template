
import os
import json

import sys
# print  os.getcwd()
# os.chdir(os.pardir)
sys.path.insert(0, os.path.join(os.getcwd(), "analytic"))
# print '\n'.join(sys.path)
from AnalyticsDemo import AnalyticsDemo


if __name__ == "__main__":
    # os.chdir(os.pardir)
    currentPath = os.getcwd()
    print currentPath

    filePath = os.path.join(currentPath, r"input\Analytics_input.json")
    with open(filePath, 'r') as f:
        data = json.load(f)
    print "inputs data:\n{}".format(json.dumps(data))
    model = AnalyticsDemo()
    rt = model.runAll(json.dumps(data))

    with open(r'output\output.json', 'w') as outfile:
        json.dump(rt, outfile)
    print'testrun finish.'