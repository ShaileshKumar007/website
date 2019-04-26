# What is Outreachy?

Outreachy is a three-month paid internship program for people traditionally underrepresented in tech.
This repository is for the Django code that comprises the [Outreachy website](https://www.outreachy.org).

# Current state of Outreachy tech

The Outreachy web presence is in a couple of different places:
 * [Outreachy website](https://www.outreachy.org)
 * [GitHub Repository](https://github.com/sagesharp/outreachy-django-wagtail/)
 * [Repository CI Status](https://travis-ci.org/sagesharp/outreachy-django-wagtail.svg?branch=master)

Older/deprecated websites include:
 - [GNOME Outreachy homepage](https://www.gnome.org/outreachy/) - shell homepage, where the outreachy.org domain currently redirects to
 - [GNOME wiki Outreachy pages](http://wiki.gnome.org/Outreachy) - moinmoin based wiki with information about how to apply and sponsor
 - [Outreachy application system](http://outreachy.gnome.org) - PHP-based application system currently hosted on OpenShift
 - irc.gnome.org #outreachy - GNOME IRC channel - where applicants get help
 - [Outreachy Planeteria](http://www.planeteria.info/outreach) - blog aggregation for Outreachy interns

# Future Long-term Goals

 - Replace planetaria with one hosted on our domain (that allows for filtering which blogs are displayed?)
 - Track longitudinal information of alumni, so we can share success stories and improve our program
 - Track sponsorship information
 - Create a better way of displaying the list of potential Outreachy projects - e.g. allow searching, tagging for programming language or design or documentation or user experience

# How does the Outreachy website tech work together?

The Outreachy website is built on a [Python](https://www.python.org/) and a web framework called [Django](https://www.djangoproject.com/). Additionally, the Outreachy website uses a content management system called [Wagtail](https://wagtail.io/), which builds on top of Django. On the Outreachy webserver, we run [Dokku](http://dokku.viewdocs.io/dokku/), which helps us deploy new code, manage our Let's Encrypt SSL certificates, and backup the Outreachy website database. Only Outreachy organizers have ssh access to push new code to the server.

# Optional helpful background reading

[Django topic guides](https://docs.djangoproject.com/en/1.11/topics/), particularly the [models](https://docs.djangoproject.com/en/1.11/topics/db/models/) guide.

# Setting up your development environment

You can run Django locally to test changes to the code, test creating new pages, test adding new users, etc. The local tests you run will not impact the main Outreachy website, only your local version of the website. You should test changes locally before submitting a pull request.

To set up your local development environment, first clone the repository to your local machine:

```
git clone https://github.com/sagesharp/outreachy-django-wagtail.git
```

In order to develop with Python, you'll need the Python 3 development headers, so install them. You'll also need to install node.js.

Next, you'll need to create a new virtualenv. A "virtualenv" is a separate virtual environment for working on different Python projects. It's good practice to create a virtual environment for each Python project you're working on, in case they have conflicting dependencies, and so that you make sure to record all the dependencies for each project.

These instructions will help you create a new virtualenv that will have all the python packages installed that you need to work on the Outreachy website. We use [pipenv](https://pipenv.readthedocs.io/en/latest/) for this purpose.

To install pipenv, you'll need to either [install Homebrew](https://brew.sh/) (if you're on a Mac or Windows) or (if you're running Linux) [install Linuxbrew](http://linuxbrew.sh/).

Then [install pipenv](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv).

The following command will automatically create a virtual environment and install the Python dependencies specified in the `Pipfile`. If you need help understanding pipenv, run `pipenv --help`

```
pipenv install
```

[Note: Pipenv automatically records changes in the project's dependencies in the `Pipfile` when you add/remove packages. You can add a package with the command `pipenv install <package>`. You can remove a package with the command `pipenv uninstall <package>`.]

Now, you activate the virtual environment by typing the following command in the directory of the project:

```
pipenv shell
```

In addition to the Python packages that were installed for you when you created the virtualenv, you also need to install some Node.js packages; these will be placed in a `node_modules` directory inside your project folder. Make sure you have `npm` installed, then run:

```
npm install
```

If this is your first time creating a local version of the website for testing, you'll need to set up the local website database from scratch. The following command will create a new database with the models in the Outreachy website. The database will initially have no website pages, but will eventually store your local test pages.

```
./manage.py migrate
```

The next step is to create an admin account for the local website.

```
./manage.py createsuperuser
```

You'll need to set up a new internship round, following the instructions in the next section.

# Django shell

Django has a 'shell' mode where you can run snippets of Python code. This is extremely useful for figuring out why view code isn't working. You can also use it to test complicated [query sets](https://docs.djangoproject.com/en/1.11/topics/db/queries/#retrieving-objects). It's also useful for doing quick tests of how templates (especially email templates) will look.

You can run the shell on either your local copy of the database, or you can run it on the remote server's database. If you start the shell on your local computer, it will load your local copy of the code and your local database. If you start the shell on the remote server, it will load the server's version of the code and the server's database. Remember, if you change any of the Python code, you'll need to exit the shell (CTRL-d) and restart it to reload the code.

## Setting up a new internship round

When you've first cloned and [set up the Outreachy website development environment](#setting-up-your-development-environment), you'll need to create a new internship round. The website expects to have at least one past round, and some pages won't work without a round. You may also need to set up a new round in your local database so you can test how the website looks during some particular phase. (See the section below for more explanation of the phases of the Outreachy round.)

In either case, the best way to do that is to use the shell to call into `home/factories.py` to create a new internship round. First, start the Django shell:

```
./manage.py shell
```

You'll get a Python prompt that looks fairly similar to the standard Python shell, except that all the Django code you've written is available. It will look like this:

```
$ ./manage.py shell
Python 3.6.6 (default, Jun 27 2018, 14:44:17) 
[GCC 8.1.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
```

First, import all the models in `home/models.py`:

```
>>> from home.models import *
```

We'll also need to import all the methods in `home/factories.py`:

```
>>> from home.factories import *
```

The advantage of using the factories methods is that it automatically computes reasonable dates for all round deadlines, based on what the Outreachy internship round schedule normally is. You just have to give it one date and it will calculate the rest.

### Contributions open

Let's assume you want an internship round where we're in the middle of the contribution period. We can set the deadline for when the final applications for most projects are due (`appsclose`) to be one week from today:

```
>>> import datetime
>>> RoundPageFactory(start_from="appsclose", start_date=datetime.date.today() + datetime.timedelta(days=7))
```

Note: Normally in the Django shell, you need to call the `save()` method to write the RoundPage object in the local database. The factories code automatically calls the `save()` method for you. Should you need to delete an object from the database, you can call the `delete()` method. Don't call `save()` afterwards, because that will write the object back to the database.

# Testing the local website

Once you've run the above setup commands, you should be all set to start testing your local website. First, run the command to start the Django webserver and serve up the local website.

```
PATH="$PWD/node_modules/.bin:$PATH" ./manage.py runserver
```

To make sure you've set up an internship round successfully, go to the internship project selection page at `http://localhost:8000/apply/project-selection/`. You should see that the internship round dates are correct. If you created an internship round where the final application date has passed, you can see older rounds at `http://localhost:8000/past-projects/`.

To go to the Django administrative interface, go to `http://localhost:8000/django-admin/`. You can log in into with the account you created with `./manage.py createsuperuser`. If you're new to Django, you may want to find the RoundPage you created and edit some of the dates. You can find it by clicking the 'Round pages' link under the HOME section. You'll see the changed dates reflected in the internship project selection page if you refresh it.

It's unlikely you'll need to access the Wagtail admin interface, where the local CMS content is managed. If you do need to access the Wagtail admin interface, go to `http://localhost:8000/admin/`. Use the same account you created with the `./manage.py createsuperuser` command.

# Tour of the code base

When you first clone this project, you'll see a couple top level directories:
 * `bin`
 * `contacts`
 * `docs`
 * `home`
 * `outreachyhome`
 * `search`

If you've followed the steps above to set up your development environment, Django may have generated some directories and put files in them. Don't modify or commit files from those directories. You can use `git status --ignored` to show you which directories are not supposed to be under revision control. Top-level directories you shouldn't commit to are ones like `media`, `node_modules`, and `static`. These directories are in the .gitignore file, so your changes to those files won't be listed if you run `git status`.

The `bin` directory almost never changes. It includes a script that's run by dokku before the website is deployed to outreachy.org.

The top-level directory `docs` is where our maintenance and design documents go. It also includes the intern and mentor agreements, and our privacy policy.

The `outreachyhome` directory contains the base HTML page templates for all pages on the website. It also includes all the Django project settings for both development and production environments. This directory isn't changed very often.

Django breaks up functionality into a project (a Django web application) and apps (smaller a set of Python code that implements a specific feature). There is only one project deployed on a site at a time, but there could be many apps deployed. You can read more about what an application is in [the Django documentation](https://docs.djangoproject.com/en/2.0/ref/applications/).  

In the Outreachy repository, the directory `outreachy-home` is the project. We have several apps:
* `home` which contains models used on most the Outreachy pages
* `search` which was set up during the wagtail installation to allow searching for pages and media
* `contacts` which is a Django app for our contact page

## External Django Packages

The Outreachy website also uses some Django apps that are listed in the `INSTALLED_APPS` variable in `outreachyhome/settings/base.py`. The Python module code for those Django apps aren't found in top-level directories in the repository. That's because the Python module code was installed into your virtualenv directory when you ran `pipenv install`. That command looked at the Python package requirements listed in `Pipfile` and installed each of the packages.

If you want to look at the source code of the installed external Django applications, you can use `pipenv open MODULE` to examine the source code files associated with that module. For example, say you notice the `home/models.py` file has an import line `from django.contrib.auth.models import User`. You can use pipenv open to look at the models.py file that contains the User class by running the command `pipenv open django.contrib.auth`. That will open all the files in the auth module in your editor, and you can then open models.py and search for `class User`.

## Outreachy terminology

Please use the gender-neutral ["they/them" pronouns](http://pronoun.is/they) and gender-neutral language to refer to all Outreachy participants.

 * **FOSS:** Free and Open Source Software.
 * **Project:** A series of intern tasks to improve FOSS.
 * **Community:** A community is a set of related projects. For instance, if Django participated as an Outreachy community, the community might mentor projects to improve Django core functionality, Django extensions, or Django documentation.
 * **Mentor:** A mentor defines a project. They work with applicants to help them complete contributions to the project during the application process. A mentor selects an applicant to be the intern for their project. The mentor works remotely with the selected intern during the internship. An intern can have one or more mentors. Most Outreachy mentors only mentor one intern.
 * **Coordinator:** Each internship project must be associated with a FOSS community participating in Outreachy. That community provides funding for interns, either directly from community funds, or by finding a company or foundation to sponsor interns. Each community has one or more coordinators, who review submitted projects, approve mentors, set internship funding sources, and generally provide a communication link between the mentors and Outreachy organizers. Some smaller communities have only one coordinator, who is also the only mentor.
 * **Outreachy organizers:** There is a small set of organizers who oversee the entire Outreachy program. They communicate with coordinators about funding, onboard new communities, review inern feedback, authorize intern payments, answer questions, and promote the program to potential applicants.
 * **Applicant:** During the application process, Outreachy applicants make contributions to projects and apply to be an Outreachy intern.
 * **Intern:** An accepted applicant works with a mentor for three months during the internship period.

## Outreachy Internship Phases

The Outreachy website changes depending on what phase of the internship round Outreachy is in. The phases of the internship round are:

 1. Community sign up and mentor project submission
 2. Initial application submission
 3. Applicant contribution period
 4. Final application submission period
 5. Intern selection period
 6. Intern announcement
 7. Internship period

Some of these phases overlap. For example, the project submission period ends part-way through the applicant contribution period. Since Outreachy internships run twice a year, that means one internship round may overlap with another. For example, the end of the intership period often overlaps with the community sign up and mentor project submission phase.

## Internship Rounds and Communities

The Outreachy internship round is represented by `class RoundPage` in `home/models.py`. It contains dates that define the phases of the internship rounds, the round name, the round number, links to future intern chats over video and text.

A FOSS community is represented by the `class Community` in `home/models.py`. It contains things like the community name.

Communities can participate in multiple Outreachy internship rounds. We record their participation in each round in with the `class Participation` in `home/models.py`. A participation includes details like who is sponsoring the Outreachy interns for this community. A participation model has a "link" (a ForeignKey) to one `Community` and one `RoundPage` object. So, for example, we could say "Debian participated the May 2019 Outreachy internship round."

The relationships described above can be represented by this diagram:

![A Participation is related to a Community and a RoundPage. A Project is related to a Participation.](https://github.com/sagesharp/outreachy-django-wagtail/raw/master/docs/graphics/RoundPage-Community-Participation-Project.png)

## ApprovalStatus class

You'll notice in the diagram above that both `class Participation` and `class Project` have `class ApprovalStatus` as a base class. The ApprovalStatus class is a way to keep track of who submitted an object, who has permissions to approve an object, and what the status of the approval is. An ApprovalStatus object can be in the pending, approved, rejected, or withdrawn state.

Outreachy coordinators sign up their community to participate in a particular Outreachy internship round. That puts the associated Participation into the pending state. Outreachy organizers then review the Participation and approve or reject it. Coordinators can withdraw their community's participation at any time. For Participation objects, coordinators are considered the submitters of the Participation, and organizers are the approvers.

Once a community signs up to participate (and even before it's approved), Outreachy mentors can submit projects. That puts the associated Project into the pending state. Coordinators then review the Project and approve or reject it. Project mentors can withdraw their project's participation at any time. For Project objects, mentors are the submitters and coordinators are the approvers.

Most classes with an ApprovalStatus will have emails sent to the submitter when they are approved, but some don't. Review the view code in `home/views.py` to see what emails are sent when the status changes.

## CoordinatorApproval class

The community coordinator role is represented by the CoordinatorApproval class. It has a foreign key to a Community, because we expect the coordinator to remain the same from round to round. New coordinators are on-boarded as people change roles, but most coordinators stick around for at least 2-4 internship rounds.

![A CoordinatorApproval has a foreign key to a Community.](https://github.com/sagesharp/outreachy-django-wagtail/raw/master/docs/graphics/Participation-Community-CoordinatorApproval-Project-MentorApproval.highlighted-CoordinatorApproval.png)

When testing the website on your local machine, it's useful to create a coordinator account that you can log into. This allows you to see how the website looks at various points in the round to a coordinator. You can create a new CoordinatorApproval object using the `home/factories.py` function `CoordinatorApprovalFactory()`.

The factory will fill in random names, phrases, and choices for any required fields in the CoordinatorApproval, Comrade, User, and Community objects. If you want to override any of those fields, you can pass that field value as an assignment in the same format you would for a [Django filter queryset](https://docs.djangoproject.com/en/1.11/topics/db/queries/#retrieving-specific-objects-with-filters).

In the example code below, we'll set the password for the coordinator so that we can log in under their account. The factories code handles hashing the password and storing the hashed password in the database. We'll also set the CoordinatorApproval approval status to approved (by default, all ApprovalStatus objects are created with the withdrawn approval status). The example sets the community name to "Really Awesome Community", but you can use the name of your favorite FOSS community instead.

```
>>> name = "Really Awesome Community"
>>> coord1 = CoordinatorApprovalFactory(coordinator__account__password="coord1", coordinator__account__username="coord1", approval_status=ApprovalStatus.APPROVED, community__name=name, community__slug=slugify(name))
>>> really_awesome_community = coord1.community
```

If you want to create a second coordinator under the same community, you can run this command:

```
>>> coord2 = CoordinatorApprovalFactory(coordinator__account__password="coord2", coordinator__account__username="coord2", approval_status=ApprovalStatus.APPROVED, community=really_awesome_community)
```

If you visit `http://localhost:8000/communities/cfp/really-awesome-community/`, you should see the randomly generated names of the coordinators. You can log in with the superuser account or one of the coordinator's accounts to see how the page changes once you log in.

## Participation and Sponsorship classes

Each community can sign up to participate in an Outreachy internship round. That sign up is represented by `class Participation`. As part of signing up to participate in Outreachy, each community must provide sponsorship for at least one intern ($6,500 USD). When a community signs up, we require the coordinator to fill out information about their sponsor names and sponsorship amounts. The sponsor information is stored in `class Sponsorship`, which has a foreign key to the Participation object.

You can use the Django shell to create a new participation. The example below assumes you already have a pre-created community that is being referenced by the variable name `really_awesome_community`, and a pre-created RoundPage `current_round`. The code also sets the approval status to say the community has been approved to participate in this round. The example sets that the community will be receiving sponsorship for two interns. We'll save a reference to that Participation object in the variable participation.

```
>>> participation = SponsorshipFactory(participation__participating_round=current_round, participation__community=really_awesome_community, participation__approval_status=ApprovalStatus.APPROVED, amount=13000).participation
```

## Project and MentorApproval classes

In Outreachy, mentors submit projects under a participating community. Mentors are in charge of defining the project description and tasks that the applicants work on during the contribution phase. Each project can have one or more mentors.

A project is represented by the `class Project` in `home/models.py`. It has a ForeignKey to a `Participation` (the representation of a community participating in an internship round).

The mentor(s) for that project are represented by the `class MentorApproval` in `home/models.py`. That provides a link between the mentor's account on Outreachy (a `Comrade` object) and the Project object. A mentor submit or co-mentor more than one project, which will create multiple MentorApproval objects.

![A MentorApproval has a foreign key to a Project.](https://github.com/sagesharp/outreachy-django-wagtail/raw/master/docs/graphics/Participation-Community-CoordinatorApproval-Project-MentorApproval.highlighted-MentorApproval-Project.png)

When testing the website on your local machine, it's useful to create a mentor account that you can log into. This allows you to see how the website looks at various points in the round to a mentor. You can create a new MentorApproval object using the `home/factories.py` function `MentorApprovalFactory()`.

The factory will fill in random names, phrases, and choices for any required fields in the Comrade, User, and Project objects. If you want to override any of those fields, you can pass that field value as an assignment in the same format you would for a [Django filter queryset](https://docs.djangoproject.com/en/1.11/topics/db/queries/#retrieving-specific-objects-with-filters).

In the example Django shell code below, we'll set the password for the mentor so that we can log in under their account. The factories code handles hashing the password and storing the hashed password in the database. We'll also set the MentorApproval approval status and the Project approval status to approved. (By default, all ApprovalStatus objects are created with the withdrawn approval status.) The code assumes you have a pre-created Participation object referenced by the variable `participation`. The code will associate the Project with that community's participation in the internship round, rather than allowing the factories code to create new Community and RoundPage objects with random values.

```
>>> mentor1 = MentorApprovalFactory(mentor__account__password="mentor1", mentor__account__username="mentor1", approval_status=ApprovalStatus.APPROVED, project__project_round=participation, project__approval_status=ApprovalStatus.APPROVED)
```

If you want to create a co-mentor under the same project, you can run these two commands:

```
>>> project = mentor1.project
>>> mentor2 = MentorApprovalFactory(mentor__account__password="mentor2", mentor__account__username="mentor2", approval_status=ApprovalStatus.APPROVED, project=project)
```

## Models for Applicants

When a person wants to apply to Outreachy, their first step is to fill out an initial application. That application is reviewed by Outreachy organizers and approved or rejected. The initial application may be automatically rejected if the person is not eligible to be paid or they have too many time commitments. The initial application must be re-submitted each internship round, because the person's time commitments and payment eligibility may change from round to round. The initial application is represented by `class ApplicantApproval`.

After the applicant's initial application is approved, their next step is to pick one or more Outreachy projects and make a contribution to it. A contribution is a small task that an applicant finds in the project's issue tracker. Once a contribution is started, the applicant can then record the contribution in the Outreachy website. The contribution form asks for the date started, completed, a URL for the contribution (typically to the issue tracker), and a description of the contribution. The recorded contribution is represented by `class Contribution`.

As the project application deadline nears, the next step is for an applicant to create a final application. The final application includes questions about the applicant's past experiences with FOSS communities, relevant projects, and a timeline of project tasks for the internship project they're applying to. The final application is represented by `class FinalApplication`.

Applicants can record many contributions for the same Project, or different projects. Applicants can submit multiple final applications to different projects. The associated Contribution and FinalApplication objects will all have foriegn keys back to the ApplicantApproval and Project objects.

If the applicant applies to another round, they have to create a new initial application (ApplicantApproval object) and new Contribution and FinalApplication objects associated with the Project they're applying for.

![Diagram showing the relationship from a RoundPage through a Project to a Contribution, then an ApplicationApproval, to a FinalApplication](https://github.com/sagesharp/outreachy-django-wagtail/raw/master/docs/graphics/RoundPage-Participation-Project-Contribution-ApplicantApproval-FinalApplication.png)

### Creating ApplicantApproval Test Objects

It can be useful to log into your local test website and see how the pages look from an applicant's perspective. The following Django shell example creates a new ApplicantApproval. It assumes you already have a pre-created RoundPage referenced by the variable `current_round`. It sets the initial application's approval status to approved. The code also ensures that the username and password is set for the applicant so you can log in.

```
>>> applicant1 = ApplicantApprovalFactory(application_round=current_round, approval_status=ApprovalStatus.APPROVED, applicant__account__username="applicant1", applicant__account__password="applicant1")
```

### Creating Contribution Test Objects

The following Django shell example creates a new Contribution object. It assumes you already have a pre-created ApplicantApproval referenced by the variable `applicant1` and a pre-created Project referenced by the variable `project`.

```
>>> ContributionFactory(project=project, applicant=applicant1, round=project.project_round.participating_round)
```

### Creating FinalApplication Test Objects

The following Django shell example creates a new FinalApplication object. It assumes you already have a pre-created ApplicantApproval referenced by the variable `applicant1` and a pre-created Project referenced by the variable `project`. It sets the FinalApplication approval status to pending.

```
>>> FinalApplicationFactory(project=project, applicant=applicant1, round=project.project_round.participating_round, approval_status=ApprovalStatus.PENDING)
```

## InternSelection and MentorRelationship classes

When the contribution period is over and the deadline has passed to submit a final application, Outreachy mentors decide which interns they want to select. As part of that process, they must sign a mentor agreement that states they understand their commitments to this internship. The signed contract for this internship with this applicant is stored in `class MentorRelationship`.

When the mentor picks an intern, that intern selection is represented by `class InternSelection`. That model stores information about the internship, such as what project the applicant will be interning with, if the intern has custom start or end dates, if the internship is approved by the Outreachy organizers, etc.

If a co-mentor for the same Project signs up to participate as a mentor for this intern, another MentorRelationship object will be created. Mentors from a different Project can select the applicant as an intern. That would create a MentorRelationship to the MentorApproval for that mentor in that other project. If mentors from two different projects select the same applicant, it shows up as an intern selection conflict on their project applicant review page, the community applicant review page, and the organizer dashboard.

The relationship between an InternSelection and a MentorRelationship is shown below:

![An InternSelection is related to a MentorApproval through a MentorRelationship](https://github.com/sagesharp/outreachy-django-wagtail/raw/master/docs/graphics/docs/graphics/MentorApproval-MentorRelationship-Project-ApplicantApproval-InternSelection.png)


# Adding a new Django app

If you have a set of Django models, views, and templates that is a discrete chunk of functionality, you may want to create a new app in the top-level directory. If we want to call our new app `contacts` we can run the helper script to set up our app:

```
./manage.py startapp contact
```

That script will stick some boilerplate examples in a new directory:

```
$ ls contacts/
admin.py  apps.py  __init__.py  migrations  models.py  tests.py  views.py
```

You may need to add a `templates` directory to that app:

```
makedir contacts/templates
```

# Dokku logs

If you've deployed to a test server with the Django debugging settings turned on, Django will send all emails to the console. If you want to create new test users, you'll need to extract the verification URL from the log. You can run:

```
ssh -t dokku@outreachy.org logs test
```

# Sentry error logging

Outreachy uses Sentry to log error messages received on both the Outreachy website and the test website. Unfortunately, that means if you ever use dokku to start the Python shell on the remote website, any typos you have end up getting reported to Sentry. To suppress those error messages, you can unset the `SENTRY_DSN` environment variable:

```
ssh -t dokku@www.outreachy.org run www env --unset=SENTRY_DSN python manage.py shell
```

# Migrations

When you change some aspect of a field in a model, that can create a change to the underlying database information. For example, if you change a field name from "foo" to "bar", the Django object database has to change such that you can quenry for objects using the new name. You can read more about migrations and how to create and apply them in the Django migrations documentation. We suggest starting with the [simple migrations introduction in the Django tutorial](https://docs.djangoproject.com/en/1.11/intro/tutorial02/#activating-models), and then looking at the [more detailed migrations documentation](https://docs.djangoproject.com/en/1.11/topics/migrations/) if needed.

In most cases, there are only two commands you need to run to create and apply a migration. The first is:

```./manage.py makemigrations```

This will examine the code changes you've made, and automatically generate a Python file that describes how the underlying database schema should change. Make sure to commit this file along with your model code changes. Then the second command you'll run is:

```./manage.py migrate```

This will apply the database schema change to your local test environment. If the Outreachy organizers push a change that includes a migration to the production or testing sites, they will need to update the server's database schema by running `ssh dokku@outreachy.org run www python manage.py migrate` or `ssh dokku@outreachy.org run test python manage.py migrate`.

The next two sections describe some of the trickier aspects of migrations that we've run into.

## Rolling back migrations

If you have migrated the database (either locally or on the server) and want to go back to a previous migration, you can run:

```
./manage.py migrate home [version number]
```

## Delicate migrations

Sometimes a field doesn't work out exactly the way you wanted it to, and you want to change the field type. In this example, we'll be changing a simple BooleanField to CharField to support three different choices. This is a dance, because we want to preserve the values in the old field to populate the contents of a new field.

1. Define the new CharField. Set 'null=True' in the argument list.

2. Run `./manage.py makemigrations && ./manage.py migrate`

3. Create an empty migration: `./manage.py makemigrations home --empty`

4. Edit the new empty migration file. You'll need to define a new function that takes `apps` and `schema_editor`, like it's documented in the `0005_populate_uuid_values.py` file in the [Django "Writing a migration" documentation.](https://docs.djangoproject.com/en/1.11/howto/writing-migrations/). You can access the objects for that Model, and set the new field based on values in the old field. Make sure to add your function to the operations list. Note that you might have to copy some class members that represent the choice short code in the database into the migration, because all migrations only have access model class members that are Django fields (like CharField or BooleanField).

5. Remove the `null=True` argument from your model, and delete the old field. You might need to remove the field from admin.py and the views. Then run `./manage.py makemigrations && ./manage.py migrate`. That will generate a third migration to make sure the field must be non-null, but the second migration will set the field on all objects. When Django prompts you about changing a nullable field to a non-nullable field, choose 'Ignore for now'.

6. The third migration will fail if someone has added a new model object between the second migration and the third migration. In this case, you should roll back to the first migration (where you first added the field). You can pass the migration number to go back to: `./manage.py migrate home PREFIX` This should be a unique prefix (like the first four numbers of the migration). Then you can try to run the migration again: `./manage.py migrate`. Repeat as necessary.

# Why Django?

We evaluated a couple different choices:
 - CiviCRM
 - Wordpress
 - Red Hen
 - Django

CiviCRM proved too clunky to use, and ultimately their data model didn't necessarily fit our data models. Wordpress might have been fine with a template plugin and would have good user experience, but with everything we wanted to do, we felt we would ultimately outgrow Wordpress.

There are other proprietary tools for tracking sponsorship information, but since Outreachy is a project under the Software Freedom Conservancy and the Outreachy organizers believe in the power of free and open source, we have decided not to use proprietary software wherever possible.

Django fit our needs for flexibility, data model definition, and future use cases. However, the Django admin interface is pretty clunky and intimidating. We wanted to have a very easy way for all our organizers to quickly edit content. The Wagtail CMS plugin provides a nice user interface and template system, while still allowing programmers to fully use Django to implement models. It also provides internal revision tracking for page content, which means we can easily roll back content changes from the wagtail admin web interface if necessary.
