document.addEventListener('DOMContentLoaded', function() {
    const addTaskBtn = document.getElementById('add-task-btn');
    const taskTitleInput = document.getElementById('task-title');
    const taskDescInput = document.getElementById('task-desc');
    const taskDueDateInput = document.getElementById('task-due-date');
    const taskList = document.getElementById('task-list');

    addTaskBtn.addEventListener('click', addTask);

    function addTask() {
        const title = taskTitleInput.value;
        const description = taskDescInput.value;
        const dueDate = taskDueDateInput.value;

        if (title === '' || description === '' || dueDate === '') {
            alert('Please fill in all fields');
            return;
        }

        const taskItem = document.createElement('div');
        taskItem.className = 'task-item';

        taskItem.innerHTML = `
            <h3>${title}</h3>
            <p>${description}</p>
            <p><strong>Due:</strong> ${dueDate}</p>
            <div class="task-actions">
                <button class="edit-btn">Edit</button>
                <button class="delete-btn">Delete</button>
            </div>
        `;

        taskList.appendChild(taskItem);

        taskTitleInput.value = '';
        taskDescInput.value = '';
        taskDueDateInput.value = '';

        const editBtn = taskItem.querySelector('.edit-btn');
        const deleteBtn = taskItem.querySelector('.delete-btn');

        editBtn.addEventListener('click', () => editTask(taskItem));
        deleteBtn.addEventListener('click', () => deleteTask(taskItem));
    }

    function editTask(taskItem) {
        const title = taskItem.querySelector('h3').innerText;
        const description = taskItem.querySelector('p').innerText;
        const dueDate = taskItem.querySelector('p strong').nextSibling.nodeValue.trim();

        taskTitleInput.value = title;
        taskDescInput.value = description;
        taskDueDateInput.value = dueDate;

        taskList.removeChild(taskItem);
    }

    function deleteTask(taskItem) {
        taskList.removeChild(taskItem);
    }
});