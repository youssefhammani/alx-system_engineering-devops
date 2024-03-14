 Postmortem: The Great Database Disaster

# Incident Details:
---
# Identification of Deceased:

* Name: Youssef HAMMANI
* Gender: Male
* Nationality: Moroccan
---

#---What is a Software Post-Mortem and How Do You Write One?---

* Every company has their own name for the highest priority bugs. Priority one, emergencies, critical fixes or urgent fixes.

* There are software bugs that can end up crippling companies if they aren't dealt with rapidly.

* The Knight Capitol Group was an American financial services company. A technician forgot to copy some new code to a computer server, and this software release caused to them to lose $440 million. This happened because one of the computer servers started to rapidly purchase stock (it completed over 4 million purchases and sales) over a 45 minute period.
---
* Not every software bug is as dramatic. But there are moments as a software developer where you have to resolve bugs as fast as you can.

* I recently learned about companies releasing publicly accessible post-mortems on their emergency bugs, and dove head first into them.

# What is a post-mortem?
* A post-mortem is where a team reflects on what went wrong with something they did, and documents it and/or amends their process to stop it happening again.
---
# Did a software release go bad? Let's break down a timeline of where things started to go wrong, and let's reflect how we could have caught it earlier.
----
* Here is the most important point: Post-mortems ARE NOT to assign blame. If we look at The Knight Capitol Group example, there should have been no way for one person to forget something and cripple the company.
---
* Where was the quality assurance process where someone checked the technician's work? Did they test this before going to production? Were there no automatic tests that ran before the deploy to production succeeded?
---
* You should be finding process failures not personal failures.
---
# Why should we do a post-mortem?
---
* So we can stop making the same mistake over and over!
---
* We provide more robust, bug free, stable software by learning how we failed in the past.
---
* Most importantly, we can catch bugs we don't even know about. And if we fix the processes that were prone to cause issues early, then those mistakes won't even happen.
---
* We want to learn every single lesson we can from the outages and emergencies to ensure they never happen again. Nothing is more valuable than experience.

