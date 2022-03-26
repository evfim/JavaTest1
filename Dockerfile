FROM tomcat:9.0

#COPY /requirements.txt .
#RUN pip install -r requirements.txt
#RUN mkdir video
#COPY / .

COPY /target/CRMMVC.war /usr/local/tomcat/webapps/

#CMD python chaimtube.py