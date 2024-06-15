import React, { useEffect, useState } from 'react';
import Chart from '../Chart/Chart'; 
import './Dashboard.css'; 
import { fetchFinancialData } from '../../services/api'; 

function Dashboard() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchFinancialData()
      .then(response => setData(response.data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div className="dashboard">
      <h1>Financial Dashboard</h1>
      <div className="charts">
        <Chart data={data} />
        {/* Add more charts or components as needed */}
      </div>
    </div>
  );
}

export default Dashboard;
