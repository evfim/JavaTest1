FROM tomcat:9.0

#COPY /requirements.txt .
#RUN pip install -r requirements.txt
#RUN mkdir video
#COPY / .

#COPY /target/CRMMVC.war /usr/local/tomcat/webapps/
COPY /target/CRMMVC.war /var/lib/tomcat9/webapps/


#CMD python chaimtube.py