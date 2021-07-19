
# QA_Project_1 ZMR

Please ignore spelling, spelling error correction isnt working on VSCODE :)
If anything doesnt make sense please leave a comment and ill get to fixing it!

## Table of contents:
- What this projectis
- Scope of the project
    - MVP
    - Personal goals
- Design specification
    - Outline
    - Tree structure
    - Database ERD
- Risk assesment
- Trello Board
- Testing
- Pipeline overview
- Changes as the project has progressed
- What I would do better
- Goals met
- Notes to build


## What this project is
This project is a demonstration of using backend services, containerizing them and deployign them across a docker swarm. This allows for scalability of the application and allows it to grow as demand increses. I picked a simple portal 2 core generator that geenrates a few random attributes, applies some logic and then returns a simple string.

## Scope of the projects
### MVP
There are a few basic requirements this project must hit, they are as followed:
- A Trello board
- At least one database
- A HTML front end
- 4 Services to run in the background
- Self testing python to be run during each build
- Automatic configuration with Ansible
- Automatic deployment using Jenkins
- Usage of VCS (GIT)
- Usage of reverse proxy

### Personal Goals
I am finding this project very difficult so i would be satisfied if i could atleast write the code for the program to work even if it might not even work


## Design specification

### Outline

The most important structure to this program will be the backend, there must be services in containers in the backend that can be deployed across a swarm. This means they must be able to be configured in a way they can speak to eachother and not cause conflicts. See below a design diagram of how the service will work:

![Service Breakdown](https://i.imgur.com/Bf1Gd7Z.png)

## Risk assesment

As with any web application there is always some threat to the application and/or the data it contains. See below for a breakdown of risks assocated and remidies that can be put in place to negate any risks.

| Risk        | Likleyhood | Impact | Description  | Evaluation | Response | Control Measure | New Likelyhood | New Impact |
| :---------- | :--------: | :----: | :----------- | :--------- | :------- | :-------------- | :------------: | :--------: | 
|Too many users could be trying to use your cloud service|2|3|There could be an overwhelming amount of real or fake users trying to access your service or an increased number of processes running|Your entire service could stop working and might lead to errors for other users, it might also overwhelm the cloud service and disrupt other people operations|Service may need to be restricted if this occurs, it will ruin the end user experience|Using docker swarm you can add more worker nodes in VM's to handle the extra traffic|1|1|
|You release an unstable or broken build|1|3|You may accidentally merge the unstable and stable release branch or unstable code might make it onto the release version|Users might have a bad end experience, buisness may be lost to yourself and to the client|You will need to revert to the latest stable branch|Ensure there are clear rules in place to differentiate between release builds and internal builds, Ensure that testing is thorough and tests every element of the version before release|1|2|
|Data loss that is integeral to function occurs|1|3|You may loose hardware or simply forget data that is key to the program being used, it could be accidentally deleted|The service would be out of operation until the orignal data could be recovered|You would either need to impliment a patch around the data or source new data|Ensure any vital data is backed-up, this may be on the cloud or physically. Using a VCS is a very good measure as it allows you to rollback easily|1|2|
|A first or third party could release important data such as passwords|2|3|A disgruntled employee, yourself or someone else might accidentally or maliciously release senitive information that allows unauthorised users to view sensitive content|Code could be stolen or important information could be leaked|Code would need to be changed, Passwords would need to be changed and re-distributed|Ensure employees are given the relevant access and not overall access, Ensure any important information is stored securley so if its leaked its harder to decode, Use 2FA To secure sensitive info so its not imediatly accesible|1|1|
|Connection to the database is lost|1|3|For whatever reason the connection to the database might be lost|The service will stop working functionally but the website will still be live|A new connection needs to be re-established or a backup of the database needs to be made|Ensure there is a fallback option, also ensure a repulatable cloud service is used. Ensure the used service allows for expansion |1|1|

## Git board
I will be using a GIT Project board to track my project, it can be found on the git page

## Testing

TBA

## Pipeline Overview

TBA

## Changes as the project has progressed

I have written all the files to deploy my application across a swarm however it isnt working, its something thats still to be fixed however.

## What I would do better

- I would manage my time and stick to my project tracking board better

## Goals met

I have met the following goals:

- Working Backend

- Working Database

- Ability to deploy in docker swarm

- Ability to pipeline with Jenkinsfile

- Ability to use ansible

## Notes to build

N/A