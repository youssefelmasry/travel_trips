import {
    BrowserRouter as Router,

    Link
} from "react-router-dom";
import { menuItems } from './navitems';
import React, { Component } from 'react'
import {
    BrowserView,
    MobileView,
    isBrowser,
    isMobile
} from "react-device-detect";
import { Button, Drawer } from "@material-ui/core";
import PersistentDrawerLeft from "./drawer"
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';

let api_url = 'http://localhost:8000/api/'
export default class Nav extends Component {
    handleClick() {
        const axios = require('axios');

        axios.get(api_url)
            .then(function (response) {
                // handle success
                console.log(response);
            })
            .catch(function (error) {
                // handle error
                console.log(error);
            })
            .then(function () {
                // always executed
            });
    }

    renderContent = () => {
        if (isMobile) {
            return <div>   <Router>
                <PersistentDrawerLeft />
                <Link to="/" className="logo">
                    Tourism
                </Link>

            </Router>

            </div>
        }
        return <div>       <AppBar position="static" className="top-header">
            <Router>
                <nav >
                    <Link to="/ " className="navbar-logo">
                        Tourism
             </Link><div className="navigation">

                        <ul className="Nav-desktop">
                            {menuItems.map((item, index) => {
                                return (<li className={item.title}>
                                    <Link to={item.url}>
                                        {item.title}
                                    </Link>
                                </li>)
                            })}
                        </ul>

                    </div>
                </nav>

            </Router>
            <button onClick={this.handleClick}>
                Test Backend
            </button>


        </AppBar>

        </div>

    }
    render() {
        return this.renderContent();
    }
}


