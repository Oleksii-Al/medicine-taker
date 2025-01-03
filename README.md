# **Medication Assistant**

![Site preview](static/images/readme/preview.png)

Medication Assistant is a user-friendly web application designed to help users track their medication schedules effectively. With features like CRUD functionality, medication reminders, and weekly overview, this tool simplifies medication management for its users.

The responsive website allows registered users to add medication and create medication schedule. Users who are not registered are free to see the Home page. To make it easy to find right day in the schedule, users can reverse medication schedule and collapse unwanted days.

# **[Link to Live Site](https://medicine-taker-993fd18628d0.herokuapp.com/)**  

*This project was built as part of a full-stack development portfolio.*

**Built by Oleksii Aleferchuk**

---

# **Table of Contents**  

 1. [ UX ](#ux)
 2. [ Agile Development ](#agile-development)
 3. [ Features implemented ](#features-implemented)  
 4. [ Technology used ](#technology-stack) 
 5. [ Testing ](#testing)  
 6. [ Validation ](#validation)
 7. [ Deployment](#deployment)
 8. [ Resources ](#resources)  
 9. [ Credits and acknowledgements ](#credits-and-acknowledgements)

---

# **UX**

## Entity Relationship Model

I used smartdraw.com to create my database entity relationship diagrams. See diagram and supporting text below.

![Database Entity Relationship Medication Assistant Diagram](static/images/readme/erd.jpg)

## UX Design

## **Overview**
Medication Assitant is created for users who need to take medications and want to remeber about all of them. The app simplifies tracking medication, ensuring simplicity and confidentiality.

### Users
Medication Assistant is aimed at individuals who need to manage their medication schedules, including people with chronic conditions, elderly users, and those on multiple medications. These users seek a straightforward, reliable platform to track their medications, ensure timely intake, and maintain consistency in their treatment plans.

### Goal
Medication Assistant helps users stay on top of their medication by offering a customizable platform to track doses, times, and status (taken or not taken). The goal is to provide a simple yet effective tool that promotes organization, adherence to prescribed schedules, and peace of mind for users managing their health.

## Wireframes

The following wireframes illustrate the design and functionality envisioned for key pages and views in the application. Each layout ensures a responsive and user-friendly experience across various devices, including mobile.

### Home Page

The home page serves as the about page where user can find the purpose of the site and the implemented features. It includes clear description of the site and call to action button that redirects to Register page.

![Home Page Placeholder](static/images/readme/home.jpg)

---

### Medication List

The Medication List page provides schedule for taking medication depending on the detail that users provide. It ensures clear and organized presentation of data.

![Medication List Placeholder](static/images/readme/schedule.jpg)

---

### Forms

The wireframes for the forms include layouts for creating or editing medications. These forms prioritize simplicity and clarity for user input.

A confirmation message appears on the index page after actions like adding or editing spaces. This feedback ensures users are informed about the success of their actions.

![Add Medication Form Placeholder](static/images/readme/add.jpg)


---

# **Agile Development**

For the development of Medication Assistant, I adopted an Agile methodology to ensure iterative and efficient progress throughout the project lifecycle. Central to this approach was the utilization of a Kanban board hosted on GitHub Projects. You can view the project board [here](https://github.com/users/Oleksii-Al/projects/4/views/1).

## Kanban Board Overview

The Kanban board served as a visual representation of the project's progress and allowed for effective task management. It consisted of the following sections:

- **Backlog:** This section contained all the tasks and user stories that were yet to be prioritized for implementation.
- **Todo:** Tasks and user stories ready for development were moved to this column.
- **In Progress:** Work in progress was tracked here, indicating tasks actively being worked on.
- **Testing:** Upon completion, tasks were moved here for testing before being marked as done.
- **Done:** Tasks that were completed successfully were moved to this column.

### User Stories Integration

User stories played a pivotal role in shaping the development process, ensuring that features were aligned with user needs. These user stories were mapped onto the Kanban board, guiding the prioritization and implementation of tasks. 

### Task Management

In addition to tracking user stories, the Kanban board served as a comprehensive task list. I utilized it to break down user stories into smaller, actionable tasks, ensuring clear and manageable objectives for development. This granular approach facilitated efficient progress tracking and enhanced team collaboration.

By leveraging Agile principles and utilizing the Kanban board effectively, the development of Medication Assistant remained focused, adaptable, and responsive to evolving requirements, resulting in a more robust and user-centric Django blog application.


## User Stories Overview

1. **Title:** Registration
   - As a user, I want to register an account so that I can securely save and access my medication schedules.

2. **Title:** Login
   - As a user, I want to log in to my account so that I can access my personalized medication data.

3. **Title:** Logout
   - As a user, I want to log out of my account so that my data remains secure when I’m done using the site.

4. **Title:** Add Medication
   - As a user, I want to easily create a new medication card so that I can track my medication schedule efficiently.

5. **Title:** Take/Untake medication
   - As a user, I want to mark medication as taken/untaken so that I can manage my daily doses efficiently.

6. **Title:** Edit medication
   - As a user, I want to edit medication cards so that I can keep my medication schedule up to date.

7. **Title:** Delete medication
   - As a user, I want to delete medication cards so that I can keep my medication schedule up to date.

8. **Title:** Medication List
   - As a user, I want to see my medication cards displayed by days of the week (Monday to Sunday) so that I can easily navigate my medication schedule for the entire week.

9. **Title:** Revers days order
   - As a user, I want to reverse the week so that I can quickly find the information I need.

10. **Title:** Collapsing/expanding the medication day
   - As a user, I want to collapse the days of the week so that I can focus on specific days or manage my schedule with more space.

11. **Title:** Home page for unauthenticated users
   - As a user, I want to see a homepage with general information about the site so that I understand its features and how to use them.

12. **Title:** Navigation
   - As a user, I want to easily navigate through the site so that I can quickly access all the features and information I need.

13. **Title:** Alert messages
   - As a user, I want to receive feedback through alert messages so that I know when my actions are successful or if there are any issues.

# **Features Implemented**

## Home page:
  - General information is displayed
  - Call to action button is displayed and redirects to Register page
  - Register button is displayed
  - Login button is displayed

## Medication List page:
  - The days of the week are rendered
  - Correct medication is displayed in each day
  - Order button can reverse the days
  - Each day can be collapsed/expanded

## Actions:
  - Take button is displayed next to every medication
  - Edit button is displayed next to every medication
  - Delete button is displayed next to every medication
  - Each button has a correct link
  - ALert message is displayed after every action with success or error result

## Delete modal:
  - Delete button call the Delete modal
  - User need to confirm deletion in the modal

## Add Medication form
   - Crispy form is rendered
   - Necessary fields is displayed
   - Filled fields allow medication to be correctly displayed on the Medication List 

## Login Page:
  - Secure signup functionality allows users to register securely.
  - Successful login redirects users to the Medication List page.

## Registration Page:
  - Secure login functionality allows users to log in securely.
  - Successful registration redirects users to the Medication List page.

## Logout Page:
  - Logout functionality allows users to sign out securely.
  - After successful logout, users are redirected to the Home page.

### Responsive Design:

   - The website is designed to be responsive, ensuring optimal usability across various screen sizes.
   - Navbar collapses into a burger bar for improved navigation on smaller screens.
   - The medication card is changed for smaller screen to provide better readability

# **Technology Stack**

- HTML - for page structure
- CSS - for custom styling
- Python - for the backend
- Javascript - for filtering and deliting functionality
- Django - framework used to build this project
- Bootstrap 5 - front end framework used for styling
- Heroku PostgreSQL - used as the database
- Balsamiq - for wireframes
- Font Awesome - for social media icons
- Smartdraw - for database ER diagrams
- GitHub - for storing the code and for the Kanban board
- Heroku - for hosting and deployement of this project
- Git - for version control

## Responsiveness

The app was tested across multiple devices (desktop, tablet, mobile) using Chrome DevTools.

### The Home page

| ![Home Page Desktop](static/images/readme/home_d.jpg) | ![Home Page Mobile](static/images/readme/home_m.jpg)

### The Medication List page

| ![Medication List Page Desktop](static/images/readme/sch_desk.jpg) | ![Medication List Page Mobile](static/images/readme/sch_mob.jpg)

### The Add/Edit Medication page

| ![Add Medication Page Desktop](static/images/readme/add_d.jpg) | ![Add Medication Page Mobile](static/images/readme/add_m.jpg)
| ![Edit Medication Page Desktop](static/images/readme/edit_d.jpg) | ![Edit Medication Page Mobile](static/images/readme/edit_m.jpg)

# **Testing** 

### Manual Testing Results

### HOME PAGE

| Test                                             | Result |
|--------------------------------------------------|--------|
| Home page is displayed for unauthenticated user  | Pass |
| Home page isn't displayed for authenticated user | Pass |
| Call to action button redirects to Register page | Pass |
| All general information are displayed            | Pass |

### MEDICATION LIST PAGE

| Test                                             | Result |
|--------------------------------------------------|--------|
| List page isn't shown for unauthenticated user   | Pass |
| List page is displayed for authenticated user    | Pass |
| Days are displayed                               | Pass |
| Medication cards are displayed for correct days  | Pass |
| Day can be expanded/collapsed                    | Pass |
| Days can be reversed                             | Pass |
| Action buttons are displayed for each medication | Pass |

### FOOTER/NAV BAR

| Test                                    | Result |
|-----------------------------------------|--------|
| Navigation links functionality          | Pass |
| Footer is displayed                     | Pass |

### ADD MEDICATION PAGE

| Test                                    | Result |
|-----------------------------------------|--------|
| Access requires login                   | Pass   |
| Add form functionality                  | Pass   |
| Merdication creation functionality      | Pass   |
| Redirect after creation                 | Pass   |

### LOGIN PAGE

| Test                                   | Result |
|----------------------------------------|--------|
| Secure signup functionality            | Pass   |
| Redirect after successful login        | Pass   |

### REGISTRATION PAGE

| Test                                   | Result |
|----------------------------------------|--------|
| Secure login functionality             | Pass   |
| Redirect after successful registration | Pass   |

### LOGOUT PAGE

| Test                                   | Result |
|----------------------------------------|--------|
| Logout functionality                   | Pass   |
| Redirect after successful logout       | Pass   |

# **Validation**

- I used the W3 HTML Validator to check the HTML on each of my site pages by Direct Input. The result is following: "Document checking completed. No errors or warnings to show.".
![HTML Validation](static/images/readme/html_v.jpg)

- I used the W3 CSS Validator to check my CSS script by Direct Input. The result is following: "Congratulations! No Error Found."
![CSS Validation](static/images/readme/css_v.jpg)

### **WCAG Contrast Checker**
The site was tested using the [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) to ensure compliance with WCAG (Web Content Accessibility Guidelines).

- **General Results**:  
  The majority of the site achieved **high contrast ratings**, ensuring good readability and accessibility for users with visual impairments.

- **Exceptions Identified**:
  1. **Footer**:  
     Contrast ratio does not meet WCAG standards in this scenario.

     ![WCAG Contrast Footer](static/images/readme/contrast.jpg) 

### **PEP 8 Compliance**

- The code was validated using Code institute's **CI Python Linter** [CI Python Linter](https://pep8ci.herokuapp.com/).
- I found a 3 small errors: lines were too long.

![Python Linter Result](static/images/readme/linter.jpg)

# **Deployment** 

## Deployment Guide for the Medication Assistant Website

### Deployment Steps:

#### Creating the Heroku App

- Begin by signing up or logging in to Heroku.
- In the Heroku Dashboard, click on 'New' and then select 'Create New App'.
- Choose a unique name for your project, like "Travelling Scribbles".
- Select the EU region.
- Click on "Create App".
- In the "Deploy" tab, choose GitHub as the deployment method.
- Connect your GitHub account and find/connect your GitHub repository.

#### Setting Up Environment Variables

- Create `env.py` in the top level of the Django app.
- Import `os` in `env.py`.
- Set up necessary environment variables in `env.py`, including the secret key and database URL.
- Update `settings.py` to use environment variables for secret key and database.
- Configure environment variables in the Heroku "Settings" tab under "Config Vars".
- Migrate the models to the new database connection in the terminal.
- Configure static files and templates directories in `settings.py`.
- Add Heroku to the `ALLOWED_HOSTS` list.

#### Creating Procfile and Pushing Changes

- Create a `Procfile` in the top level directory.
- Add the command to run the project in the `Procfile`.
- Add, commit, and push the changes to GitHub.

#### Heroku Deployment

- In Heroku, navigate to the Deployment tab and deploy the branch manually.
- Monitor the build logs for any errors.
- Upon successful deployment, Heroku will display a link to the live site.
- Make sure to resolve any deployment errors by adjusting the code as necessary.

### Forking the Repository

Forking the GitHub Repository allows you to create a copy of the original repository without affecting it. Follow these steps:

- Log in to GitHub or create an account.
- Visit the [repository link](https://github.com/Oleksii-Al/medicine-taker).
- Click on "Fork" at the top of the repository.

### Creating a Clone of the Repository

Creating a clone enables you to make a local copy of the repository. Follow these steps:

- Navigate to the [Medical Assistant repository](https://github.com/Oleksii-Al/medicine-taker).
- Click on the <>Code button.
- Select the "HTTPS" option under the "Local" tab and copy the URL.
- Open your terminal and change the directory to your desired location.
- Use `git clone` followed by the copied repository URL.

# **Resources**

- [Code Institute Full Stack Development course materials](https://codeinstitute.net/) 
- [Django docs](https://www.djangoproject.com/)
- [Crispy forms docs](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Cloudinary docs](https://cloudinary.com/documentation/programmable_media_overview)
- [Bootstrap docs](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Code Institude Slack](https://slack.com/)
- [ChatGPT](https://chatgpt.com/)

# **Credits and Acknowledgements**
- **Code Institute** course content for providing the structured templates and guidance throughout the project
- GitHub user **katiejanecoughlan** and **jack-brosnan** for sharing a best practice README structure
- Course Facilitator **David Calikes** for his support and guidance during the course 
- Tutor **Kevin Loughrey** for his helpful SME sessions and expert advice
- ChatGpt for helping in debugging and understanding hard topics.