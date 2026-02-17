📡 Basics of HTTP/HTTPS

Difference between HTTP and HTTPS HTTP (HyperText Transfer Protocol)
HTTP is a protocol used for communication between a client (browser) and a server.

Characteristics:

Data is sent in plain text

Not secure

Vulnerable to:

    - interception

    - modification

    - spying
Example:

http://example.com

Anyone on the network can see the data.

HTTPS (HyperText Transfer Protocol Secure)

HTTPS is the secure version of HTTP.

Characteristics:

Data is encrypted

Uses SSL/TLS encryption

Protects:

    - passwords

    - personal data

    - banking information
Example:

https://example.com

Encrypted data cannot be read by attackers.

Main difference summary: HTTP HTTPS Not secure Secure No encryption Encryption Port 80 Port 443 Data visible Data protected

Structure of HTTP Request and Response HTTP Request Structure
Example:

GET /index.html HTTP/1.1 Host: example.com User-Agent: Mozilla/5.0 Accept: text/html

Components:

Method Example:

GET POST

Defines action.

Path /index.html

Resource requested.

Headers

Provide information:

Host User-Agent Content-Type

HTTP Response Structure

Example:

HTTP/1.1 200 OK Content-Type: text/html Content-Length: 123

Hello
Components:

Status Code

Example:

200 OK 404 Not Found

Headers

Example:

Content-Type

Body

Actual data returned

Example:

HTML JSON

Common HTTP Methods GET
Description:

Retrieve data
Use case:

Fetch webpage
Example:

GET /users

POST

Description:

Create data
Use case:

Create user
Example:

POST /users

PUT

Description:

Update data
Use case:

Update user info
Example:

PUT /users/1

DELETE

Description:

Delete data
Use case:

Delete user
Example:

DELETE /users/1

Common HTTP Status Codes 200 OK
Description:

Request successful
Scenario:

Page loaded successfully
201 Created

Description:

Resource created
Scenario:

New user created
400 Bad Request

Description:

Invalid request
Scenario:

Missing required field
404 Not Found

Description:

Resource not found
Scenario:

Page does not exist
500 Internal Server Error

Description:

Server error
Scenario:

Server crashed
Status Code Categories Code Meaning 1xx Information 2xx Success 3xx Redirection 4xx Client error 5xx Server error