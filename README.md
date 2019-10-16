# A Getting-Started Example of Flask Web Framework
1. The simplest web application <br />
   Follow the steps to download and launch the simple application <br />
   - Open an Anaconda Prompt <br />
   - Install package 'flask', if necessary <br />
   - Make a folder, say 'project', and change to 'project' <br />
   - Download the python code 'main.py' and store it under folder 'project' <br />
     (You may create your own python code similar to 'main.py'.) <br />
   - Execute the command: <br />
     ```
     set FLASK_APP=main.py
     ```
   - Execute the command:
     ```
     flask run
     ```
   - Run the application by opening a browser to go to: <br />
     ```
     http://localhost:5000
     ```
1. A web application that loads database records and shows a word cloud of the specified text
   Procedure to create an environment for the application and launch this application: <br />
   - Download the folder 'App' and the file 'environment.yml' <br />
   - Launch an Anaconda command prompt <br />
   - Excute the following command: <br />
     ```
     conda env create -f environment.yml
     ```
     (This will create a virtual environment 'fenv', as stated at the first line of 'environment.yml', and you may change it. <br />
      It will also install the relevant Python packages for this web application.) <br />
   - Activate the virtual environment, fenv by running the command:
     ```
     activate fenv
     ```
     OR
     ```
     conda activate fenv
     ```
   - Go to folder 'App' and execute: <br />
     ```
     python flask_app.py
     ```
     (This will start up a Flask web server) <br />
   - Run the application by opening a browser to go to: <br />
     ```
     http://localhost:5000
     ```
