import React, {useState} from 'react';
import { useNavigate } from 'react-router-dom';
import bcrypt from 'bcryptjs';
import style from './style.module.scss'

const RegisterForm = () => {
    const navigate = useNavigate();
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [passwordAgain, setPasswordAgain] = useState('');

    const handleSubmit = async (e) => {
        bcrypt.genSalt(10, (err, salt) => {
            bcrypt.hash(password, salt, (err, hash) => {
                setPassword(hash);
            });
            bcrypt.hash(passwordAgain, salt, (err, hash) => {
                setPasswordAgain(hash);
            });
        });
        e.preventDefault();
        const data = {
            username,
            email,
            password,
            passwordAgain
        };

        try {
            const csrfToken = document.cookie.match(/csrftoken=([^;]+)/)[1];
            const response = await fetch('http://localhost:8000/register/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });

            if (response.status === 200) {
                console.log('User registered successfully');
                navigate('/login');
            } else {
                console.error('Failed to register user');
            }
        } catch (err) {
            console.error(err);
        }
    };

    return (
        <form onSubmit={handleSubmit}
              data-testid="registration_form"
              id={style.registration_form}
        >
            <label htmlFor="email"
                   data-testid="email_input_label">
                Email:
            </label>
            <input type="text"
                   id="email"
                   name="email"
                   placeholder="email@gmail.com"
                   value={email}
                   onChange={e => setEmail(e.target.value)}
                   data-testid="email_input"
                   data-test="email_input"
            />
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
            <label htmlFor="password_again"
                   data-testid="password_again_input_label">
                Password again:
            </label>
            <input type="password"
                   id="password_again"
                   name="password_again"
                   placeholder="password again"
                   value={passwordAgain}
                   onChange={e => setPasswordAgain(e.target.value)}
                   data-testid="password_again_input"/>
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

export default RegisterForm;
