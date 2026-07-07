import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

function Navbar() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = async () => {
    await logout();
    navigate("/login");
  };

  return (
    <nav className="navbar">
      <div className="navbar-brand">📝 Todo List App</div>
      <div className="navbar-right">
        {user && (
          <>
            <span className="navbar-user">
              Hi, {user.username} {user.is_admin && <span className="admin-badge">Admin</span>}
            </span>
            {user.is_admin && (
              <button className="navbar-link" onClick={() => navigate("/admin")}>
                Admin Dashboard
              </button>
            )}
            {user.is_admin && (
              <button className="navbar-link" onClick={() => navigate("/home")}>
                My Tasks
              </button>
            )}
            <button className="logout-btn" onClick={handleLogout}>
              Logout
            </button>
          </>
        )}
      </div>
    </nav>
  );
}

export default Navbar;
