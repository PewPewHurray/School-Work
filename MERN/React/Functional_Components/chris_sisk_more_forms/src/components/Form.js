import React, {useState} from "react";

const Form = (props) =>{
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [firstNameError, setFirstNameError] = useState("");
    const [lastNameError, setLastNameError] = useState("");
    const [emailError, setEmailError] = useState("");
    const [passwordError, setPasswordError] = useState("");
    const [confirmPasswordError, setConfirmPasswordError] = useState("");


    const createUser = (e) => {
        e.preventDefault();

        const newUser = {firstName, lastName, email, password, confirmPassword};
        setFirstName("");
        setLastName("");
        setEmail("");
        setPassword("");
        setConfirmPassword("");
    };

    const handleFirstName = (e) => {
        setFirstName(e.target.value);
        if(e.target.value.length < 2){
            setFirstNameError("First Name must be at least 2 characters");
        } else {
            setFirstNameError("");
        }
    }

    const handleLastName = (e) => {
        setLastName(e.target.value);
        if(e.target.value.length < 2){
            setLastNameError("First Name must be at least 2 characters");
        } else {
            setLastNameError("");
        }
    }

    const handleEmail = (e) => {
        setEmail(e.target.value);
        if(e.target.value.length < 5){
            setEmailError("Email must be at least 5 characters");
        } else {
            setEmailError("");
        }
    }

    const handlePassword = (e) => {
        setPassword(e.target.value);
        if(e.target.value.length < 8){
            setPasswordError("Password must be at least 8 characters");
        } else {
            setPasswordError("");
        }
    }

    const handleConfirmPassword = (e) => {
        setConfirmPassword(e.target.value);
        if(e.target.value != password){
            setConfirmPasswordError("Password does not match");
        } else {
            setConfirmPasswordError("");
        }
    }

    return(
        <div>
            <form onSubmit={createUser}>
                <div>
                    <label>First Name: </label>
                    <input type="text" onChange={handleFirstName} value={firstName} />
                    {firstNameError ? <p className="error">{firstNameError}</p>: ''}
                </div>
                <div>
                    <label>Last Name: </label>
                    <input type="text" onChange={handleLastName} value={lastName} />
                    {lastNameError ? <p className="error">{lastNameError}</p>: ''}
                </div>
                <div>
                    <label>Email: </label>
                    <input type="text" onChange={handleEmail} value={email}/>
                    {emailError ? <p className="error">{emailError}</p>: ''}
                </div>
                <div>
                    <label>Password: </label>
                    <input type="text" onChange={handlePassword} value={password} />
                    {passwordError ? <p className="error">{passwordError}</p>: ''}
                </div>
                <div>
                    <label>Confirm Password: </label>
                    <input type="text" onChange={handleConfirmPassword} value={confirmPassword} />
                    {confirmPasswordError ? <p className="error">{confirmPasswordError}</p>: ''}
                </div>
                <input type="submit" value="Create User" />
            </form>
        </div>
    );
};

export default Form;