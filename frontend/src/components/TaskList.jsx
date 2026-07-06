
import { useEffect, useState } from "react";
import { getTasks, createTask, updateTask, deleteTask } from "../api/taskApi";
import AddTask from "./AddTask";
import TaskItem from "./TaskItem";


// Idhu than main component - ella tasks um handle pandrathu
function TaskList() {
 const [tasks, setTasks] = useState([]);
 const [loading, setLoading] = useState(true);


 // Component load aaguravaga backend la irundhu tasks ah fetch pandrom
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


 // Puthu task add pandrathukku
 const handleAdd = async (taskData) => {
   try {
     const response = await createTask(taskData);
     setTasks([...tasks, response.data]); // Puthu task ah list oda add pandrom
   } catch (error) {
     console.error("Task add error:", error);
   }
 };


 // Task complete/incomplete nu toggle pandrathukku
 const handleToggle = async (task) => {
   try {
     const response = await updateTask(task.id, {
       completed: !task.completed,
     });
     // State la irukura antha task ah mattum update pandrom
     setTasks(
       tasks.map((t) => (t.id === task.id ? response.data : t))
     );
   } catch (error) {
     console.error("Task update  error:", error);
   }
 };


 // Task ah delete pandrathukku
 const handleDelete = async (id) => {
   try {
     await deleteTask(id);
     setTasks(tasks.filter((t) => t.id !== id)); // Delete pannina task ah list la irundhu eduthudrom
   } catch (error) {
     console.error("Task delete  error:", error);
   }
 };


 if (loading) {
   return <p>Loading... (tasks vara kaathurukom)</p>;
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
           />
         ))}
       </ul>
     )}
   </div>
 );
}


export default TaskList;
