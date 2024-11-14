// src/App.js
import React from 'react';
import './App.css';
import FileUpload from './components/FileUpload';
import FileList from './components/FileList';

function App() {
  const [reloadFiles, setReloadFiles] = React.useState(false);

  const handleUploadComplete = () => {
    setReloadFiles(!reloadFiles);
  };

  return (
    <div className="App">
      <div className="header">
        <img src={`${process.env.PUBLIC_URL}/logo.png`} alt="App Logo" className="logo" />
        <h1>Dropbox Clone</h1>
      </div>
      <FileUpload onUpload={handleUploadComplete} />
      <FileList key={reloadFiles} />
    </div>
  );
}

export default App;
