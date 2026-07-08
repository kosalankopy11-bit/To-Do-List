import { useEffect, useState } from "react";
import { getTasks, createTask, updateTask, deleteTask } from "../api/taskApi";
import AddTask from "./AddTask";
import TaskItem from "./TaskItem";

function TaskList() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      const response = await getTasks();
      setTasks(response.data);
    } catch (error) {
      console.error("Tasks fetch error:", error);
    } finally {
      setLoading(false);
    }
  };


  const handleAdd = async (taskData) => {
    try {
      const response = await createTask(taskData);
      setTasks([...tasks, response.data]); 
    } catch (error) {
      console.error("Task add error:", error);
    }
  };

  
  const handleToggle = async (task) => {
    try {
      const response = await updateTask(task.id, {
        completed: !task.completed,
      });
     
      setTasks(
        tasks.map((t) => (t.id === task.id ? response.data : t))
      );
    } catch (error) {
      console.error("Task update  error:", error);
    }
  };


  const handleDelete = async (id) => {
    try {
      await deleteTask(id);
      setTasks(tasks.filter((t) => t.id !== id)); 
    } catch (error) {
      console.error("Task delete  error:", error);
    }
  };

  const handleEdit = async (id, updatedData) => {
    try {
      const response = await updateTask(id, updatedData);
      setTasks(tasks.map((t) => (t.id === id ? response.data : t)));
    } catch (error) {
      console.error("Task edit error:", error);
    }
  };

  if (loading) {
    return <p>Loading... (Loading tasks...)</p>;
  }

  return (
    <div className="task-list-container">
      <AddTask onAdd={handleAdd} />

      {tasks.length === 0 ? (
        <p className="empty-message"> No tasks available. So please add some tasks!</p>
      ) : (
        <ul className="task-list">
          {tasks.map((task) => (
            <TaskItem
              key={task.id}
              task={task}
              onToggle={handleToggle}
              onDelete={handleDelete}
              onEdit={handleEdit}
            />
          ))}
        </ul>
      )}
    </div>
  );
}

export default TaskList;
