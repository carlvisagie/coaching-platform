
import React from 'react';
import { HashRouter, Routes, Route } from "react-router-dom";
import EmotionDashboard from "./EmotionDashboard";

function App() {
  return (
    <HashRouter>
      <Routes>
        <Route path="/" element={<h1>Welcome to the Coaching Platform</h1>} />
        <Route path="/dashboard" element={<EmotionDashboard />} />
      </Routes>
    </HashRouter>
  );
}

export default App;
