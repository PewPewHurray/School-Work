import {useReducer} from "react";

const User = (props) => {

    const initialState = {
            firstName: {
                value: '',
                error: "Required"
            },
            lastName: {
                value: '',
                error: "Required"
            },
            email: {
                value: '',
                error: "Required"
            },
            hasBeenSubmitted: false
        };

    const reducer = (state, action) => {
        switch (action.type) {
            case "SET_FIRST_NAME_VALUE":
                return {
                    ...state,
                    firstName: {
                        ...state.firstName,
                        value: action.payload
                    }
                }
            case "SET_FIRST_NAME_ERROR":
                return {
                    ...state,
                    firstName: {
                        ...state.firstName,
                        error:action.payload
                    }
                }
            case "SET_LAST_NAME_VALUE":
                return {
                    ...state,
                    lastName: {
                        ...state.lastName,
                        value: action.payload
                    }
                }
            case "SET_LAST_NAME_ERROR":
                return {
                    ...state,
                    lastName: {
                        ...state.lastName,
                        error: action.payload
                    }
                }
            case "SET_EMAIL_VALUE":
                return {
                    ...state,
                    email: {
                        ...state.email,
                        value: action.payload
                    }
                }
            case "SET_EMAIL_ERROR":
                return {
                    ...state,
                    email: {
                        ...state.email,
                        error: action.payload
                    }
                }
            case "SET_SUBMITTED_BOOLEAN":
                return {
                    ...state,
                    hasBeenSubmitted: action.payload
                }
            default:
                return state;
        }
    }

    const [state, dispatch] = useReducer(reducer, initialState);

    const handleFirstNameChange = (e) => {
        if (e.target.value.length == 1) {
            dispatch({
                type: "SET_FIRST_NAME_ERROR",
                payload: "First Name must be at least 2 characters"
            });
        } else if (e.target.value.length < 1) {
            dispatch({
                type: "SET_FIRST_NAME_ERROR",
                payload: "Required"
            });
        } else {
            dispatch({
                type: "SET_FIRST_NAME_ERROR",
                payload: ""
            });
        }
        dispatch({
            type: "SET_FIRST_NAME_VALUE",
            payload: e.target.value
        });
    }

    const handleLastNameChange = (e) => {
        if (e.target.value.length == 1) {
            dispatch({
                type: "SET_LAST_NAME_ERROR",
                payload: "Last Name must be at least 2 characters"
            });
        } else if (e.target.value.length < 1) {
            dispatch({
                type: "SET_LAST_NAME_ERROR",
                payload: "Required"
            });
        } else {
            dispatch({
                type: "SET_LAST_NAME_ERROR",
                payload: ""
            });
        }
        dispatch({
            type: "SET_LAST_NAME_VALUE",
            payload: e.target.value
        });
    }

    const validateEmail = (e) => {
        if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(e.target.value))
            {
                return (true)
            }
        return (false)
}

    const handleEmailChange = (e) => {
        if (validateEmail(e)) {
            dispatch({
                type: "SET_EMAIL_ERROR",
                payload: ""
            });
        } else if (e.target.value.length < 1) {
            dispatch({
                type: "SET_EMAIL_ERROR",
                payload: "Required"
            });
        } else {
            dispatch({
                type: "SET_EMAIL_ERROR",
                payload: "Not a valid Email"
            });
        }
        dispatch({
            type: "SET_EMAIL_VALUE",
            payload: e.target.value
        });
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        dispatch({
            type: "SET_SUBMITTED_BOOLEAN",
            payload: true
        });
        dispatch({
            type: "SET_FIRST_NAME_VALUE",
            payload: initialState.firstName.value
        });
        dispatch({
            type: "SET_FIRST_NAME_ERROR",
            payload: initialState.firstName.error
        });
        dispatch({
            type: "SET_LAST_NAME_VALUE",
            payload: initialState.lastName.value
        });
        dispatch({
            type: "SET_LAST_NAME_ERROR",
            payload: initialState.lastName.error
        });
        dispatch({
            type: "SET_EMAIL_VALUE",
            payload: initialState.email.value
        });
        dispatch({
            type: "SET_EMAIL_ERROR",
            payload: initialState.email.error
        });
    }

        return (
            <div>
                <h1>{JSON.stringify(state)}</h1>
                {state.hasBeenSubmitted ? <h3>Form has been submitted!</h3> : null} 
                <form onSubmit={handleSubmit}>
                    <div>
                        <label htmlFor="firstname">First Name</label>
                        <input
                            id="firstname"
                            value={state.firstName.value}
                            onChange={(e) => handleFirstNameChange(e)}
                        />
                        {state.firstName.error?<p className="error">{state.firstName.error}</p>:null}
                    </div>
                    <div>
                        <label htmlFor="lastname">Last Name</label>
                        <input
                            id="lastname"
                            value={state.lastName.value}
                            onChange={(e) => handleLastNameChange(e)} 
                        />
                        {state.lastName.error?<p className="error">{state.lastName.error}</p>:null}
                    </div>
                    <div>
                        <label htmlFor="email">Email</label>
                        <input
                            id="email"
                            value={state.email.value}
                            onChange={(e) => handleEmailChange(e)} 
                        />
                        {state.email.error?<p className="error">{state.email.error}</p>:null}
                    </div>
                    {state.firstName.error
                        ?<input type="submit" value="Submit" disabled />
                        : state.lastName.error
                            ?<input type="submit" value="Submit" disabled />
                            :state.email.error
                                ?<input type="submit" value="Submit" disabled />
                                :<input type="submit" value="Submit" />}
                </form>
            </div>
        )
}

export default User;