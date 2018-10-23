# FlaskMail
# How to Send Emails using Python

Have you ever wondered how companies like Medium send millions of Emails to their massive user-base in minutes? And how they make it look so visually appealing which basically looks like a website in a mail?
![](https://cdn-images-1.medium.com/max/2000/1*fRrwI-_ekP4PkQ4TDtYUyw.png)

Let's write a few lines of Python code that will allow us to sent emails to 1000's of people at once just by running that python script.
##  💻 Lets pip First
We are going to use Flask and Flask-mail to do this. So open your command prompt & do.
`pip install Flask Flask-Mail`

# Code 
You only need 3  easy steps for this:
## 1. Create a Flask App
Let's start by creating a Flask app. 
![](https://cdn-images-1.medium.com/max/880/1*5ukhuSn0sBHrr_O-1QwZCA.png)


We will be using mail variable to manage the features the instance "Mail" present in the [Flask-Mail](https://pythonhosted.org/Flask-Mail/) library.


## 2. Add Your Details
![](https://cdn-images-1.medium.com/max/880/1*JLI7SZLMZToRvZBzWkhmvA.png)
## 3. Compose & Send [Simple]
![](https://cdn-images-1.medium.com/max/1100/1*VrejNCUcPEIIJEqajR3fKQ.png)
![](https://cdn-images-1.medium.com/max/1100/1*WIhi84XNh1vdaxkiqRKmfA.png)
## 🍓 Compose & Send [Advanced]
By using .html instead of .body you can use different html tags and add .svg, .png too.  I am using <img> argument to add image using Url.


![](https://cdn-images-1.medium.com/max/1100/1*s_0nooHpNF3bBePm6axXfA.png)
![](https://cdn-images-1.medium.com/max/880/1*EtDLMXCS76nanEH7nsnGng.png)


## 🍓 Compose & Send [Pro]
Now that we know how add text & image. We can use different .html tags in combination with text and images to make it impressive like any other company Email. Also add <button> </button> redirecting users to your new websites.


![](https://cdn-images-1.medium.com/max/880/1*8xMggon62Wwp8R1qCI-P9w.png)


## 💁 Keep in Mind
Since our code is not a full fledged app at this point, you may need to toggle your Gmail Setting.

![](https://cdn-images-1.medium.com/max/880/1*vd0kXIICbB9OvfupIDg4ew.png)

## How can I Send Personalized Email to 1000's of Users?!
## Automate Mails
_(like)_ **Change User's Name** -  Use python to go through a .txt or excel document of your user base and parse through all the names one by one and replace it in the mail.

```
with app.app_context():
    for user in users:
        message = '...'
        subject = "Hello, %s" % user.name
        msg = Message(recipients=[user.email],
                      body= message,
                      subject = subject)
        mail.send(msg)
```

**!dea:** You can also change all the "he" to "she" or vice-versa depending on the gender.

## How can I Attach Files with the Mail ?!
### Attaching Files
Here we are attaching image.png file present in the same folder.
```
with app.open_resource("image.png") as fp:
    msg.attach("image.png", "image/png", fp.read())
```
