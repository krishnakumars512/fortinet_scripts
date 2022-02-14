# fortinet_scripts
fortinet_rule_import

This script can be used to convert the fortinet firewall policy into csv.

Usage:

1. Download the script.
2. Copy the config file to the same location of your script file.
3. run the command python <script.py> 
4. redirect the output to a csv file as below

Usage : python rule_export.py <file name as an argument> 
  If you want to redirect the output to a file then use "python rule_export.py <file name as an argument> >> out_file.csv

 Example : python rule_export.py vdom_config.conf >> vdom_config.csv
  
  You can use the other scripts as in the same way for extracting address objects,address object groups and ip pools.
