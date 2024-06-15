import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import { fetchFinancialData } from '../../services/api';

function Chart() {
  const [financialData, setFinancialData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await fetchFinancialData();
        setFinancialData(data);
      } catch (error) {
        console.error('Error fetching financial data:', error);
      }
    };

    fetchData();
  }, []);

  const chartData = {
    labels: financialData.map(data => data.id),
    datasets: [
      {
        label: 'Revenue',
        data: financialData.map(data => data.revenue),
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1,
      },
      {
        label: 'Gross Profit',
        data: financialData.map(data => data.gross_profit),
        fill: false,
        borderColor: 'rgb(54, 162, 235)',
        tension: 0.1,
      },
      {
        label: 'Net Income',
        data: financialData.map(data => data.net_income),
        fill: false,
        borderColor: 'rgb(255, 99, 132)',
        tension: 0.1,
      },
    ],
  };

  return (
    <div className="chart-container">
      <h2>Financial Data Chart</h2>
      <Line data={chartData} />
    </div>
  );
}

export default Chart;
