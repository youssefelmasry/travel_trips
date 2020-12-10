import React from 'react';
import ReactDOM from 'react-dom';
import Container from '@material-ui/core/Container';
import Slider from '../Nav/Slider';
import './Home.css';
import { Grid } from '@material-ui/core';


function Home() {
    return (<div>
        <Slider />
        <Grid className="grid" container >
            <Grid className="grid-left" item xs={6}>
                <h2>
                    Lorem ipsum dolor sit amet
                </h2>
                <p>
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


                </p>

            </Grid>
            <Grid item xs={6}>

                <img src="/images/7903.png" width="300"/>
            </Grid>
        </Grid>


    </div>)
}


export default Home