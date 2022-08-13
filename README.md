# Productivity Blog

<h3> Hi! This is a full-featured django blog about productivity and scientific stuff that you can register to it and post your articles.</h3>

<img src="screenshots/1.png" width='1200' heigth='650'>

<h3>• From register you can create a acount and you will redirect to home page with a flashy massage of success.</h3>
<h4> register from-model made by built-in django user model and a extensional email filed</h4> 
<img src="screenshots/2.png" width='1200' heigth='650'>
<img src="screenshots/3.png" width='1200' heigth='650'>

<h3>• When you create a acount you can login to your acount and you will have a profile with default profile picture!</h3>
<h4> with django singnals and a predfined profile-model, after creating a instance for User-model, profile atoumaticly create for that instance with default image profile in database</h4> 

<img src="screenshots/4.png" width='1200' heigth='650'>

<h3>• As you see after you log in at top of the page "Create Post" section is available for you and you can post a new article with abillity of deleting or updating that post any time you want but you can't make changes on other user posts!</h3>
<h4> with django mixins and login_required decorator we personalize some accessibility</h4> 
<h4> with class base views we have full CRUD funtionallity and unique url rout with using of primary key for every Post </h4> 

<img src="screenshots/5.png" width='1200' heigth='650'>
<img src="screenshots/6.png" width='1200' heigth='650'>
<img src="screenshots/7.png" width='1200' heigth='650'>
<img src="screenshots/8.png" width='1200' heigth='650'>

<h3>• And we can logout every time we want</h3>
<h4> django.auth has bilt-in LoginView and LougoutView classes that with seting url and making templete for them we can use their functionality.</h4>
<img src="screenshots/9.png" width='1200' heigth='650'>

<h3>• We have some pagination for our pages</h3>
<img src="screenshots/10.png" width='1200' heigth='650'>


<h3>• And this is how our admin pannel looks like </h3>
<img src="screenshots/11.png" width='1200' heigth='650'>
