# MACOS CONFIGURATION

# ===================

The following will help you setup this script on your macos cron using crontab.

## 1. Clone this repository

```bash
git clone https://github.com/noelzappy/jibble-auto-clocking && cd jibble-auto-clocking
```

NB: You can also download the zip file and extract it.

### ENSURE YOU UPDATE THE LOGIN CREDENTIALS LABELED AS `user_email` AND `password` IN BOTH THE `clock_in.py` AND `clock_out.py` FILES. THIS STEP IS IMPORTANT.

## 2. Create a directory to store the script logs

```bash
mkdir -p ~/.scripts
```

This will create a directory called `.scripts` in your home directory. This directory is hidden by default.

## Move scripts files to the directory

```bash
mv clock_in.py ~/.scripts
mv clock_out.py ~/.scripts
```

This will move the scripts to the directory we created in the previous step.

## 3. Create a cron job

```bash
crontab -e
```

This will open the crontab file in your default editor. If you don't have a default editor, it will open the file in `vi`. Incase you don't know how to use `vi`, you can use `nano` by running the following command:

```bash
EDITOR=nano crontab -e
```

Or you can do a quick google search on how to use `vi`.

### Add the following lines to the file

```bash
# Clock in at 8:56am every weekday
56 8 * * 1-5 cd ~/.scripts &&  /usr/local/bin/python3 clock_in.py

# Clock out at 5:01pm every weekday
1 17 * * 1-5 cd ~/.scripts &&  /usr/local/bin/python3 clock_out.py
```

This will clock you in at 8:56am every weekday and clock you out at 5:01pm every weekday.

### Save and exit the file

```bash
:wq
```

This will save and exit the file.

## 4. Test the cron job

```bash
crontab -l
```

This will list all the cron jobs you have set up. You should see the two jobs you just added.
