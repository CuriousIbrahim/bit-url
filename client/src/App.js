import React from 'react';
import { Provider } from 'react-redux';

import Header from "./Components/Header/Header";
import MakeShortUrl from './Components/MakeShortUrl/MakeShortUrl';
import ListOfUrls from './Components/ListOfUrls/ListOfUrls';

import './App.css';

import { store } from './store';

function App() {
  return (
    <div className="App">
      <Provider store={store}>
        <Header />
        <MakeShortUrl />
        <ListOfUrls />
      </Provider>  
    </div>
  );
}

export default App;
