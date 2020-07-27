#Importing package from Package
from Packages import some_main_script
#Importing package from MySubPackage
from Packages.MySubPackage import mysubscript

#Calling function defined in the Package
some_main_script.report_main()

#Calling function defined in the MySubPackage
mysubscript.sub_report()