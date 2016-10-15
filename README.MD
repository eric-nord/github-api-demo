## GitHub API Demonstration
Simple use case of Github APIs, AWS S3, and SMTP via gmail to meet this coding challenge:

[Requirements and Assumptions](https://docs.google.com/document/d/17iH_e4RWnEHoxBZT7qNUh-vMGAQI53yUnsH_FgTQtuk/edit?usp=sharing)

## Installation
* Implemented in Python 2.7.6 
* requirements.txt for pip libraries
* Copy exampleconfig.py to config.py and add your Github, AWS S3, and gmail credentials
* AWS S3 user will need access to a S3FullAccess security group to upload files
* Gmail will need to allow unsecure applications and unlock Captcha to provide SMTP services. 
    https://www.google.com/settings/security/lesssecureapps <br>
    https://accounts.google.com/b/0/DisplayUnlockCaptcha 
* To run: python GitHubApiDemo/github_aip_demo.py

## License

MIT
