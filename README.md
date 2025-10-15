# Shark_CNC_CPS_for_Fusion360_-CL_-EXE
This project encompases years of frustration watching coworkers wage a fight (of their own making) on multiple Shark CNC from Next Wave. Due availability issues of who a has a post processor, they have had no choice but to use Vcarve for all of their needs. This project aims to offer options through Fusion360, command line, and drag and drop EXE. 

# Why this matters
Within the framework of Fusion360 CPS provide a framework that is referenced when sttting up a cut pattern. 
Then serve to FILTER or CONVERT code that has been output by the application. 
Lastly they insert additional information as needed by a particulat vendor. 
Mine inject a header, startup and shutdown. 
Given my familiarity with several FDM software interface I have also injected the ability for a user to insert their own startup and shutdown code as needed.
It is important to note that not everything listed has been added to this project yet. 

# Two Branches
The line of machines seems to have diverged into two distict developments 
This means I will inevitably designate two CPS. 
It is possible I will be able to simply add a switch.
Never the less some functions conflict so this CPS cannot be everything all at once. 
Since the code is being done on AI, development is vastly accelerated. But code will be less compressed and include less clever compression, at least for now. 

# Drag and Drop
I know this isnt how post processor normaly works. But what can I say, the 3D printing market has effected everything, including CNC which is why they even exist on a small scale today. Many tools in the FDM market are drag and drop, some just work and others have more robust configurations. I dont think this needs to be more than generic conversions and filters.

# Command Line
This is a thought that a user can open the function as a terminal within VCS. 
From here the they have a limited interface and edditor abilities. 

# Fusion360 CPS
This is the default on the list. A standard CPS that can be saved and used with Fusion360 as needed. 
Already I have successfull and functioning CPS for MARLIN based CNC, though more limited than I would like they do the job needed. 

#Open Source
It is until it cannot.
I welcome public interaction. If you have a machine to test with and help with development. Welcome.
