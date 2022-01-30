# CRMMVC
- Deploy Source Code
1. Open in Spring MVC source project in Eclipse JEE (> v4.7.2).
2. Open up src/main/resources/application.properties in the source project.
3. Ensure database credentials _jdbc.url, jdbc.username and jdbc.password_ are correct. Save for any change.
4. Right-Click on project _CRMMVC_ > Export > WAR File.
5. Enter Destination by clicking Browse. Type 'CRMMVC.war' as filename. Check _Overwrite existing file_ and click Finish.
6. Copy CRMMVC.war to _\<your tomcat directory\>_/webapps/ of your Tomcat server installation.

- Setup Database
1. Connect to MySQL server (> v5.6) on MySQL Workbench using DBAdmin User database credentials.
2. Under Navigator panel, select Management tab, select _Data Import/Restore_.
3. Under _Import from Self-Contained File_, locate the _CRMmvc.sql_ inside the Spring MVC project root directory.
4. Under _Default Schema to be Imported to_ section, click _New_ to create new schema.
5. Ensure 'Dump Structure and Data' is selected, click _Start Import_.
