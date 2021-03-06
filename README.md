# Assassins Emailer

A simple python script that automates emailing people their targets (random) for the popular group game Assassins.
Super simple, easily deployable script that anyone can use to set up their Assassins games whether it be for a club,
a camp, or a class. 

## Prerequisites

Make sure you have Python3 installed. If you don't have it installed, you can find a guide here: 
http://docs.python-guide.org/en/latest/starting/install3/osx/

## Getting Setup

In order to run your own copy, make sure to clone the repository.

```
git clone https://github.com/justinhe16/assassins_emailer
```

After that you need to fill in and replace the members.txt and message.txt files with proper data.

members.txt is a .txt file, split up by spaces by the python script. It is formatted like so:
<First Name> <Last Name> <Email Address>

Here's an example:
```
Justin He justinhe16@gmail.com
Foo Bar foobar@gmail.com
Ronald McDonald rMc@gmail.com
...
```

message.txt is a .txt file that contains variables ${PERSON_NAME} and ${TARGET_NAME}, formulated and 
passed to the message.txt file in the python script. Feel free to play with the message.

**Important:** Make sure to make a tokens.py file and fill it in like so:
```
email_address = "me@gmail.com"
password = "yourrealpasswordhere"
```

## Execution

To run, just enter **python assassins.py** into terminal and watch as all your members are slowly emailed and assigned.

## Troubleshooting

Here is a list of problems you may run into. If you are a developer, feel free to send me a push request with edits on this section if you run into different kinds of problems that would be good for FAQ!

### Authentication does not work

You entered in your email correctly and everything, but it still won't let you authenticate :(. The key here is to go to your email provider's settings and you must allow low-security applications to access your mailbox. Additionally, you may have to turn on other functions/disable some security functions in your emailer to successfully authenticate through the python script.

### You are not using Gmail

If you are not using gmail, you will need to change the SMTP server settings on line 34 of assassins.py. You need to find the necessary host and port values of your email service provider (a quick google) and replace line 34 accordingly. 


## Contributing

Feel free to modify and improve and send me a push request!

## Authors

[![Libraries.io for GitHub](https://img.shields.io/badge/Justin%20He-justinhe16-blue.svg)](http://justinhe.com)

## License

[MIT](https://github.com/omgimanerd/rit-notes/blob/master/LICENSE)

