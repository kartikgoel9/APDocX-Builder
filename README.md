#  APDocxBuilder Complete Overview

> Making lab file can be very cumbersome and filling out the index manually can be tedious at times. so APDocxBuilder has brought a solution to this.
> APDocxBuilder, your friendly lab file builder

> you'll find deployed site to be having different UI, I had changed it later so my college students finds it somewhat attractive
and for that I have used someone else's HTML and CSS styling that's why i didn't push that code in this branch for avoiding plagiarism.

# How to Run:
* create a virtual environment by using this command :- python -m venv nameOfvirtualEnv
* activate it : source virtualEnvName/bin/activate
* run this command 'pip install -r requirements.txt'
* run 'python manage.py migrate'
* run 'python manage.py runserver'

> it is responsive as well for both mobile and laptops

# External Files:

* requirements.txt has all the required files to be downloaded in order to run this project

* runtime.txt file contains python version, it helps us to deploy it on Production Server

# djangoProject Directory:

* ### urls.py files contains two things:

   1. it has included DockMaker app urls path, so it can be accessible throughout the project on app level.
   2. urlspattern, it places here , so we can serve static files url.
  
* ### settings.py files:
   1. AUTH_USER_MODEL = "DocMaker.User", we are using django abstract User model for login and registration
   2. MEDIA_ROOT=os.path.join(BASE_DIR,'DocMaker/static/images') helps to store static files in the defined path
   3. allowedhost is like this, ALLOWED_HOSTS = ["*"] so, it can accept any host request

# DocMaker Directory:
  * ### templates/DockMaker/ contains our presentation layer(templates)
     1. addExperiment.html, for adding experiments.however, if you add experiment without adding any subjects, it will show you an warning message
     2. addSubject.html, for adding subjects
     3. layout.html, it is the base design that you can see on every page, so we created it seperately in order to reduce redundancy.
     4. login.html, login page only authenticated user will get access to the index page
     5. register.html, registration page for adding new user
     6. subjectselection, it helps us to select subject so we can make individual lab file for each subject with its corresponding experiments
     7. editexperiment, edits the existing experiment
     
  * ### models.py file contains 3 user-defined models:
    1. Subject, Experiment, UserCurrentSelectedSubjects, Subject model has one foreignkey 'User' .
    When a individual user get deleted , it's corresponding Subjects will also get deleted,
    I have also used Subject as a foreign key for experiments, because a subject can have many experiments and
    if a particular subjects get deleted, it's corresponding subject will also get deleted.
    UserCurrentSelectedSubjects is created in order to generate a word file, so we can get the information of which subject experiments to be created in a file.
    
    2. I have also defined properties for getting url of static files, so I can serve the user with a download option.
    
    3. abstract user model which we are using for login and register, I have defined here
    
    
   * ### In admin.py file, I've registered all models in order to see its tables on admin console
   
   * ### In forms.py , several forms have been defined to do a designated task, which it is getting 
         in templates.(addSuject,addEpxeriment,editExperiment forms)
   
   * ### urls.py contains urlpatterns for views:
     1. login/
     2. register/
     3. subjectselection/
     4. addsubject/
     5. addexperiments/
     6. template/
     7. edit/<int:id>
     
   * ### views.py contains function that will get triggered for every url path defined
     1. index() takes a request and render a view according to authentication 
     if a user is authenticated then he/she only can access to other pages otherwise,
     they'll have to login themselves in order to access any page due to @login_decorator if an suer tries to access any page with its path it'll
     redirected to login page itself.
     
     2. I have also passed experiment objects to index page via dictionary so when user clicks on show experiments , 
     he/she can see all experiments , if is there any, otherwise the button will appear showing 'you don't have any experiment'
     and I'm handling the show experiment section using javascript dom manipulation.
     
     3. **editExperiment()** takes a request and an id to find the specific experiment with its id and prefilled the form with
     data inside that experiment object
     
     4. **addSubject()**, this function takes a request and simply add a new subject in subjects table
     
     
     *  **templateCreation()** uses several libraries in order to get its job done.
        So the second complex thing was to me figuring it out how to dynamically generate my index page without hurting its 
        style formatting, when i was working with python-docx library several things was not working properly.
        **DocMaker/static/docfiles/Template_4.docx** this is where the template resides, I'm using this file to build a complete lab file.
        when you will open this file, you get to see jinja2 syntax inside a word file under a for loop.
        In that for loop, the way, I used to send values across django templates, I have sent values to this word file and rendered its content.
        the third problem had come when i tried to generate a file with 'C language syntax' 
        so django get confused between jinja2 syntax and C, for this I have used autoescape=True
        and saving every file with a username.docx, so name collision won't take place.
     
     *   for the file to be downloaded, I have used FilePointer and reading it as a binary and
         passing it on to response object and setting
         content-type for word document and then deleting it 
         from the directory,for storage efficiency.

     5. **addExperiments()**, here we are first taking subject objects and filtering it
     with the request.user which gives me the 'only current user added subjects' and 
     then pass it on to template and giving an user option to select a subect from its own created subjects.
     and the complexity for me had come when i was finding a way to do it via models, but I didn't succeed in doing that. 
     so i realized about HTML and pass that value to template and wrap that particular 
     <select> tag in a for loop and run it for object size times.
   
   

  
   
     
     
     
   

   



   
 

     
     
     


