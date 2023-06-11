# NaiveBayesWeb-CryotherapyDataset
Simple Web App about cancer level prediction based on post condition after cryotherapy treatment. Using dataset of Cryotherapy analysis

### Procedure to use the application
<ol>
  <li> If you dont have pip, install it first</li>
  https://pip.pypa.io/en/stable/installing/
  </br></br>
  <li> Install virtualenv</li>
  
    pip install virtualenv
    
  </br>
  <li> Create the env folder inside your project</li>
     
     virtualenv <env-name-folder>
     
  </br>
  <li> (Optional) Change the permission of the virtualenv in the windows operating system, by search PowerShell, run as administrator and write command     below</li>
  
      Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
      
  </br>
  <li>Activate the virtual environtment</li>
      
      <env-name-folder>/Scripts/activate
      
  </br>
  <li>Make sure you're in the virtual environtment by see the symbol ( < env-folder-name >)</li>
  </br>
  
  ![alt text](https://github.com/ifs20004-itdel/NaiveBayesWeb-CryotherapyDataset/assets/87352987/80489032-a5d5-47cc-9271-20b8daaf151e)
  
  </br>
  <li> Make sure the pip is up to date by upgrade it</li>
      
      python.exe -m pip install --upgrade pip
      
  </br>
  <li> Install all the library that needed</li>
      
      pip install scikit-learn
      pip install pandas
      pip install flask
      pip install pickle-mixin
      pip install pickleshare
      
   </br>
  <li> Run the application</li>
      
      flask run
</ol>
