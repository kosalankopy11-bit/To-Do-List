import { useState } from "react";

function TaskItem({ task, onToggle, onDelete, onEdit }) {
  const [isEditing, setIsEditing] = useState(false);
  const [editTitle, setEditTitle] = useState(task.title);
  const [editDescription, setEditDescription] = useState(task.description || "");

  const startEdit = () => {
    setEditTitle(task.title);
    setEditDescription(task.description || "");
    setIsEditing(true);
  };

  const cancelEdit = () => {
    setIsEditing(false);
  };

  const saveEdit = () => {
    if (editTitle.trim() === "") {
      alert("Task title ah kandippa type pannunga!");
      return;
    }
    onEdit(task.id, { title: editTitle, description: editDescription });
    setIsEditing(false);
  };

  if (isEditing) {
    return (
      <li className="task-item editing">
        <div className="edit-form">
          <input
            type="text"
            className="edit-title-input"
            value={editTitle}
            onChange={(e) => setEditTitle(e.target.value)}
            placeholder="Task title..."
          />
          <input
            type="text"
            className="edit-description-input"
            value={editDescription}
            onChange={(e) => setEditDescription(e.target.value)}
            placeholder="Description (optional)..."
          />
          <div className="edit-actions">
            <button className="save-btn" onClick={saveEdit}>
              Save
            </button>
            <button className="cancel-btn" onClick={cancelEdit}>
              Cancel
            </button>
          </div>
        </div>
      </li>
    );
  }

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

      <div className="task-actions">
        <button
          className="edit-btn"
          onClick={(e) => {
            e.stopPropagation();
            startEdit();
          }}
        >
          Edit
        </button>
        <button
          className="delete-btn"
          onClick={(e) => {
            e.stopPropagation();
            onDelete(task.id);
          }}
        >
          Delete
        </button>
      </div>
    </li>
  );
}

export default TaskItem;
