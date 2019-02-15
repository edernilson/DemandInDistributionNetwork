![Icone](/assets/icon.png "Icone")
# Demand in Distribution Network
QGIS 2.8 or higher processing provider plugin that calculates demand on distribution network nodes.

Algorithm for calculating demand in nodes (hub):
---- 
Estimate the demand at the nodes (hubs), based on household consumption. The calculation is performed by adding the demand in the households, and designating the total demand in the nodes of the distribution network. This processing plugin is based on the component **"Distance to nearest hub"**.

Authors:
----
* Eder Nilson <[eder.nilson@gmail.com](mailto:eder.nilson@gmail.com)>
* Julian Cardona <[juliancardona77@gmail.com](mailto:juliancardona77@gmail.com)>

### Operation: 
Given a layer of origin (households) and another layer representing destination points (nodes), the algorithm calculates the distance between each point of origin (households) and the nearest point of detention (Nodes). households, and totaling the demand value that will be assigned to the nearest node (hub). In addition, the algorithm displays a "line" layer, created by the **"Distance to nearest hub"** component, which identifies households (origin) and Nodes (destination), allowing easy verification of geoprocessing connectivity.

### Where to find the algorithm:
Once installed and active, this plugin adds the new provider (Algorithms to designate demands on nodes in the distribution network) in the **Processing Toolbox**. 
You find the algorithm in the Toolbox under Algorithms to designate demands on the nodes in the distribution network -> Algorithms -> Calculate the Demand Flow in the Nodes.

![Processing Toolbox](/assets/tools.png "Processing Toolbox")

Config and Result:
![Config and Result](/assets/result.png "Config and Result")
