function TaskItem({ task, onToggle, onDelete }) {
 return (
   <li className={`task-item ${task.completed ? "completed" : ""}`}>
     <div className="task-info" onClick={() => onToggle(task)}>
       <input
         type="checkbox"
         checked={task.completed}
         onChange={() => onToggle(task)}
       />
       <div>
         <p className="task-title">{task.title}</p>
         {task.description && (
           <p className="task-description">{task.description}</p>
         )}
       </div>
     </div>


     <button className="delete-btn" onClick={() => onDelete(task.id)}>
       Delete
     </button>

     <button className="edit-btn" onClick={() => onEdit(task)}>
       Edit
     </button>
   </li>
 );
}


export default TaskItem;



