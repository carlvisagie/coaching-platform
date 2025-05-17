
import React, { useEffect, useState } from "react";
import axios from "axios";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement, Tooltip, Legend);

const EmotionDashboard = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("/api/emotion_logs")
      .then((res) => setData(res.data))
      .catch(() => {
        setData([
          { date: "2025-05-10", emotion: "Anxiety", intensity: 6 },
          { date: "2025-05-11", emotion: "Stress", intensity: 7 },
          { date: "2025-05-12", emotion: "Calm", intensity: 3 },
          { date: "2025-05-13", emotion: "Sadness", intensity: 5 },
          { date: "2025-05-14", emotion: "Joy", intensity: 2 },
        ]);
      });
  }, []);

  const chartData = {
    labels: data.map(entry => entry.date),
    datasets: [{
      label: "Emotion Intensity",
      data: data.map(entry => entry.intensity),
      fill: false,
      borderColor: "#0070f3",
      tension: 0.4,
    }]
  };

  return (
    <div style={{ width: "100%", maxWidth: "800px", margin: "auto", padding: "2rem" }}>
      <h2>Emotional Resilience Dashboard</h2>
      <Line data={chartData} />
    </div>
  );
};

export default EmotionDashboard;
