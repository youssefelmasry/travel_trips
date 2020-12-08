import React from 'react';
import logo from './logo.svg';
import './App.css';

import Nav from './Component/Nav/Nav';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import Home from './Component/pages/Home';

function App() {
  return (
    <div className="App">
      <Nav />
      <Router>

        <Switch>
          <Route path="/about">
            <Home />
          </Route>
          <Route path="/topics">
            <Home />
          </Route>
          <Route exact path="/">
            <Home />
          </Route>
        </Switch>


      </Router>

    </div>
  );
}

export default App;
