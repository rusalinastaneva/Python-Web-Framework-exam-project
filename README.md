## Welcome to my Django exam project!

<a href="https://softuni.bg/trainings/resources/officedocument/29648/team-exercise-problem-descriptions-software-technologies-march-2018" rel="GitandGitHub-Teamwork">  ![SoftUni logo][logo] <a/>

[logo]: http://innovationstarterbox.bg/wp-content/uploads/2016/05/Softuni_logo_trasparent.png "Logo Title Text 2"


<br/>

## HomePlace web listing platform for real estates



### Table of Contents

1. [INTRODUCTION](#introduction)
2. [PROJECT FUNCTIONALITY](#project-functionality)
3. [HOW TO RUN THIS PROJECT?](#run-project)


#### 1. <a name="introduction"></a> INTRODUCTION
The project is a **Django**-powered **web listing platform** designed specifically for the **real estate** crowd and **focused on** being a marketplace **for buyers and sellers** of real estate. 
It's a platform that **allows property owners to post** real estate listings for sale or lease **for FREE**.

![homepage][index]
[index]:  static/img/home.png

#### 2. <a name="project-functionality"></a>PROJECT FUNCTIONALITY

- Manage listings - authenticated users can create, edit and delete listings for sale/ lease of their created content.
- Unauthenticated users have access only to view the featured listings.
- Search and filter listings by keywords, city, state, bedrooms, home type, status and price (on Home & Search page) accessible by all users (unauthenticated & authenticated).
- Forms (for register/login)
- Admin panel (accessible by admins only). 
- Admin/s has full access for all content - manage website users, listings and team members.
- Admin/s can set the listings to unpublished via admin panel.

#### 3. <a name="run-project"></a>HOW TO RUN THIS PROJECT?

1. Clone the project by running the command `clone`:

```
git clone (repository_name)
```
2. Create a virtual environment by executing the command `venv`: 
(Ref: https://docs.python.org/3/library/venv.html)

```
python -m venv ./venv
```
3. Activate your virtual environment by running command:

```
On windows: cd venv\Scripts\activate 
Linux/ Mac: source /bin/activate.
```

4. Install all the dependencies by running the command below. (If you face any problem, install them manually).

```
pip install -r requirements.txt
```
5. Run an emulated server on your local computer by running the command `runserver`:

```
python manage.py runserver
```
6. Go to any internet browser and enter [localhost:8000](http://localhost:8000) or [127.0.0.1:8000](http://127.0.0.1:8000).
7. Great, you're done! :smiley:
