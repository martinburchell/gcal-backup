#!/usr/bin/env python
import sys
import os
import urllib2
import datetime

# Google Calendar Backup Script
# Saves your Google Calendars in ICS format from private or public links
# that can then be imported into most calendaring applications.
# This script really isn't meant for syncing, just backup in case Google's
# cloud explodes and loses your data.

# Version 1.0 
# Leander Hutton
# www.one-button.org
# github.com/lhutton

from settings import *


# Get the current date 
currentdate = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')

try:
	# test to see if the backup directory exists
	# if not create it
	if not os.path.exists(backupdir):
		os.makedirs(backupdir)
	# download the files
	# write them to disk
	keys = calendars.keys() 
	for calendar in keys:	
		response = urllib2.urlopen(calendars[calendar])
		cal = response.read()
		os.chdir(backupdir)
		filename = calendar + '-' + currentdate + '.ics'
		calfile = open(filename, "w")
		calfile.write(cal)
		calfile.close()
except IOError, e:
	print "I/O error({0}): {1})".format(e.errno, e.sterror)
except:
	print "Unknown error:", sys.exc_info()[0]
	raise
