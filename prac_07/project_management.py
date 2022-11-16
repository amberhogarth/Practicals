"""
CP1404 Practical 7 - Project Management
Estimated time: 1hr 30mins
Actual time: 2hr 10mins
"""

from datetime import date, datetime
from prac_07.project import Project
from operator import attrgetter

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new " \
       "project\n- (U)pdate project\n- (Q)uit "


def main():
    projects = load_projects("projects.txt")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            projects = load_projects(filename)
            print(MENU)
            choice = input(">>> ").upper()
        elif choice == "S":
            save_filename = input("Filename to save projects in: ")
            save_projects(projects, save_filename)
            print(MENU)
            choice = input(">>> ").upper()
        elif choice == "D":
            projects.sort(key=attrgetter("priority"))
            print_incomplete_projects(projects)
            print_completed_projects(projects)
            print(MENU)
            choice = input(">>> ").upper()
        elif choice == "F":
            filter_by_date(projects)
            print(MENU)
            choice = input(">>> ").upper()
        elif choice == "A":
            add_new_project(projects)
            print(MENU)
            choice = input(">>> ").upper()
        elif choice == "U":
            update_project(projects)
            print(MENU)
            choice = input(">>> ").upper()


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    new_completion = int(input("New percentage: "))
    new_priority = int(input("New priority: "))
    projects[project_choice].completion = new_completion
    projects[project_choice].priority = new_priority


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost Estimate: $"))
    percent_complete = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(new_project)


def save_projects(projects, save_filename):
    out_file = open(save_filename, "w")
    for project in projects:
        print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t"
              f"{project.completion}", file=out_file, end="\n")


def filter_by_date(projects):
    chosen_date = input("Show projects that start after date (dd/mm/yy): ")
    chosen_date = datetime.strptime(chosen_date, "%d/%m/%Y").date()
    for project in projects:
        if project.start_date > chosen_date:
            print(project)


def print_completed_projects(projects):
    print("Completed projects:")
    for project in projects:
        if project.is_complete():
            print(project)


def print_incomplete_projects(projects):
    print("Incomplete projects:")
    for project in projects:
        if not project.is_complete():
            print(project)


def load_projects(filename):
    projects = []
    in_file = open(filename, "r")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split("\t")
        project = Project(parts[0], parts[1], parts[2], parts[3], int(parts[4]))
        projects.append(project)
    return projects


main()
