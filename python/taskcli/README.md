# TaskCLI / Task Tracker
https://roadmap.sh/projects/task-tracker

## Description
This is a simple task tracker tool made in Python that allows you, the user, to add, delete, update, list, and mark tasks easily.

## Installation
This is a pretty simple tool so it doesn't require installation, just go to command prompt and navigate to the folder you downloaded the python file in `eg: C:\Users\User\GitHubDownloads`

After that, you can start using the tracker in the command prompt.

## Usage
As said before, you must navigate to the folder that you downloaded the python file in the command prompt to start typing in commands.
### Adding a Task
**To add a task, type in:**
`taskcli add "{task-description}"`
> Example: `taskcli add "prepare for school"`

It will then show you that the task has been created, as well as the created task's ID and status, and the current tasklist.

**NOTE:**

> When doing future operations with tasks after you have created it such as deleting, updating, or marking the task, refer to its ID rather than the name/description of the task.

### Deleting a task
**To delete a task, type in:**
`taskcli delete {task-id}`
> Example: `taskcli delete 3`

This will then show you that the task with that ID has been deleted, as well as the current tasklist.

### Updating a task's description
**To update a task, type in:**
`taskcli update {task-id} "{updated-description}"`
> Example: `taskcli update 1 "play ultrakill"`

This will update the task's description and show the updated tasklist.
### Marking a task as todo/in-progress/done
**To mark a task as todo/in-progress/done, type this:**
`taskcli mark {task-id} {todo/in-progress/done}`
> Example: `taskcli mark 4 in-progress`

This will update the status of that task's ID to either todo/in-progress/done depending on what you typed in, and will also show the updated tasklist.

**NOTE:**

**You can put the task-id as "everything" to mark every task as todo/in-progress/done:**

> **Example: `taskcli mark everything done`**

### Listing the tasklist
**To list the tasklist, type in:**
`taskcli list`

This will show every task regardless of status.

Additionally, you can put in todo/in-progress/done to list every task that has that particular status.
> Example: `taskcli list done`

This will show every task that has the status of "done"
### Clearing the tasklist
**To clear the tasklist, type in:**
`tasklist clear`

This will clear every task in the tasklist.