# Let's look at some post-mortems together
---
* I wanted a little bit of variety of companies and languages, so let's review some from Google, Microsoft, and Flowdock.
---
* A common post-mortem template will contain some key details like:
---
#  when it happened
---
* who owns the post-mortem (and will do the analysis)
* some lessons learned
* a rough timeline of the emergency bug and some actions from the post-mortem
* So let's dive in.
---
# Google
* If you did a Google search between 6:30 a.m. PST and 7:25 a.m. PST on January 31st, 2009, you would have seen the message "This site may harm your computer" accompanying every single result.
---
# What happened?
---
* Google flags search results with this message if the site is known to install malicious software. This is a warning to protect Google users, and is collated with Google's automatic algorithms, manual data entry, and a non-profit called StopBadWare.com.
---
* One of the developers had updated the list and accidentally entered in a /, which resolved to every single site!
---
* We know this one was human error, and because of this, Google implemented some tests and checks whenever that file changes. (And I haven't seen it happen again since 2009!)
---
# The full post-mortem can be found here.

# Microsoft
---
* Microsoft had a 12 hour outage on February 29th, 2012.
---
# What happened?
---
* Microsoft have Fabric Controllers which are computers that control around 1,000 servers. It manages their life cycles, monitors their health, and restarts servers when they go down.
---
* Isolating all these servers into 1,000 server clusters helps them keep modularity and keeps failures localized to 1 Fabric Controller (rather than all of their servers going down).
---
* Each server in the cluster has something called a Host Agent, and this is used by the Fabric Controller to do the work it deems necessary. One of the things it handles is deploying SSL certificates to keep the servers using HTTPS, which is a way of encrypting data.
---
* To know when these SSL certificates need to be re-generated, they take the next day at midnight and add one year. So if the Fabric Controller is creating a new certificate for a server on March 19, 1990 it will expire March 20, 1991.
---
* Do you see where this is going? These servers attempted to generate a one year certificate for a server on a leap year. It was trying to set the certificates to expire on February 30th, 2020.
---
* When the certificates fail to generate for the server, it terminates. And if it terminates three times in a row, it's considered to be a hardware failure, and then tells the Fabric Controller it is faulty.
---
* The Fabric Controller, in an attempt to "heal" the failed server, will hand over the work to another server. One by one, all the servers will error out while trying to generate these certificates. And this eventually shuts down the Fabric Controller (with it's 1000 servers!).
---
* This disaster resulted from faulty code. There are better ways to handle date problems like leap years and time-zone differences.
---
# The full post-mortem can be found here.
---
# Google, take two
---
* From Thursday August 13, 2015 to Monday August 17, 2015, there were some errors on Google Cloud services, along with permanent data loss on 0.000001% of some hard drives.
---
# What happened?
---
* There were four successive lightning strikes on the local electrical grid that sent power to Google's computers powering Google Cloud services.
---
* There were systems that began to immediately replace the power that was taken out by using a battery backup. Alongside manual intervention from Google employees, the service was restored with minimal permanent loss.
---
* Google has an ongoing program of upgrading their infrastructure so that they are less susceptible to issues like this. After this, they ran analysis covering electrical distribution, software controlling the Cloud services, and the Cloud hardware being used.
---
# The full post-mortem can be found here.
---
# Flowdock
---
* Flowdock instant messaging became unavailable for roughly 32 hours between April 21st and 22nd 2020. Weird behavior was also spotted, like some users not being able to log in. Also, some people found users from another organization in their organisation (like Amazon employees cross-contaminated Microsoft, for example).
---
# What happened?
---
* Coronavirus caused a sudden spike of people working from home, which led to a higher than usual usage of Flowdock. This caused very high CPU usage and caused the database to hang whilst trying to deal with the load. There was also some permanent data loss.
---
# The full post-mortem can be found here.
---
# Postmortem: The Great Database Disaster

## Issue Summary

**Duration**: March 10, 2024, 3:00 PM - March 11, 2024, 9:00 AM (UTC)
**Impact**: Database service outage resulted in slow response times, affecting 80% of users
**Root Cause**: Database server overload due to unoptimized queries

## Timeline

- **3:00 PM**: Issue detected by monitoring alert indicating high CPU usage on database server
- **3:15 PM**: Investigation initiated by DevOps team to identify the cause of the high CPU usage
- **4:00 PM**: Initial assumption made that a recent code deployment may have caused inefficient database queries
- **5:30 PM**: Development team involved to analyze recent code changes and their impact on database performance
- **6:00 PM**: Misleading assumption of a potential network issue explored and ruled out
- **7:30 PM**: Incident escalated to senior database administrator for further analysis
- **8:30 PM**: Root cause identified as poorly optimized database queries leading to excessive resource consumption
- **9:00 PM**: Immediate resolution implemented by optimizing the problematic queries and restarting the database server

## Root Cause and Resolution

- **Root Cause**: Unoptimized database queries causing high CPU usage and server overload
- **Resolution**: Optimized queries to reduce resource consumption and restarted the database server to restore normal functionality

## Corrective and Preventative Measures

- Improve query optimization practices to prevent similar issues in the future
- Implement regular code reviews to identify and address inefficient database queries
- Set up additional monitoring alerts for early detection of resource-intensive queries
- Conduct performance testing before deploying code changes to production environment

---

# Advanced: Adding a Touch of Humor

## Postmortem: The Great Database Disaster: A Tale of Queries and Quandaries

In the realm of databases, where SQL queries roam freely, an unsuspecting server found itself in the midst of chaos. Like a storm on the horizon, high CPU usage signaled impending doom. But fear not, for the brave DevOps team embarked on a quest to unravel the mystery.

As the sun set and the moon rose, developers and administrators alike delved into the depths of code and queries, seeking the elusive culprit. Alas, a misstep led them down a path of false assumptions, chasing shadows in the dark.

With the flicker of hope dwindling, a beacon of light emerged: the senior database administrator, wielding knowledge like a sword. With precision and prowess, the root cause was uncovered—a tale of unoptimized queries burdening the server beyond measure.

But fear not, for in the face of adversity, heroes rose. Queries were tuned, servers rebooted, and normalcy restored. And thus, the Great Database Disaster came to pass, leaving behind lessons learned and a legacy of resilience.

---

This postmortem aims to shed light on the trials and triumphs of a fateful outage, with a dash of humor to captivate the reader's attention. Through adversity, we find wisdom, and through laughter, we find connection.
