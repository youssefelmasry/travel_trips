import React, { Component } from 'react'
import FacebookLogin from 'react-facebook-login';

export default class Facebook extends Component {
    state = {
        isLoggedin: false,
        name: "",
        email: "",
        picture: "",
    };

    responseFacebook = (response) => {
        console.log(response);
        const axios = require('axios');
        console.log(response.accessToken);

        axios.post('http://52.15.72.6/social/facebook/', {
            access_token: response.accessToken,

        })
            .then(function (response) {
                console.log("server response");
                console.log(response);
            })
            .catch(function (error) {
                console.log("server response error");

                console.log(error);
            });

    };
    render() {
        return (
            <div>
                <FacebookLogin
                    appId="425294421745569"
                    autoLoad={true}
                    fields="name,email,picture"
                    callback={this.responseFacebook} />
            </div>
        )
    }
}

