from flask import Flask
from flask_mail import Mail, Message
import os
app = Flask(__name__)

mail_settings = {
"MAIL_SERVER": 'smtp.gmail.com', 
    "MAIL_USE_TLS": False, #Transport Layer Security
    "MAIL_USE_SSL": True,  #Secure Sockets Layer
    "MAIL_PORT": 465, 		 #For using SSL
    "MAIL_USERNAME": 'aDD YOUR eMAIL @gmail.com',
    "MAIL_PASSWORD": 'yOUR pASSWORD hERE'
    }
app.config.update(mail_settings)
mail = Mail(app)

if __name__ == '__main__':
	with app.app_context():
		msg = Message(sender=app.config.get("MAIL_USERNAME"),recipients=["wHO tO sEND @gmail.com"])
		msg.subject = " Hello "
		msg.html =  """   
        
<!DOCTYPE html>
<html>
<head>
    <title>Email Template</title>
    <link href="https://fonts.googleapis.com/css?family=Niramit" rel="stylesheet">
    <style>
        .paragraph{
    font-family: 'Niramit', sans-serif;
    font-style: 50px

}
.button {
    background-color: #4CAF50; /* Green */
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
}

.button3 {background-color: #f44336;} /* Red */ 

    </style>
 
</head>
<body style="margin: 0; ">
    
    <table align="center" border="0" cellpadding="20" cellspacing="0" >
        <tr><td>
    <table align="center" border="0" cellspacing="0" width="300">
        <tr>
            <td align="center">
                <h1 class="paragraph" style="font-size: 50px">Universe</h1>    
                <img src="https://pbs.twimg.com/media/C_kwC7GWAAE-uyY.jpg" alt= "Creating Email Magic" width="900" height="300">
            </td>
        </tr>
        <tr>
            <td bgcolor="#ffffff" style="padding-top: 20px">
                <table border="0" cellpadding="0" cellspacing="0" width="100%">
            <tr>
                <td align="center">
                    <h1 class="paragraph">Mankind was born on Earth. It was never meant to die here.</h1>
                </td>
            </tr>
            <tr>
                <td align="center">
                <p class="paragraph">“We used to look up at the sky and wonder at our place in the stars, now we just look down and worry about our place in the dirt.”  <b>- Cooper</b> </p>
                </td>
            </tr>

         <tr>
            <td align="center">
                <img src="https://vignette.wikia.nocookie.net/interstellarfilm/images/3/30/Imax-poster-for-interstellar.jpeg/revision/latest?cb=20141003183300" alt= "Creating Email Magic" width="250" height="370">
             
        </td>
    </tr>

    <tr>
        <td align="center" style="padding-top: 50px">
        
        <font style="font-family: 'Niramit', sans-serif;font-style: 50px">
        In the future, Earth is slowly becoming uninhabitable. Ex-NASA pilot Cooper, along with a team of researchers, is sent on a planet exploration mission to report which planet can sustain life.
        </font>
        </td>
    </tr>

    <tr>
    <td align="center">
        <img src="https://coverfiles.alphacoders.com/449/44921.jpg" alt= "Creating Email Magic" width="900" height="300">
        
    </td>
    </tr>
    </td>
</tr>
</table>
</table>

<div align="center" style="padding-top: 20px">
<a href="https://in.bookmyshow.com/vadodara">
    <button class="button button3" value="Book Tickets!" onclick="window.open('https://in.bookmyshow.com/vadodara')">Book Tickets!</button>
</a> 
</div>

</body>
</html>

"""
		mail.send(msg)




 
        							# <img src="https://cdn.dribbble.com/users/1815223/screenshots/5408785/flmdribbox_edit_04_stxcolor_preview.gif" width="800" height="600"  />
               #      # <img src="http://helloracer.com/webgl/" width="800" height="600"  />
               #        <img src="https://cdn.dribbble.com/users/2541080/screenshots/5405337/34gopro_1x.png" width="399" height="300"  />




