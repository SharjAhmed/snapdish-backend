# SnapDish - Backend

(Developer: Sharj Ahmed)

![Screenshot of Am I Responsive](/assets/readme/images/amiresponsive.png)

SnapDish is an Instagram-esque picture sharing social media site for users to share their food snaps. Users can share recipes or simply just post photos of their favourite snacks.

Users are able to sign up/sign in, create a post, like and comment another user's post and edit their profile username or picture.

This repository is the frontend of Snapdish which uses HTML, CSS, JavaScript, React & React Bootstrap.

## Deployed Link

- [SnapDish Backend Deployed Link](https://snapdish-backend-eb95a816e88d.herokuapp.com/)

## Frontend Links

- [SnapDish Frontend Deployed Link](https://snapdish-frontend-57cabaa4da7e.herokuapp.com/)
- [SnapDish Frontend GitHub Link](https://github.com/SharjAhmed/snapdish-frontend)

## Table of Contents

- [User Experience (UX)](#user-experience--ux-)
  - [Project Goals](#project-goals)
  - [User Stories](#user-stories)
  - [Kanban Board](#kanban-board)
  - [Design](#design)
  - [Wireframes](#wireframes)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
  - [Languages and Packages/Libraries Used](#languages-and-packages-libraries-used)
  - [Programs Used](#programs-used)
- [Testing](#testing)
  - [Validation Testing](#validation-testing)
  - [Manual Testing](#manual-testing)
  - [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Code](#code)
  - [Acknowledgements](#acknowledgements)

## User Experience (UX)

### Project Goals

- User Goals

  - Sign into my account or sign up for an account if I don't already have one.
  - Post images of my favoruite food.
  - Edit my posts.
  - View and edit my profile.
  - View other user's posts.
  - Like and comment on other user's posts.
  - Sign out of my account.

- Site Owner Goals

  - Allow the user to be able to sign in to their account or sign up and create an account if not already registered.
  - Allow users to create a new post and edit an existing post.
  - Allow users to follow other user's profiles and view their posts.
  - Allow users to like and comment on other user's posts.
  - Allow users to sign out of their account.

### User Stories

- Authentication
    1. As a user I cannot edit/delete posts/comments/likes that are not mine so that I can be assured that my posts/comments/likes are protected and can only be changed by me.
        - This user story is achieved by creating custom permissions that will stop users from deleting, editing, unliking/liking posts/comments that are not done by themselves.
    2. As a user I can see whether I am logged in or not so that I will know if I will need to log in if I am not.
        - This user story is achieved by showing the username created in profile after the user signs up and logs in using Django's all-auth.
    3. As a user I can sign up easily with just a username and password so that I have the ability to create posts or comments without having to share my email address.
        - This user story is achieved by using Django's all-auth.
    4. As a user I can easily log out so that I can have more security on my account.
        - This user story is achieved by using Django's all-auth.
    5. As a user I can easily log in so that I can quickly post, add more comments, or delete content if I wish.
        - This user story is achieved by using Django's all-auth.    
    6. As a user I can only like/unlike other users' posts.
        - This user story is achieved by creating the Post Likes models to like other user's posts. Custom permissions are created to allow users to only like other users' posts.
    7. As a user I cannot follow my own account so that my account reflects correctly when displaying follower counts.
        - This user story is achieved by creating the Follower model to follow other users. A custom permission is created to stop users from following themselves.

- Posts
    1. As a user I can create new posts so that I can share images.
        - This user story is achieved by creating the Post model. Users can add images, content, and a title to posts.
    2. As a user I can edit posts so that I can change my posts, whenever I change my mind about what I posted or wish to remove/change any details.
        - This user story is achieved by using generics.RetrieveUpdateDestroyAPIView in Post views. Users are able to edit their posts. 
    3. As a user I can delete my posts so that I can get rid of my posts that I no longer want to share.
        - This user story is achieved by using generics.RetrieveUpdateDestroyAPIView in Post views. Users are able to delete their posts. 
    4. As a user I can view the details of a post so that I can read more information about the post such as when it was created, who created it and any comments that are on the post.
        - This user story is achieved by using generics.RetrieveUpdateDestroyAPIView in Post views. Users are able to see the detailed information about a post such as who created it, when it was created/edited, if there are comments, etc. 
    5. As a user I can like posts so that I can share my appreciation.
        - This user story is achieved using the Post Likes model. Users are able to like to user posts.
    6. As a user I can remove likes on a post so that I can change my mind about whether I like the post or not.
        - This user story is achieved using generics.RetrieveDestroyAPIView in Post likes views. Users are able to remove their likes on a post.

- Comments
    1. As a user I can comment on a post so that I can share my thoughts about the post.
        - This user story is achieved using the Comment model. Users are able to add comments on posts
    2. As a user I can delete my comments on a post so that I can remove comments if I no longer want my comments to be public.
        - This user story is achieved using generics.RetrieveUpdateDestroyAPIView in Comment views. Users are able to delete their comments. 
    3. As a user I can read comments on a post so that I can see what other users think.
        - This user story is achieved using generics.ListCreateAPIView in Comment views. Users are able to read the list of comments on a post.
    4. As a user I can edit my comments so that can change what my comment says.
        - This user story is achieved using generics.RetrieveUpdateDestroyAPIView in Comment views. Users are able to edit their comments. 

- Profile
    1. As a user I can follow or unfollow other users so that I can see or choose to remove posts by specific users in my posts feed.
        - This user story is achieved using the Follower model. Users are able to follow and unfollow other users. 
    2. As a user I can view a detailed profile page of other users so that I can see their posts and follower/following information.
        - This user story is achieved using the Profile views. Users are able to see posts tied to a user, including their following count and followers count.
    3. As a user I can view other user's avatars so that I can easily identify them.
        - This user story is achieved by the Profile model, allowing users to view profile images/avatars of other users. 

- Errors
    1. As a user I can view a nice 500 page in the API so that I can be informed whether the server or database is having an issue on a nice, user-friendly interface.
        - This user story is achieved by creating custom views to throw a 500 page in a readable format when the server or database is having an issue.
    2. As a user I can see a nice 404 page in the API so that I know if I have reached a webpage that does not exist on a more user-friendly interface.
        - This user story is achieved by creating custom views to throw a 404 page in a readable format when a link or page does not exist. 

- Searching
    1. As a user I can search for posts or users by typing in text in the search bar so that I can easily find posts or users with a few keyboard taps.
        - This user story is achieved in Post views where custom filterset fields, search fields, and ordering fields are implemented to allow users to search for posts based on content, title, and owner.

- Filtering
    1. As a user I can easily filter information based on different circumstances so that I can easily find information via a simple filtering method such as who is following who, what posts a user liked, etc.
        - This user story is achieved by creating custom filterset fields in Post views, Comment views, Profile views, etc. However, users will not be able to see who is following who, they can see how many followers a user has or how many they are following.

### Database Model

![Database Model](/assets/readme/images/database-models.png)
### Kanban Board

I used a kanban in GitHub Projects to help log my user stories. By doing this, I was able to keep on track.
I moved any tasks from Todo into In Progress as I worked on them, and then into Done once completed. I then moved onto the next set of tasks and followed the same steps until all the tasks were done.

![workflow1](/assets/readme/images/workflow1.png)
![workflow2](/assets/readme/images/workflow2.png)
![workflow3](/assets/readme/images/workflow3.png)

### Future Features

- Future features I would like to implement are:

    - The option to like other users' comments.
    - Functionailty to be able to upload videos as well as images.
    - Functionality to be able to upload multiple images in a single post.

## Technologies Used

### Languages and Packages/Libraries Used

1. [Django REST Framework](https://pypi.org/project/djangorestframework/3.14.0/)
2. [Django](https://www.djangoproject.com/)
3. [Python](https://www.python.org/)
4. [psycopg2](https://pypi.org/project/psycopg2/)
5. [Django all-auth](https://django-allauth.readthedocs.io/en/latest/installation.html)
6. [gunicorn](https://gunicorn.org/)
7. [PostgreSQL](https://www.postgresql.org/)
9. [dj-rest-auth](https://pypi.org/project/dj-rest-auth/2.2.5/)
10. [Django-filter](https://pypi.org/project/django-filter/22.1/)
11. [Djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/5.2.1/)
12. [Django-cors-headers](https://pypi.org/project/django-cors-headers/3.13.0/)

### Programs Used

1. [Git](https://git-scm.com/)
    - Git was used by utilizing the Gitpod terminal to commit to Git and Push to GitHub. Version control. 

2. [GitHub](https://github.com/)
    - GitHub was used to store the project code after being pushed in by Git. Project repository linked with Heroku for the deployment process. GitHub was also used to create the kanban board. 

3. [Heroku](https://dashboard.heroku.com/login)
    - Heroku was used to deploy this project.

4. [CI Python Linter](https://pep8ci.herokuapp.com/)
    - CI Python Linter was used to validate the Python code used and check for warnings/errors.  

5. [Cloudinary](https://cloudinary.com/)
    - Cloudinary is used to host the uploaded images.

6. [Autopep8](https://pypi.org/project/autopep8/)
    - Autopep8 was used to help organize Python code to match PEP8 standards.

7. [ElephantSQL](https://www.elephantsql.com/)
    - ElephantSQL was used for the configured and optimized PostgreSQL database.

8. [Pillow](https://pypi.org/project/Pillow/9.2.0/) 
    - Python Imaging Library which provides image processing capabilities.

## Testing

### Validation Testing

- All files have been run through CI Python Linter and all files returned no issues.
### Manual Testing

- Comprehensive testing has been conducted on the backend project, resulting in lists of successful outcomes.
- The testing process involved repeated manual execution of each list to ensure consistent success and flawless functionality.
- Each list was systematically tested multiple times to confirm the flawless performance of the project.

#### Profile:
- Users are able to successfully create an account and their profile, default image, and content are saved in the database.
- Users are able to view their username, image, content, when their account was created, etc.
- The post count, following count, and follower count are visible in the user API. When creating new posts, following new users or being followed, the numbers will go up, and will decrease when there are any deletions or unfollows.
- A List of users are shown in the list view, and a detailed list of users will show with the approrpriate id.
- Users are able to be deleted in the backend.
- All urls are working perfectly. Can view all profiles when visiting `/profiles/`. Can access specific profiles in detail view when adding specific profile id to url.

#### Post:
- Users are able to successfully create posts and have the posts attached to the user id.
- The number of posts tied to a user will increase or decrease if the user posts more or deletes posts. 
- API shows whether the logged-in user is the owner of the post or not.
- The posts successfully show the owner, when it was created, when it was updated, the post image, the content, and title.
- Posts are successfully able to be edited and deleted only by the owner of the post.
- Image validation created in the serializer.py works as images posted by the user must be less than 1 MG, smaller than 2500 px in width and in height. 
- The list of posts appear in the list view page, and a detailed view of posts will appear in the detail view page with the appropriate post id.
- Posts are successfully able to be searched by typing owner or title.
- Posts are able to be liked and unliked, and have the number of likes edited accurately. 
- All urls are working perfectly. Can view all posts when visiting `/post/`. Can access specific posts in detail view when adding specific post id to url.

#### Comment:
- Users are able to successfully create comments and have the comments attached to the user id and post id.
- The number of comments will increase or decrease if the user chooses to delete or remove the comment.
- API shows whether the logged-in user is the commenter of the comment or not.
- The comments successfully show the commenter, when it was created, when it was updated, and the content.
- Comments are successfully able to be edited and deleted only by the commenter of the post.
- The list of comments appear in the list view page, and a detailed view of comments will appear in the detail view page with the appropriate comment id.
- Comments associated with a given post are successfully able to be retrieved. 
- All urls are working perfectly. Can view all comments when visiting `/comment/`. Can access specific comments in detail view when adding specific comment id to url.
    
#### Follower:
- Users are successfully able to follow other users. API successfully reads which user is the follower, and which user is being followed.
- The creation date of the follow is successfully logged with the number of days shown. 
- If a user tries to follow a user again, the API will throw a duplicate validation error.
- The list view successfully shows a list of all follows.
- In detail follow view, can see detailed information on the follow.
- Users are able to successfully unfollow the users that they are following.
- Users are able to follow themselves in the backend. But in the frontend, conditional rendering will be applied to prevent users from following themselves. 
- All urls are working perfectly. Can view all followers when visiting `/follower/`. Can access specific followers in detail view when adding specific follower id to url.

#### Likes:
- Users are successfully able to like other posts. API successfully registers the post_likes_id to the post.
- Users are successfully able to unlike the posts that they have liked. 
- Users are not able to like their own posts or else a permission denied error will be thrown.
- If users try to like a post they have already liked, the API will throw a duplicate validation error.
- All urls are working perfectly. Can view all post likes when visiting `/post_likes/`. Can access specific post likes in detail view when adding specific post likes id to url.

#### Authentication:
- Users are able to create a new account on the backend and the new user details will be saved. 
- In the backend, users are able to successfully login and view their username in the navigation bar.
- Users are able to log out of the backend successfully. 
### Bugs

I came across many bugs during this process, and spent a lot of time on with tutor support to help me resolve these issues.

1. Frontend was acting as though I was logged in but backend was showing as undefined. After speaking with tutor support, it was discovered that I had installed django-rest-auth v5.0.1 which did not support the code - installed v2.1.9 and allauth v0.44.0 instead of v0.55.2 for compatibility as Heroku failed to deploy with v0.55.2

2. Kept receiving 500 error when I was attempting to create a post - I had used "length" instead of "height" in the image validation in the Post Serializer.

3. I was unable to edit a comment successfully - this was my longest lasting bug, and I spent a lot of time through a lot of different channels trying to resolve this:
    - Tutor Support
    - Google
    - Slack
    - ChatGPT
    - Mentor Support

    - I changed my code a lot to try and resolve this issue as I was getting many different errors:
        - Heroku app logs:
            - django.core.exceptions.ImproperlyConfigured: Field name `profile_id` is not valid for model `Comment`.
            - I updated the Comment model to show `profile_id` - this resolved the Heroku app logs but led to another error:
        - console error:
            - AxiosError {message: 'Request failed with status code 400'}
            - `{"owner":["This field is required."]}`
            - So I went back to my backend code and took it back to basics by following the Django REST walkthrough project - after fiddling around with the code and makign sure there were no typos, the issue was finally resolved.

## Deployment

- The following steps were taken for the deployment process for the back end component of Yakker. These steps take place after Django is correctly installed and an 'env.py' file is made (and file is added to .gitignore). [Cloudinary](https://cloudinary.com/) must also be successfully hooked up to Django by adding in all necessary imports and settings in 'settings.py' and 'env.py'.
Instructions are copied from CI's DRF Example Project. 
 
1. Login or create an account to [ElephantSQL](https://www.elephantsql.com/) and click "Create New Instance".
2. Set up a plan, give your plan a name (name of project), select the Tiny Turtle (free plan), leave the Tag fields blank, and select your region. 
3. Click review, and after ensuring details are correct, click 'Create instance'. 
4. Return to ElephantSQL dashboard and click database instance name for this project.
5. In URL section, click the copy icon to copy database URL.
6. Log in to [Heroku](https://www.heroku.com/).
7. Create a new app, add a unique app name (this project is called "yakker") and choose your region, and create app.
8. Open the settings tab of your project, Add a Config Var 'DATABASE_URL' and for the value, copy in the database URL from ElephantSQL (without quotation marks).
9. In terminal of your project, run `pip3 install dj_database_url==0.5.0 psycopg2`. 
10. In 'settings.py' file of project, add `import dj_database_url` underneath `import os`.
11. In 'settings.py', update the DATABASES section to the following:
    ![Screenshot of database setting code](documentation/deployment-settings-screenshot.png)
12. In your 'env.py' file, add a new environment variable to Gitpod with the key set to `DATABASE_URL` and the value to your ElephantSQL database URL. 
13. Temporarily comment out the DEV environment variable so Gitpod can connect to external database. 
14. Back in 'settings.py', add print statement to confirm you are connected do database.
15. In terminal do a dry run to makemigrations to confirm you are connected to the database. If you see the 'connected' message printed in terminal, remove print statement. 
16. Migrate your database models running `python3 manage.py migrate`.
17. In terminal of Gitpod workspace, install gunicorn by running `pip3 install gunicorn django-cors-headers`.
18. Update your requirements.txt by running `pip3 freeze --local > requirements.txt`.
19. Create a Procfile by running `touch Procfile`.
20. Inside Procfile, add: 
`release: python manage.py makemigrations && python manage.py migrate`
`web: gunicorn drf_api.wsgi`
21. In 'settings.py', update value of ALLOWED_HOSTS variable to include Heroku app's URL.
22. Add corsheaders to INSTALLED_APPS of 'settings.py'. 
23. Add corsheaders middlewear to the TOP of MIDDLEWARE.
24. Under MIDDLEWARE list, set the ALLOWED_ORIGINS for network requests to be made to the server with following code: 
    ![Screenshot of cors allowed origins setting code](documentation/deployment-cors-origins.png)
25. To have front-end app and API deployed to different platforms, set JWT_AUTH_SAMESITE atribute to 'None' like so:
    ![Screenshot of jwt setting code](documentation/deployment-jwt.png)
26. Remove the SECRET_KEY value and replace the following code to use an environment variable instead.
27. Set a new value for SECRET_KEY in env.py (do not use the same published to GitHub in commits).
28. Set the DEBUG value to True only if DEV environment variable exists. This will mean it's True in development, and False in production.
29. Comment DEV back in 'env.py'.
30. Ensure 'requirements.txt' file is up to date by running `pip3 freeze --local > requirements.txt`.
31. Add, commit, and push your code to GitHub. 
32. Back on Heroku dashboard, open your app and open settings tab.
33. Add two more Config vars, SECRET_KEY (same value as the one in env.py file) and CLOUDINARY_URL (copy in Cloudinary URL from env.py file without quotation marks).
34. Open the Deploy tab.
35. In Deployment method section, select 'Connect to GitHub', search for your repo, and click Connect. 

- The following steps were taken for the cloning process: 

1. Log in to **[GitHub](https://github.com/)**.
2. Click on the profile icon to locate **'Your repositories'**. 
3. On the repository page, click on the repository you wish to clone.
4. Under **'Code'**, see the different cloning options, HTTPS, SSH, and GitHub CLI. Click the preferred cloning option, and then copy the link provided. 
5. Open **Terminal**.
6. In Terminal, change the current working directory to the desired location of the cloned directory.
7. Type git clone, and then paste the URL copied from GitHub earlier. 
8. Type **Enter** to create the local clone. 

## Credits

### Code

- [Code Institute DRF API Example Project](https://github.com/Code-Institute-Solutions/drf-api)
    - Most of code is inspired by Code Institute's DRF API example project, including the database model, the different features and functionality of the API, creating serializers, setting up the project, setting up filters and search fields, etc. 

- [Django Documentation](https://www.djangoproject.com/)
    - The official Django documentation was referred to many times while creating this project. 

- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
    - The official Django REST Framework documentation was referred to many times while creating this project. 

### Acknowledgements

- Firstly, and most importantly - Tutor Support for being extremely patient with me as I bugged them non-stop and used all my tutoring hours. I definitely could not have gotten through this project without you!
- My fellow students for helping me understand serializers.
- CI Walkthrough projects - massive amounts of inspiration taken from the projects.