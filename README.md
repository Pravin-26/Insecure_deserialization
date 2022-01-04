Remote Code Execution using Insecure Deserialization vulnerability



Vulnerable application: - 
•	It is simple vulnerable application which will return a cookie to every visitor.

Attack: - 
•	Session data is stored in cookies in form of serialized data. 
•	Crafted two payloads for Remote Code Execution - one payload to view files inside app directory & other payload to get a reverse shell.

Payloads: -
•	Defined a ‘reduce’ function in payload scripts which will return a Tuple. 
•	Tuple contain first value like ‘os.system’ & ‘subprocess’ which will be called during  deserialization process and then we supply command like ‘ls’ or ‘netcat’ to execute as a second value of tuple.
•	Payloads are encoded with ‘base64 encoding’ so that it can be injected in cookie value.


Testscript: -
•	Developed an automated script using Selenium, implemented Unit Test to test the code & fing bugs.
•	Testscript will load the vulnerable app in Chrome instance then change the cookie value on the webpage for Remote Code Execution.
•	First Test case will inject malicious value  from payload1 in cookie to view all the files in app directory.
•	Second Test case will inject malicious value from payload2 in cookie to get Reverse shell.
