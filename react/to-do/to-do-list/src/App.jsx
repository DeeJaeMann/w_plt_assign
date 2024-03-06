import { useState } from 'react'
import tasksData from './data/tasks.json'
import './App.css'

function App() {

  const[tasks, setTasks] = useState(tasksData);

  // console.log(`tasks data: ${tasksData}`)
  // console.log(`tasks state: ${tasks}`)

  const renderTask = (task) => {
    return `ID: ${task.id}, ${task.description} Completed: ${task.completed ? "Yes" : "No"}`;
  }

  const maxValueFromId = (tasks) => {
    const theseIds = tasks.id;

    console.log(theseIds)

    // return arrIds
  }

  const addTask = () => {
    // get the max value from key id and add 1
    // get info from input box
    // populate data into object: newTask
    // setTasks([...tasks, newTask]);
    maxValueFromId(tasks)
  }

  return (
    <>
      <h1>To-Do List</h1>
      <form>
        <input type="text" placeholder="New Task"></input>
        <button onClick={addTask}>Add Task</button>
      </form>
      <ul>
        {tasks.map((task, i) => <li key={i}>{renderTask(task)}</li>)}
      </ul>
    </>
  )
}

export default App
