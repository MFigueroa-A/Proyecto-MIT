import smtplib
#import mysql.connector
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


"""destinatarios = ['mathias.figueroa13@gmail.com', 'dannytorresogalde@gmail.com', 'alexander_7797@hotmail.com', 'kahel-1998@hotmail.com','marco.friant.94@gmail.com']
[x.encode('utf-8') for x in destinatarios]"""
me    = '' # me == my email address

you   = '' # you == recipient's email address

login = ''



# Create message container - the correct MIME type is multipart/alternative.

msg = MIMEMultipart('alternative')

msg['Subject'] = "Alert!!"

msg['From'] = me

msg['To'] = you


# Create the body of the message (a plain-text and an HTML version).

#text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
#titles =['aaa','bbb','ccc','ddd','eee']

html = """\
<!DOCTYPE html>

<html>
<head>
<title></title>
<meta charset="utf-8"/>
<meta content="width=device-width" name="viewport"/>
<link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css"/>
<link href="https://fonts.googleapis.com/css?family=Nunito" rel="stylesheet" type="text/css"/>
<link href="https://fonts.googleapis.com/css?family=Droid+Serif" rel="stylesheet" type="text/css"/>
<link href="https://fonts.googleapis.com/css?family=Cabin" rel="stylesheet" type="text/css"/>
<link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet" type="text/css"/>
<style>
		.bee-row,
		.bee-row-content {
			position: relative
		}

		.bee-row-3 .bee-row-content,
		body {
			background-color: #fbfbfb;
			color: #000
		}

		body {
			font-family: Cabin, Arial, Helvetica Neue, Helvetica, sans-serif
		}

		a {
			color: #175df1
		}

		* {
			box-sizing: border-box
		}

		body,
		p {
			margin: 0
		}

		.bee-row-content {
			max-width: 350px;
			margin: 0 auto;
			display: flex
		}

		.bee-row-content .bee-col-w12 {
			flex-basis: 100%
		}

		.bee-button .content {
			text-align: center
		}

		.bee-button a,
		.bee-icon .bee-icon-label-right a {
			text-decoration: none
		}

		.bee-divider,
		.bee-image {
			overflow: auto
		}

		.bee-divider .center,
		.bee-image .bee-center {
			margin: 0 auto
		}

		.bee-row-2 .bee-col-1 .bee-block-1 {
			width: 100%
		}

		.bee-icon,
		.bee-icon .bee-icon-image,
		.bee-icon .bee-icon-label-right {
			display: inline-block
		}

		.bee-icon {
			vertical-align: middle
		}

		.bee-icon .bee-icon-image {
			vertical-align: middle;
			margin-right: -4px
		}

		.bee-image img {
			display: block;
			width: 100%
		}

		.bee-social .icon img {
			max-height: 32px
		}

		.bee-text {
			overflow-wrap: anywhere
		}

		@media (max-width:370px) {
			.bee-row-content:not(.no_stack) {
				display: block
			}
		}

		.bee-row-1,
		.bee-row-7,
		.bee-row-8 {
			background-repeat: no-repeat
		}

		.bee-row-1 .bee-row-content,
		.bee-row-2 .bee-row-content,
		.bee-row-4 .bee-row-content,
		.bee-row-5 .bee-row-content,
		.bee-row-7 .bee-row-content,
		.bee-row-8 .bee-row-content {
			background-repeat: no-repeat;
			color: #000
		}

		.bee-row-1 .bee-col-1,
		.bee-row-3 .bee-col-1,
		.bee-row-4 .bee-col-1,
		.bee-row-5 .bee-col-1,
		.bee-row-7 .bee-col-1,
		.bee-row-8 .bee-col-1 {
			padding-bottom: 5px;
			padding-top: 5px
		}

		.bee-row-1 .bee-col-1 .bee-block-1 {
			padding-bottom: 20px;
			padding-left: 10px;
			padding-top: 20px;
			width: 100%
		}

		.bee-row-2,
		.bee-row-3,
		.bee-row-4,
		.bee-row-5,
		.bee-row-6 {
			background-color: #175df1;
			background-repeat: no-repeat
		}

		.bee-row-2 .bee-col-1 {
			padding-top: 5px
		}

		.bee-row-3 .bee-row-content {
			background-repeat: no-repeat
		}

		.bee-row-3 .bee-col-1 .bee-block-1,
		.bee-row-6 .bee-col-1 .bee-block-2,
		.bee-row-7 .bee-col-1 .bee-block-1 {
			padding: 10px
		}

		.bee-row-4 .bee-col-1 .bee-block-1 {
			padding-left: 10px;
			padding-right: 10px;
			padding-top: 15px
		}

		.bee-row-4 .bee-col-1 .bee-block-2 {
			padding: 15px
		}

		.bee-row-5 .bee-col-1 .bee-block-1,
		.bee-row-5 .bee-col-1 .bee-block-2,
		.bee-row-5 .bee-col-1 .bee-block-3,
		.bee-row-6 .bee-col-1 .bee-block-1 {
			padding: 10px;
			text-align: center
		}

		.bee-row-5 .bee-col-1 .bee-block-4 {
			padding: 25px 10px 10px
		}

		.bee-row-6 .bee-row-content {
			background-color: #175df1;
			background-repeat: no-repeat;
			color: #000
		}

		.bee-row-6 .bee-col-1 {
			padding-bottom: 20px;
			padding-top: 15px
		}

		.bee-row-8 .bee-col-1 .bee-block-1 {
			color: #9d9d9d;
			font-family: inherit;
			font-size: 15px;
			padding-bottom: 5px;
			padding-top: 5px;
			text-align: center
		}

		.bee-row-8 .bee-col-1 .bee-block-1 .bee-icon-image {
			padding: 5px 6px 5px 5px
		}

		.bee-row-8 .bee-col-1 .bee-block-1 .bee-icon {
			margin-left: 0;
			margin-right: 0
		}
	</style>
</head>
<body>
<div class="bee-page-container">
<!--- --><div class="bee-row bee-row-1">
<div class="bee-row-content">
<div class="bee-col bee-col-1 bee-col-w12">
<div class="bee-block bee-block-1 bee-image"><img alt="Logo" class="bee-center bee-fixedwidth" src="https://i.postimg.cc/kGtsmtD9/3b0c14e3-b341-43b0-8c05-f9291ec21a75.png" style="max-width:140px;"/></div>
</div>
</div>
</div>
<div class="bee-row bee-row-2">
<div class="bee-row-content">
<div class="bee-col bee-col-1 bee-col-w12">
<div class="bee-block bee-block-1 bee-image"><img alt="" class="bee-center bee-autowidth" src="https://i.postimg.cc/MX2DKKjB/warning-symbol-warning-sign-design-template-5becb2f6646d14a8076b36a92efb1db8-screen.png" style="max-width:350px;"/></div>
</div>
</div>
</div>
<div class="bee-row bee-row-3">
<div class="bee-row-content">
<div class="bee-col bee-col-1 bee-col-w12">
<div class="bee-block bee-block-1 bee-text">
<div class="bee-text-content" style="font-size: 14px; line-height: 120%; font-family: inherit; color: #ffffff;">
<p style="font-size: 14px; line-height: 16px; text-align: center;"><span style="font-size: 22px; line-height: 26px;"><strong style=""><span style="color: #175df1; line-height: 14px;">ALERTA!!! 🚨<br style=""/></span></strong></span></p>
</div>
</div>
</div>
</div>
</div>
<div class="bee-row bee-row-4">
<div class="bee-row-content">
<div class="bee-col bee-col-1 bee-col-w12">
<div class="bee-block bee-block-1 bee-text">
<div class="bee-text-content" style="font-size: 14px; line-height: 120%; font-family: 'Cabin', Arial, 'Helvetica Neue', Helvetica, sans-serif; color: #ffffff;">
<p style="font-size: 30px; line-height: 36px; text-align: center;"><span style="font-size: 38px; line-height: 45px;">Hola <span id="66cf0b74-5d0c-4402-b944-88d39970c011" style="line-height: 14px;">@usuario</span><br style=""/></span></p>
</div>
</div>
<div class="bee-block bee-block-2 bee-text">
<div class="bee-text-content" style="font-size: 14px; line-height: 150%; color: #ffffff; font-family: inherit;">
<p style="font-size: 14px; line-height: 21px; text-align: center;"><span style="font-size: 17px; line-height: 25px;"><strong style=""><span style="font-size: 20px; line-height: 30px;">Se ha detectado poca humedad en el suelo</span> 😢<br style=""/></strong></span></p>
<p style="font-size: 14px; line-height: 21px; text-align: center;"><span style="font-size: 17px; line-height: 25px;"><strong style=""><span style="font-size: 20px; line-height: 30px;"> Se le recomienda regar lo antes posible !!</span> 😀</strong><br style=""/></span></p>
</div>
</div>
</div>
</div>
</div>
<div class="bee-row bee-row-5">
<div class="bee-row-content">
<div class="bee-col bee-col-1 bee-col-w12">
<div class="bee-block bee-block-1 bee-button">
<div class="bee-button-content" style="font-size: 14px; line-height: 28px; background-color: #f9c253; border-bottom: 0px solid #8a3b8f; border-left: 0px solid #8a3b8f; border-radius: 4px; border-right: 0px solid #8a3b8f; border-top: 0px solid #8a3b8f; color: #ffffff; font-family: inherit; max-width: 100%; padding-bottom: 5px; padding-left: 60px; padding-right: 60px; padding-top: 5px; width: auto; font-weight: 400; display: inline-block;"><span style="font-size: 16px; line-height: 200%; word-break: break-word;">Temperatura: 26°C</span></div>
</div>
<div class="bee-block bee-block-2 bee-button">
<div class="bee-button-content" style="font-size: 14px; line-height: 28px; background-color: #f9c253; border-bottom: 0px solid #8a3b8f; border-left: 0px solid #8a3b8f; border-radius: 4px; border-right: 0px solid #8a3b8f; border-top: 0px solid #8a3b8f; color: #ffffff; font-family: inherit; max-width: 100%; padding-bottom: 5px; padding-left: 60px; padding-right: 60px; padding-top: 5px; width: auto; font-weight: 400; display: inline-block;"><span style="font-size: 16px; line-height: 200%; word-break: break-word;">Humedad Suelo: 30%</span></div>
</div>
<!-- <div class="bee-block bee-block-3 bee-button">
<div class="bee-button-content" style="font-size: 14px; line-height: 28px; background-color: #f9c253; border-bottom: 0px solid #8a3b8f; border-left: 0px solid #8a3b8f; border-radius: 4px; border-right: 0px solid #8a3b8f; border-top: 0px solid #8a3b8f; color: #ffffff; font-family: inherit; max-width: 100%; padding-bottom: 5px; padding-left: 60px; padding-right: 60px; padding-top: 5px; width: auto; font-weight: 400; display: inline-block;"><span style="font-size: 16px; line-height: 200%; word-break: break-word;">Humedad aire: 40</span></div>
</div> -->
<div class="bee-block bee-block-4 bee-divider">
<div class="center" style="border-top:7px solid #FBFBFB;width:100%;"></div>
</div>
</div>
</div>
</div>
<div class="bee-row bee-row-6">
<div class="bee-row-content">
<div class="bee-col bee-col-1 bee-col-w12">
<div class="bee-block bee-block-1 bee-social">
<div class="content"><span class="icon" style="padding:0 7.5px 0 7.5px;"><a href="http://www.example.com/"><img alt="Facebook" src="https://i.postimg.cc/zf00Sr9m/facebook2x.png" title="Facebook"/></a></span><span class="icon" style="padding:0 7.5px 0 7.5px;"><a href="http://www.example.com/"><img alt="Twitter" src="https://i.postimg.cc/3xjLNp1x/twitter2x.png" title="Twitter"/></a></span><span class="icon" style="padding:0 7.5px 0 7.5px;"><a href="http://www.example.com/"><img alt="Instagram" src="https://i.postimg.cc/V6v4Kh8J/instagram2x.png" title="Instagram"/></a></span><span class="icon" style="padding:0 7.5px 0 7.5px;"><a href="http://www.example.com/"><img alt="LinkedIn" src="https://i.postimg.cc/YSpdW9Df/linkedin2x.png" title="LinkedIn"/></a></span></div>
</div>
<div class="bee-block bee-block-2 bee-text">
<div class="bee-text-content" style="font-size: 14px; line-height: 180%; color: #ffffff; font-family: inherit;">
<p style="font-size: 14px; line-height: 25px; text-align: center;"><strong style="">IQUIQUE - CHILE<br style=""/></strong></p>
</div>
</div>
</div>
</div>
</div>
<div class="bee-row bee-row-7">
<div class="bee-row-content">
<div class="bee-col bee-col-1 bee-col-w12">
<div class="bee-block bee-block-1 bee-divider">
<div class="spacer" style="height:0px;"></div>
</div>
</div>
</div>
</div>
<div class="bee-row bee-row-8">
<div class="bee-row-content">
<div class="bee-col bee-col-1 bee-col-w12">
<div class="bee-block bee-block-1 bee-icons">
<div class="bee-icon">
<!--- <div class="bee-icon-image"><a href="https://www.designedwithbee.com/" target="_blank" title="Designed with BEE"><img alt="Designed with BEE" height="32px" src="https://i.postimg.cc/vBKhkvY3/bee.png" width="auto"/></a></div>
<div class="bee-icon-label-right"><a href="https://www.designedwithbee.com/" target="_blank" title="Designed with BEE">Designed with BEE</a></div> -->
</div>
</div>
</div>
</div>
</div>
</div>
</body>
</html>> """ 

# Record the MIME types of both parts - text/plain and text/html.

#part1 = MIMEText(text, 'plain')

#part2 = MIMEText(html, 'html')

part3 = MIMEText(html, 'html', 'utf-8')


# Attach parts into message container.

# According to RFC 2046, the last part of a multipart message, in this case

# the HTML message, is best and preferred.

#msg.attach(part1)

#msg.attach(part2)

msg.attach(part3)

# Send the message via local SMTP server.

mail = smtplib.SMTP('smtp.gmail.com:587')


mail.ehlo()


mail.starttls()

mail.login(me, login)
mail.sendmail(me, you, msg.as_string())
mail.quit()