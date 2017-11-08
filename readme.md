Purpose:

Configuration in the format:

Row 1: Label of field
Row 2: Type of field
Row 3: Liquid script looping through field values ex: {{loop_atom.field_name}}

within an .xlsx file is required as configuraiton in order to get the Onit app builder tool to generate a spreadsheet of the data within in app from the Mongo DB. The summary tab of app builder provides information formated "field_name : field_type" and this information can be used to generated the configuration described above. The input of this application is a .txt file selected by the user which is simply a copy of the text from the summary page of the app builder. 

Installation Instructions:

1) Make sure you have Python 2.7 installed
2) Run | git clone https://github.com/hackzor12/DeveloperTools.git 
2) Run | pip install Py2App
3) Navigate to the project directory
4) Run | python setup.py py2app

This should create a dist folder with an executable application that you can use and share.
