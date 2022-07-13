import smtplib
from ssl import HAS_TLSv1_2
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# conexion a base
import mysql.connector

conexion = mysql.connector.connect( user="", # usuario de la base base de datos
                                    password="", # contraseña de la base de datos
                                    host="", # el host en donde esta almacenado la base de datos
                                    db="", # nombre de la base de datos
                                    port="" # puerto, ejemplo: 3306
)
 

# consulta SQL

cur = conexion.cursor()
query = '''select TEMPERATURE, MOISTURE, DATE from sensor1 order by id desc limit 1;''' 
cur.execute(query)

data = cur.fetchall()
soil = float(data[len(data)-1][1]) # transformacion del dato en la posicion 1 de int a float, ejemplo: 750.0
soil_1 = soil/10 # nueva variable con el dato tranformado a float, dividido en 10 para dejarlo con 1 decimal, ejemplo: 75.0
cur.close()


if soil_1 < 60.0:

            me    = " " # me == email remitente

            you   = ' ' # you == email destinatario

            login = ' ' # contraseña de la cuenta del remitente


            # Create message container - the correct MIME type is multipart/alternative.

            msg = MIMEMultipart('alternative')

            msg['Subject'] = "Alerta!! 🚨"

            msg['From'] = me

            msg['To'] = you


            # Create the body of the message (a plain-text and an HTML version).

            html = """\
            <html>
            <head>

            </head>
            <body>
                <p>Se ha detectado poca humedad 😢</p>
                <p>Se le recomienda regar lo antes posible !! 😀</p>
                <table width="100%%" height="100%%" border="5px">
                    <tr>
                        <td>Temperatura: {}°C</td>
                    </tr>
                    <tr>
                        <td>Humedad Suelo: {}%</td>
                    </tr>
                    <tr>
                        <td>Fecha: {}</td>
                    </tr>
                </table>
            </body>
            </html> """ .format(data[0][0], soil_1, data[0][2])


            # Record the MIME types of both parts - text/plain and text/html.

            part3 = MIMEText(html, 'html', 'utf-8')


            # Attach parts into message container.

            # According to RFC 2046, the last part of a multipart message, in this case

            # the HTML message, is best and preferred.

            msg.attach(part3)

            # servidor SMTP y puerto ejemplo: stmp.gmail.com:465

            mail = smtplib.SMTP(' ')


            mail.ehlo()


            mail.starttls()

            mail.login(me, login)
            mail.sendmail(me, you, msg.as_string())
            mail.quit()
            print("Correo enviado correctamente")
else:
    print("No falta humedad")
    pass






