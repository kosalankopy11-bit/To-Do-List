import { useState } from "react";


function AddTask({ onAdd }) {
 const [title, setTitle] = useState("");
 const [description, setDescription] = useState("");


 const handleSubmit = (e) => {
   e.preventDefault(); 


   if (title.trim() === "") {
     alert("Task title ah kandippa type pannunga!");
  return;
   }


   onAdd({ title, description });


   setTitle("");
   setDescription("");
 };


 return (
   <form className="add-task-form" onSubmit={handleSubmit}>
     <input
       type="text"
       placeholder="Task title (edhavadhu vela)..."
       value={title}
       onChange={(e) => setTitle(e.target.value)}
     />
     <input
       type="text"
       placeholder="Description (optional)..."
       value={description}
       onChange={(e) => setDescription(e.target.value)}
     />
     <button type="submit">+ Add Task</button>
   </form>
 );
}


export default AddTask;
