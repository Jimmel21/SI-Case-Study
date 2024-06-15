import React from 'react';
import './Sidebar.css'; 

function Sidebar() {
  return (
    <div className="sidebar">
      <div className="logo">
        <h2>Financial App</h2>
      </div>
      <nav className="nav-links">
        <ul>
          <li>
            <a href="/">Dashboard</a>
          </li>
          <li>
            <a href="/reports">Reports</a>
          </li>
          {/* Add more navigation items as needed */}
        </ul>
      </nav>
    </div>
  );
}

export default Sidebar;
