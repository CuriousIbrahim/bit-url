import React from 'react';

import Header from "./Components/Header/Header";
import MakeShortUrl from './Components/MakeShortUrl/MakeShortUrl';
import ListOfUrls from './Components/ListOfUrls/ListOfUrls';

import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
        <Header />
        <MakeShortUrl />
        <ListOfUrls />
    </div>
  );
}

export default App;
