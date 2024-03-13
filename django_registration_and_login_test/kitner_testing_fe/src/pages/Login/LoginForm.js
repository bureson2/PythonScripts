import React, {useState} from 'react';
import bcrypt from "bcryptjs";
import {useNavigate} from "react-router-dom";
import style from "./style.module.scss";

const LoginForm = () => {
    const navigate = useNavigate();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
        bcrypt.genSalt(10, (err, salt) => {
            bcrypt.hash(password, salt, (err, hash) => {
                setPassword(hash);
            });
        });
        e.preventDefault();
        const data = {
            username,
            password,
        };

        try {
            const csrfToken = document.cookie.match(/csrftoken=([^;]+)/)[1];
            const response = await fetch('http://localhost:8000/login/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });

            if (response.status === 200) {
                console.log('User logged successfully');
                navigate('/home');
            } else {
                console.error('Failed to login user');
            }
        } catch (err) {
            console.error(err);
        }
    };

    return (
        <form onSubmit={handleSubmit}
              data-testid="login_form"
              id={style.login_form}>
            <label htmlFor="username"
                   data-testid="username_input_label">
                Username:
            </label>
            <input type="text"
                   id="username"
                   name="username"
                   placeholder="Username"
                   value={username}
                   onChange={e => setUsername(e.target.value)}
                   data-testid="username_input"/>
            <label htmlFor="password" data-testid="password_input_label">
                Password:
            </label>
            <input type="password"
                   id="password"
                   name="password"
                   placeholder="password"
                   value={password}
                   onChange={e => setPassword(e.target.value)}
                   data-testid="password_input"/>
            <button type="submit"
                    value="Submit"
                    data-testid="submit_button"
                    id={style.submit_button}
            >
                Submit
            </button>
        </form>
    );
}

export default LoginForm;
