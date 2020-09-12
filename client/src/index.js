import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

import * as firebase from 'firebase';

firebase.initializeApp({
  apiKey: "AIzaSyBjFV6pRtDO42cyfuzZmXrsMJEw5YbkeqE",
  authDomain: "newsusnetwork.firebaseapp.com",
  databaseURL: "https://newsusnetwork.firebaseio.com",
  projectId: "newsusnetwork",
  storageBucket: "newsusnetwork.appspot.com",
  messagingSenderId: "701371769717",
  appId: "1:701371769717:web:b6649579a8d4616079a93c",
  measurementId: "G-55BQ9KN7MZ"
});

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
