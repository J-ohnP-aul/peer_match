# SOFTWARE REQUIREMENTS SPECIFICATION (SRS)

## Student Study Partner Matching System

**Version:** 1.0
**Scope:** Minimum Viable Product (MVP)
**System Type:** Web-based Application

---

# 1. Introduction

## 1.1 Purpose

The Student Study Partner Matching System is a web-based platform designed to help university students find suitable study partners and study groups based on their academic interests, courses, skills, study preferences, and availability.

The system will provide students with personalized study-partner recommendations and allow them to connect and form study groups.

This SRS defines the functional and non-functional requirements for the **Minimum Viable Product (MVP)**.

---

## 1.2 Problem Statement

University students often have difficulty finding suitable study partners who share similar courses, academic interests, learning goals, or compatible study schedules.

Students may know many people on campus but still struggle to identify individuals who are interested in studying the same subjects or who have complementary skills.

The proposed system addresses this problem by providing a centralized platform where students can create academic profiles and receive recommendations for compatible study partners.

---

## 1.3 Objectives

The main objectives of the MVP are to:

* Allow students to create academic profiles.
* Allow students to specify their courses, interests, skills, and study preferences.
* Identify students with similar or complementary academic interests.
* Recommend suitable study partners.
* Allow students to connect with recommended students.
* Allow connected students to create study groups.
* Provide a simple way of organizing study sessions.

---

## 1.4 Scope

### Included in the MVP

The system will provide:

* Student registration and authentication.
* Student profile management.
* Academic information management.
* Unit/course selection.
* Interest and skill selection.
* Study preference management.
* Student matching.
* Match compatibility scores.
* Student recommendations.
* Connection requests.
* Study group creation.
* Basic study-session scheduling.

### Outside the MVP

The following features will not be required in the initial version:

* Video conferencing.
* Online examinations.
* AI-generated study materials.
* Advanced chat/messaging.
* Payment processing.
* Integration with university systems.
* Attendance tracking.
* Advanced machine-learning personalization.
* Mobile application.

These features may be considered for future versions.

---

# 2. Overall Description

## 2.1 Product Perspective

The system will operate as a standalone web application.

A simplified architecture is:

**Frontend → Backend API → Database → Matching Engine**

The frontend will provide the user interface through which students interact with the system.

The backend will handle authentication, profiles, connections, groups, and other business logic.

The database will store student and system information.

The matching engine will calculate compatibility between students and generate recommendations.

---

## 2.2 User Classes

### Student

The primary user of the system.

A student can:

* Register and log in.
* Create and edit their profile.
* Add units and interests.
* Specify skills and study preferences.
* View recommended study partners.
* Send and receive connection requests.
* Create or join study groups.
* Organize study sessions.

### Administrator

The administrator manages the platform.

An administrator can:

* Manage student accounts.
* Manage academic units.
* Manage interests/categories.
* Manage reported users or inappropriate content.
* Monitor system activity.

---

# 3. Functional Requirements

## FR-01: User Registration

The system shall allow students to create an account.

The registration form shall collect:

* Full name
* Email address
* Password
* University/program
* Year of study

The system shall validate the submitted information before creating the account.

---

## FR-02: User Authentication

The system shall allow registered students to:

* Log in.
* Log out.
* Reset their password.

Only authenticated users shall access protected student features.

---

## FR-03: Student Profile

The system shall allow students to create and update their academic profile.

The profile shall contain:

* Name
* Profile picture (optional)
* Program/course
* Year of study
* Units
* Academic interests
* Skills
* Learning goals
* Preferred study method
* Preferred study times

---

## FR-04: Unit Management

Students shall be able to select the academic units they are currently studying.

The system shall store the selected units and use them when calculating compatibility.

---

## FR-05: Interest and Skill Management

Students shall be able to select their academic interests and skills.

Examples include:

* Programming
* Mathematics
* Database Systems
* Artificial Intelligence
* Web Development
* Networking
* Business
* Research

The system shall use this information when generating recommendations.

---

## FR-06: Study Preferences

Students shall be able to specify their preferred study conditions.

Examples include:

* Individual study
* Pair study
* Small group
* Large group

Students may also specify preferred study times, such as:

* Morning
* Afternoon
* Evening
* Weekends

---

## FR-07: Student Matching

The system shall compare student profiles and calculate a compatibility score.

The matching system may consider:

* Shared units
* Shared interests
* Complementary skills
* Study preferences
* Availability
* Year/program

Example:

> **John — 87% compatible**

Reasons:

* 3 shared units
* 2 shared interests
* Compatible study times
* Complementary programming skills

---

## FR-08: Recommended Students

The system shall display a list of recommended study partners.

Each recommendation shall display:

* Student name
* Program/year
* Shared interests or units
* Compatibility percentage
* Relevant compatibility reasons

The student shall be able to view the recommended student's profile.

---

## FR-09: Connection Requests

Students shall be able to send connection requests to recommended students.

The recipient shall be able to:

* Accept the request.
* Reject the request.

The system shall maintain the connection status.

---

## FR-10: Study Groups

Connected students shall be able to create study groups.

A study group shall contain:

* Group name
* Unit/topic
* Description
* Creator
* Members
* Maximum number of members (optional)

The creator shall be able to invite connected students.

---

## FR-11: Study Sessions

Study groups shall be able to create basic study sessions.

A study session shall contain:

* Date
* Time
* Location or meeting link
* Topic/unit
* Description

Group members shall be able to view upcoming sessions.

---

## FR-12: Notifications

The system shall notify students about important events such as:

* New connection requests.
* Accepted connection requests.
* Study-group invitations.
* New study sessions.

---

## FR-13: Profile Privacy

