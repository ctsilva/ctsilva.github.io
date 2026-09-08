---
title: "DS-GA 3001: Visualization for Machine Learning - Fall 2026 Syllabus"
permalink: /2026-VisML-CDS/syllabus
author_profile: true
---

⚠️ **Work in progress:** This syllabus is **tentative** and is being actively updated ahead of and during the semester. Students will be notified of any changes via course announcements and Discord.

# Special Topics in Data Science: Visualization for Machine Learning

# Fall 2026

**Instructor:** Claudio Silva (csilva@nyu.edu); [webpage](https://ctsilva.github.io)

**Session Leader (labs):** Bhavya Matam (bm3792@nyu.edu)

**Grader:** Bhavya Matam (bm3792@nyu.edu)

**Instruction Mode:** In-Person

**Dates:** Fall 2026 (September 8 - December 8, 2026)

**Meeting Times:**

DS-GA 3001.001 (Lecture)  
Tuesdays 4:55 PM - 6:55 PM  
Classroom: 60 Fifth Avenue, Room 150, Washington Square Campus

DS-GA 3001.002 (Lab)  
Tuesdays 7:10 PM - 8:00 PM  
Classroom: 60 Fifth Avenue, Room 150, Washington Square Campus

Both sections meet on the same evening in the same room: the lecture runs 4:55-6:55 PM, and after a short break the lab runs 7:10-8:00 PM and reinforces that week's material with hands-on work. The first class is Tuesday, September 8.

**Important Dates:**
- All 14 Tuesday sessions meet as scheduled. Labor Day (Sept 7) and Fall Break (Oct 12) both fall on Mondays, and Thanksgiving Recess (Nov 26-27) on Thursday-Friday, so this course loses no meetings.
- First class September 8; last class December 8

**Class Discord:** Invite link to be posted before the first class

## Course Prerequisites

You should have solid programming expertise, of the level expected from a first-year graduate student in computer science or data science.

The coursework includes extensive programming with JavaScript, the D3.js library, and web technologies (CSS, SVG, etc.). While previous knowledge of these technologies is not required, being proficient and comfortable with extensive programming is a fundamental prerequisite for this course. If you are not comfortable with programming please contact the instructor before enrolling.

We will also expect students to be able to program in Python.

We expect that you have a solid foundation in *either* data visualization or machine learning. If you have no knowledge of machine learning, this course might not be appropriate for you.

## Course Description 

The material for this course is part of a fast-changing field of computing. It is a research-oriented course on topics related to visualization for machine learning, and all students will be expected to work on a guided research project.

Our course is based on foundations of visual analytics, which is an area of data visualization that is concerned with improving a human analytic process, or how one makes sense of data for a given problem: understanding, reasoning, and making decisions about a provided dataset, and a given problem domain. Visual analytics is concerned with combining automated processes with human-driven processes that are built around data visualization: visual representations of data, and ways to interact with data. Given the rapid growth in machine learning in the last decade, research in visual analytics has witnessed similar growth in leveraging machine learning in a variety of ways.

## Course History

This course started as a variation of the Visual Analytics and Machine Learning course designed by Professor Matthew Berger (Vanderbilt University). We first offered it at Tandon CSE on Spring 2020.

For the second offering in Spring 2021, the content of the course was updated quite substantially, in particular with more practical material aimed at enabling students to experience data analysis tasks through visualization.

The course offered in Spring 2022 was a further refinement of the material. Borrowing ideas from Professor Chris Manning (Stanford) in his course Natural Language Processing with Deep Learning, we provided *default* projects to help those students that are not already engaged in research. Also, we limited the assignments to the first part of the course before the project-related deadlines start.

The Spring 2023 was based on the Spring 2022 course, with updated materials and lectures.

The Spring 2024 offering was taught at NYU CDS as DS-GA 3001, with further refinements and updates.

The Fall 2025 offering marked the return of this course to NYU Tandon as CS-GY 9223.

**Fall 2026** brings the course back to NYU CDS as DS-GA 3001, incorporating lessons learned from all previous offerings.

### Acknowledgments

The development of this course has been a collaborative effort. Many members of our research group have contributed to creating materials over the years, including João Rulff, Erin McGowan, Vitória Guardieiro, Peter Xenopoulos, Jorge Piazentin Ono, and Guande Wu. Their contributions have been instrumental in shaping this course into its current form.

## Course Objectives 

This course is designed to sharpen a student's knowledge of visualization and machine learning, and how the two areas interact. It is expected that the student will be a more effective data scientist by being fluent on the connections between the two areas. It is also designed around a major project, which will help the student develop research skills.

### Learning Objectives

By the end of this course, students will be able to:

1. **Understand** the role of visualization in the machine learning pipeline
2. **Design** effective visualizations for different types of ML models and data
3. **Implement** interactive visualization systems using D3.js and modern web technologies
4. **Evaluate** ML models through visual analytics
5. **Create** visual explanations for complex ML systems
6. **Critique** existing visualization approaches for ML
7. **Develop** novel visualization techniques for emerging ML challenges

## Course Structure 

The course meets once a week, in two back-to-back sessions on Tuesday evening: a 2-hour lecture (4:55-6:55 PM) followed by a 50-minute lab (7:10-8:00 PM) in the same room. The lab is a hands-on programming session that complements the theoretical material from the lecture that precedes it.

The course starts with a short primer on visualization. We will introduce machine learning concepts as they are needed in the class. We will cover visualizations for model assessment, white-box and black-box machine learning explainers. After that, we will continue with dimensionality reduction (clustering) techniques (e.g., PCA, t-SNE, UMAP).

After this initial set of lectures, we will continue with more advanced and specialized topics. We will cover Topological Data Analysis, followed by multiple lectures on visualizing deep neural networks.

## Reading Material

There is no textbook for the course - most lectures will be based on recent technical papers, which have not yet been incorporated into textbooks. We will have suggested reading materials for each class. It is expected that, prior to the lecture, you have read the corresponding papers.

Here are supplemental readings to be used as reference material:

1. Data Visualization Curriculum, Jeff Heer, [link](https://observablehq.com/@uwdata/data-visualization-curriculum)
2. A Course in Machine Learning, Hal Daumé III, [link](http://ciml.info/dl/v0_99/ciml-v0_99-all.pdf)
3. Interpretable Machine Learning: A Guide for Making Black Box Models Explainable, Christoph Molnar, [link](https://christophm.github.io/interpretable-ml-book/)
4. Introduction to Machine Learning, Etienne Bernard, [link](https://www.wolfram.com/language/introduction-machine-learning/)
5. Deep Learning, Ian Goodfellow, Yoshua Bengio and Aaron Courville, MIT Press, 2016 [link](http://www.deeplearningbook.org/)
6. Understanding Deep Learning, Simon J.D. Prince, MIT Press, 2023 [link](https://udlbook.github.io/udlbook/)

## Research Project

This course includes a substantial research project. Please see the project section of the course for more details. As part of the project, you will be expected to reproduce prior work or implement a proposed research idea of your choosing (requirement details will be forthcoming and discussed in class). Moreover, you will be expected to demonstrate both the prior work, and your final research project, to the class during lectures. Projects are expected to be pursued in groups of 2-3, although you can optionally pursue your project by yourself. Once the group is finalized, students cannot change or separate their groups throughout the semester.

## Course Assessment

* **Assignments:** 50%
* **Project Proposal** (4-page writeup): 10%
* **Project Updates** (1-page writeup): 10%
* **Full Project** (8-page writeup): 25%
* **Class Participation:** 5%

### Assignment Schedule

Weekly programming assignments will be given for the first half of the semester, focusing on implementing visualization techniques for ML. These assignments are designed to build the technical skills needed for the final project.

### Project Timeline

- **Week 2 (Sept 15):** Team formation
- **Week 4 (Sept 29):** Project proposal due (4 pages)
- **Week 7 (Oct 20):** Mid-term project update due (1 page)
- **Weeks 13-14 (Dec 1 & 8):** Final project presentations
- **December 14:** Final project report due (8 pages)

## Late Submissions

Late submissions of assignments will be penalized as follows:
- A standard deduction rate of 20% per day.

It means that after 5 days of being late, your assignment will have a maximum grade of 0 (zero).

## Course Schedule (tentative)

The course schedule is tentative and might need to be adjusted along the way. See the [detailed schedule](/2026-VisML-CDS/schedule) for readings and lab topics.

| Week | Date (Tue) | Topic |
|------|------------|-------|
| 1 | Sept 8 | Introduction to Visualization for Machine Learning |
| 2 | Sept 15 | Perception and Color Theory |
| 3 | Sept 22 | Model Assessment and Performance Metrics |
| 4 | Sept 29 | White-box Model Visualization |
| 5 | Oct 6 | Black-box Model Interpretation & Project Discussion |
| 6 | Oct 13 | Clustering Visualization |
| 7 | Oct 20 | Dimensionality Reduction |
| 8 | Oct 27 | Deep Learning Visualization |
| 9 | Nov 3 | NLP and Large Language Model Visualization |
| 10 | Nov 10 | Topological Data Analysis |
| 11 | Nov 17 | Time Series and Streaming Data |
| 12 | Nov 24 | Interpretable ML and Fairness |
| 13 | Dec 1 | Project Presentations I |
| 14 | Dec 8 | Project Presentations II and Wrap-up |

## Software Requirements

- Modern web browser (Chrome/Firefox recommended)
- Text editor or IDE (VS Code recommended)
- Python 3.8+ with standard ML libraries (NumPy, Pandas, Scikit-learn, etc.)
- Node.js for JavaScript development
- Git for version control

## Moses Center Statement of Disability

If you are a student with a disability who is requesting accommodations, please contact New York University's Moses Center for Students with Disabilities (CSD) at 212-998-4980 or mosescsd@nyu.edu. You must be registered with CSD to receive accommodations. Information about the Moses Center can be found at www.nyu.edu/csd. The Moses Center is located at 726 Broadway on the 3rd floor.

## Academic Integrity

All students are expected to do their own work. Students may discuss assignments with each other, as well as with the course staff. Any discussion with others must be noted on a student's submitted assignment. Excessive collaboration (i.e., beyond discussing the assignment) will be considered a violation of academic integrity. Questions regarding acceptable collaboration should be directed to the class instructor prior to the collaboration. It is a violation of the honor code to copy or derive solutions from other students (or anyone at all), textbooks, previous instances of this course, or other courses covering the same topics. Copying solutions from other students, or from students who previously took a similar course, is also clearly a violation of the honor code. Finally, a good point to keep in mind is that you must be able to explain and/or re-derive anything that you submit. This is particularly important if you should adapt solutions from online sources.

Here is a [link to the GSAS statement on Academic Integrity](https://gsas.nyu.edu/about-gsas/policies-and-procedures/gsas-statement-on-academic-integrity.html).

## AI Policy

We live in the age of viable generative AI. Banning these tools is neither realistic, nor desirable. In fact, learning to use these tools is an emerging skill. Note that AI tools do not always produce correct or accurate results. In addition, it is unwise to rely on them too much. There are situations where you won't have access to these tools, for instance during technical interviews. In addition, there are also skills someone with an advanced degree in Data Science is just expected to have on tap - without AI assistance or looking anything up. To integrate both considerations, you can use generative AI tools to do the assignments in this class. If you use an AI to guide you in completing an assignment, you have to disclose which parts were generated by the AI.

## NYU Academic Calendar

[Link to NYU Academic Calendar](https://www.nyu.edu/students/student-information-and-resources/registration-records-and-graduation/academic-calendar.html?semester=Fall%202026)

This course does not have a final exam.

Also, please pay attention to notable dates such as Add/Drop, Withdrawal, etc.

## Important Dates

- **Sept 8:** First Class (lecture and lab)
- **Sept 15:** Add/drop deadline for full-semester classes (after this date, dropping results in a W)
- **Nov 25:** Deadline to withdraw from classes and to request the pass/fail option
- **Nov 26-27:** Thanksgiving Recess - No Classes (Thursday-Friday; our Tuesday sessions are unaffected)
- **Dec 8:** Last Class (lecture and lab)
- **Dec 14:** Final Project Reports Due
- **Dec 15:** Reading Day - no classes or required meetings
- **Exam week:** No final exam is held for this course

## Contact Information

**Course Website:** [https://ctsilva.github.io/2026-VisML-CDS/](https://ctsilva.github.io/2026-VisML-CDS/)

**Discord:** Invite link to be posted before the first class (primary communication channel)

**Email:** For private matters only

**Office Hours:** Fridays 1:30-2:30 PM, 370 Jay Street, Room 1153

---

*This syllabus is subject to change. Students will be notified of any modifications.*