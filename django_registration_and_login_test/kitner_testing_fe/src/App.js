import React, {useEffect} from 'react';
import axios from 'axios';
import RegisterForm from "./pages/Register/RegisterForm";
import LoginForm from "./pages/Login/LoginForm";
import {
    Routes,
    Route,
} from "react-router-dom";
import Home from "./pages/Home/Home";

function App() {

    useEffect(() => {
        axios.get('http://localhost:8000/csrf_token/')
            .then(response => {
                document.cookie = `csrftoken=${response.data.csrf_token}`;
            }).catch(error => {
            console.log(error);
        });
    }, []);

    return (
        <Routes>
            <Route path="/" element={<RegisterForm/>}/>
            <Route path="/login" element={<LoginForm/>}/>
            <Route path="/home" element={<Home/>}/>
        </Routes>
    );
}

export default App;