# Gradebook Program

## Project Scope
This program was written to fulfill a Lab 4 assignment for the course *COSC 1336: Fundamentals of Programming*. Lab 4 corresponds to Learning Module 4, which introduces the repetitive structures `while` and `for` loops. Students were instructed to create a simple program that would receive multiple grades for an unspecified number of students, calculate numerical averages and letter grades, as well as display a final class average.

~~Honestly, this was very boring, so~~ I went out of my way to add data validation to the grade input so that negative values would not be allowed. I didn't cap the possible grade value in case teachers wanted to offer extra credit. I also added stats for the class by letter grade, and added a warning to the teacher if there were students for which they had not yet input grades.

### Limitations
Because Learning 4 introduces very basic Python skills, the intial version of this program was intentionally designed to use simple statements and have limited functionality. For example, no data validation was required. Requiring the use of a sentinel value rather than asking the user to simply input *y* or *n* to keep running was also not the best solution for this program, as it necessitated adjusting the totals and counts before calculating averages.

### Future Plans
As my Python skills progress, I may revisit this program and continue to expand its functionality past the requirements of the lab assignments. Higher-level goals for this program include displaying all student data together at the end in a spreadsheet-type format, building some kind of GUI, adding the capability to sync to a student roster rather than inputting each name each time, and syncing the grade input to the assignments on a syllabus so it's apparent what assignment each of these scores are for.

## Set Up
Because *COSC 1336: Fundamentals of Programming* is an introductory course to programming, the program was written using Python only, and is meant to be run from the terminal without any further set up required.

## Repo File Descriptions
- Lab 4 entails using repetitive strutures and a sentinel to create a simple gradebook tool which holds student grades and averages ([Lab_4_instructions.pdf](https://github.com/emnharris/COSC-1336/blob/master/gradeook_program/Lab_4_instructions.pdf)).
- The conversion program itself has been committed as one file ([gradebook_program.py](https://github.com/emnharris/COSC-1336/blob/master/gradebook_program/gradebook_program.py)).
