# A getting-started example of Flask web framework
Procedure of building an environment and running the application: <br />
- Download the folder 'App' and the file 'environment.yml' <br />
- Launch an Anaconda command prompt <br />
- Excute the following command: <br />
  ```
  conda env create -f environment.yml
  ```
  (This will create a virtual environment 'fenv', as stated at the first line of 'environment.yml', and you may change it. <br />
   It will also install the relevant Python packages for this web application.) <br />
- Go to folder 'App' and execute: <br />
  ```
  python flask_app.py
  ```
  (This will start up a Flask web server) <br />
- Run the application by opening a browser to browse: <br />
  ```
  http://localhost:5000
  ```
