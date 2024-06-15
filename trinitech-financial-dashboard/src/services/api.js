
export const fetchFinancialData = async () => {
    try {
      const response = await fetch('/api/financial-data'); // Adjust URL as per your Flask route
      if (!response.ok) {
        throw new Error('Network response was not ok.');
      }
      return await response.json();
    } catch (error) {
      console.error('Error fetching financial data:', error);
      throw error;
    }
  };
  