# AnalyticsDemo Analysis 

A python-based  analytic for Predix-Analytic-Framework.
Further Orchestration can be done with this analytics: Input from Predix Timeseries, scheduler run.

## Compiled binaries
Refer to the [Releases](https://github.com/PredixDev/predix-analytics-sample/releases) page for compiled binaries you can upload directly to Predix Analytics.  

## Pre-requisites
To run this analytic locally, you will need to have the following:  
- Python 2.7+  
- numpy  

## Building, deploying and running the analytic  
1. Zip the contents of this directory.  
2. Create an analytic in Analytics Catalog with the name "{{analytic name}}" and the version "{{version number}}".  
3. Upload the zip file and attach it to the created analytic.  
4. Deploy and test the analytic on Predix Analytics platform.  

## Analytic template
This analytic takes timeseries and constants and returns timeseries.   
(Step for Orchestration only)Upload this json file into Analytics Catalog as template together with your Analytics executable.  

|Signal |Description|from Module|Input Output|Unit|
|-----------------------|-----------------------|---------|--------|--------------|
|h_H2O|Evaporation enthalpy of water||Constants|MJ/kg|



## Input format
The expected JSON input data format is shown in following file:  
Analytics_input.json.

## Output format
The JSON output format from the analytic is shown in following file:  
output.json

## Developing a Python-based analytic
1. Implement the analytic (and test functions) according to your development guidelines.
2. Create an entry method in your analytic class. The entry method signature must be in one of the following two formats:
 * For analytics that do not use trained models, use the following signature for your entry method:
  `def entry_method(self, inputJson):`
 * For analytics that use trained models, use the following signature for your entry method:
  `def entry_method(self, inputJson, inputModels):`
 * In either case, the `entry_method` can be any method name. `inputJson` is the JSON string input that will be passed to the analytic. The output of this method must also be a JSON string.
 * `inputModels` contains a dict() of trained models as defined in the port-to-field map. The entry method should properly handle the case of an empty dict.
3. Create a config.json file in the top level of the project directory. Specify the entry method in the format of `<subdirectory>.<className>.<methodName>`, conda-libs, and non-conda-libs.
4. Package all the analytic files and the config.json file into a ZIP file.

For more information, see [Python Analytic Development](https://www.predix.io/docs#alaepr9P) in the Predix Analytics Services documentation on Predix IO.