Students shall have control over information displayed to other students.

Sensitive account information such as passwords shall never be publicly displayed.

---

## FR-14: Administration

Administrators shall be able to:

* View registered students.
* Disable or remove accounts.
* Add or remove academic units.
* Manage interest categories.
* Manage reported accounts.

---

# 4. Matching Algorithm

The MVP shall initially use a **simple compatibility-based matching algorithm** rather than a complex machine-learning model.

A possible scoring model is:

| Factor               | Weight |
| -------------------- | -----: |
| Shared Units         |    30% |
| Shared Interests     |    25% |
| Study Availability   |    20% |
| Complementary Skills |    15% |
| Study Preferences    |    10% |

The system shall calculate a compatibility score between 0% and 100%.

For example:

**Student A and Student B**

* Shared units: 90%
* Shared interests: 80%
* Availability: 70%
* Skills compatibility: 80%
* Study preference: 90%

The system combines these values according to the defined weights to produce the final compatibility score.

### Future enhancement

The matching engine may later be upgraded to use machine-learning techniques such as:

* K-Nearest Neighbors (KNN)
* Recommendation systems
* Collaborative filtering
* Behavioral analysis


---

# 5. Non-Functional Requirements

## NFR-01: Performance

The system should respond to normal user requests within approximately 2–3 seconds under normal university-scale usage.

---

## NFR-02: Security
The system shall:

* Hash user passwords.
* Require authentication for protected resources.
* Validate user input.
* Prevent unauthorized access to user data.
* Use secure communication through HTTPS in production.

---

## NFR-03: Usability

The interface shall:

* Be simple and easy to understand.
* Be responsive on desktop and mobile browsers.
* Use clear navigation.
* Provide meaningful error messages.

---

## NFR-04: Reliability

The system should remain available during normal operating conditions and should handle invalid user input without crashing.

---

## NFR-05: Scalability

The system architecture should allow additional students, groups, units, and features to be added without requiring a complete redesign.

---

## NFR-06: Maintainability

The application should use a modular architecture so that components such as authentication, profiles, matching, and groups can be maintained independently.

---

# 6. Data Requirements

The main entities in the MVP will include:

### Student

* student_id
* name
* email
* password
* program
* year_of_study
* profile_picture

### Unit

* unit_id
* unit_code
* unit_name

### Interest

* interest_id
* name

### Skill

* skill_id
* name

### StudentUnit

* student_id
* unit_id

### StudentInterest

* student_id
* interest_id

### StudentSkill

* student_id
* skill_id

### Connection

* connection_id
* sender
* receiver
* status
* created_at

### StudyGroup

* group_id
* name
* description
* unit/topic
* creator
* created_at

### GroupMember

* group_id
* student_id
* joined_at

### StudySession

* session_id
* group_id
* date
* time
* location
* topic

---

# 7. Basic System Workflow

## Student Registration

**Student → Register → Create Profile → Select Units/Interests/Skills → Set Preferences → Dashboard**

## Finding Study Partners

**Student → Find Study Partners → Matching Engine → Calculate Compatibility → Display Recommendations**

## Connecting

**Student → View Recommendation → Send Request → Other Student Accepts → Connection Created**

## Creating a Study Group

**Connected Student → Create Group → Select Topic/Unit → Invite Students → Group Created**

## Organizing a Session

**Group → Create Study Session → Set Date/Time/Location → Members View Session**

---

# 8. MVP User Stories

### Account

> As a student, I want to create an account so that I can use the platform.

### Profile

> As a student, I want to create an academic profile so that other students can understand my study interests.

### Matching

> As a student, I want the system to recommend compatible students so that I can find suitable study partners.

### Compatibility

> As a student, I want to see why someone is recommended to me so that I can decide whether to connect with them.

### Connection

> As a student, I want to send a connection request so that I can connect with a potential study partner.

### Groups

> As a student, I want to create a study group so that several students can study together.

### Sessions

> As a group member, I want to schedule a study session so that members know when and where to meet.

---

# 9. MVP Success Criteria

The MVP will be considered successful if a student can complete the following journey:

**Register → Create Profile → Select Units & Interests → Receive Matches → View Compatibility → Connect → Create/Join Study Group → Schedule Study Session**

The system should demonstrate that students can be matched based on meaningful academic characteristics rather than simply being shown a random list of users.

---

# 10. Suggested Technology Stack

### Frontend

* React
* HTML/CSS
* JavaScript
* Bootstrap or Tailwind CSS

### Backend

* Django
* Django REST Framework

### Database

* PostgreSQL for production
* SQLite for initial development

### Matching Engine

* Python
* Rule-based compatibility algorithm for MVP
* Scikit-learn/KNN as a future enhancement

### Deployment

* Frontend: Vercel or similar platform
* Backend: Render/Railway or similar platform
* Database: PostgreSQL hosting

---

# 11. Future Enhancements

After validating the MVP, future versions could introduce:

* AI-powered study-partner recommendations.
* KNN-based matching.
* Group recommendations.
* Real-time messaging.
* Video study rooms.
* Shared notes and documents.
* Study progress tracking.
* Calendar integration.
* University timetable integration.
* Peer tutoring.
* Skill exchange.
* Reputation/rating system.
* Mobile application.
* Notifications through email or WhatsApp.

---

# 12. Conclusion

The Student Study Partner Matching System will provide a focused solution to the problem of students struggling to find suitable academic peers.

The MVP will concentrate on the core functionality: **creating academic profiles, matching compatible students, facilitating connections, forming study groups, and organizing study sessions.**

The initial matching algorithm will remain simple and explainable, allowing the project to be implemented and tested efficiently while providing a foundation for future AI and machine-learning improvements.
