import axios from "axios";

const API_URL = "http://127.0.0.1:8000/tasks";


export const getTasks = () => axios.get(`${API_URL}/`);


export const createTask = (task) => axios.post(`${API_URL}/`, task);


export const updateTask = (id, task) => axios.put(`${API_URL}/${id}`, task);


export const deleteTask = (id) => axios.delete(`${API_URL}/${id}`);


